from prj001.models import GeneralInfo, Menstruation, Symptom, ClinicalConclusion, Other

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.db import transaction

from rest_framework import serializers, status
from rest_framework import exceptions
from datetime import datetime

# 引入读取离线文件的工具包
from utils.read_file_util.questionairetojson import readQuestionaireExcel
from utils.read_file_util.exception import UploadFileException
from prj001.pagination import GenPage
from .constants import qita_

import urllib.parse
import json


def save_table_data(data_dict, request):
    """
    保存表格中的数据至数据库
    """
    info = data_dict.get("general_info")
    menstruation = data_dict.get("menstruation")
    symptom = data_dict.get("symptom")
    other = data_dict.get("other")
    conclusion = data_dict.get("conclusion")

    owner_id = data_dict.get("owner_id")

    serial = info.get('serial')

    try:
        obj_of_info = GeneralInfo.objects.filter(serial=serial)

    except GeneralInfo.DoesNotExist:
        raise

    recdate = info.pop("recdate")

    qt_update('info', info)
    qt_update('symptom', symptom)
    qt_update('other', other)
    qt_update('conclusion', conclusion)

    iii = datetime.strptime(recdate, '%Y-%m-%d')
    ii = iii.strftime('%Y-%m-%d')
    info['recdate'] = ii
    if not obj_of_info:
        with transaction.atomic(savepoint=True):
            point = transaction.savepoint()
            try:
                gen_info = GeneralInfo(owner_id=owner_id, **info)
                gen_info.save()

                info_id = gen_info.id

                men_info = Menstruation(
                    owner_id=owner_id,
                    person_id=info_id,
                    **menstruation)

                sy_info = Symptom(
                    owner_id=owner_id,
                    person_id=info_id,
                    **symptom)

                ot_info = Other(
                    owner_id=owner_id,
                    person_id=info_id,
                    **other)

                con_info = ClinicalConclusion(
                    owner_id=owner_id,
                    person_id=info_id,
                    **conclusion)

                save_table(men_info)
                save_table(sy_info)
                save_table(con_info)
                save_table(ot_info)

            except Exception as e:
                transaction.savepoint_rollback(point)
                raise e

            transaction.savepoint_commit(point)
    else:
        # 存在, 修改
        if len(obj_of_info) == 1:
            owner = obj_of_info[0].owner
            if request.user == owner:
                with transaction.atomic(savepoint=True):
                    point_update = transaction.savepoint()

                    try:
                        obj_of_info.update(**info)
                        person_id = obj_of_info[0].id
                        num_men = Menstruation.objects.filter(person_id=person_id).update(**menstruation)
                        num_sym = Symptom.objects.filter(person_id=person_id).update(**symptom)
                        num_oth = Other.objects.filter(person_id=person_id).update(**other)
                        num_cli = ClinicalConclusion.objects.filter(person_id=person_id).update(**conclusion)
                        if not (num_cli == 1 and num_men == 1 and num_oth == 1 and num_sym == 1):
                            raise ValueError('update error')
                    except Exception as e:
                        transaction.savepoint_rollback(point_update)
                        raise ValueError('数据库更新错误%s' % e)

                    transaction.savepoint_commit(point_update)
            else:
                data = {
                    'code': status.HTTP_403_FORBIDDEN,
                    'detail': '您目前对该信息无修改权限, 如需修改请联系%s' % owner.email,
                }
                exceptions.PermissionDenied.default_detail = data
                raise exceptions.PermissionDenied
        else:
            raise ValueError('数据库中编码不唯一')


def validate_file(data):
    """
    InvestFileUploadSerializer 验证
    :param data:
    :return:
    """

    file_obj = data['ivfile']

    if not file_obj:
        raise serializers.ValidationError("并未选择文件")

    if not (type(file_obj) == InMemoryUploadedFile):
        raise serializers.ValidationError("上传的非文件类型")

    file_name = file_obj.name

    upload_type = file_name.split(".")[::-1][0]

    # print(upload_type)

    if upload_type not in settings.UPLOAD_FILE_TYPE:
        raise serializers.ValidationError("文件类型不允许")

    return data


def validate_person(sf, obj, obj_o, data):
    """
    :param sf: self
    :param obj: Generalinfo 数据表名称
    :param obj_o: 即将创建表的名称
    :param data: 需要验证的数据
    :return: data
    """

    p_id = data.get("person", None)

    # print(p_id.id, type(p_id), "-------validate_person--------")

    if not p_id:
        raise serializers.ValidationError("表内容填写不完整")

    if sf.context["view"].request.method == "POST":

        try:
            obj_obj = obj.objects.filter(id=p_id.id)
        except obj.DoesNotExist:
            raise serializers.ValidationError("一般信息内容不存在")

        try:
            obj_own = obj_o.objects.filter(person_id=p_id.id)
        except obj_o.DoesNotExist:
            pass
        else:
            if obj_own:
                raise serializers.ValidationError("已经存在有对应的信息")

        if not obj_obj:
            raise serializers.ValidationError("一般信息表格不存在")

    else:
        pass

    return data


def perform_create_content(sf, obj, s):
    """
    :param sf:  self参数
    :param obj:  GenInfo固定对象
    :param s: 序列化对象
    :return:
    """
    person_id = s.validated_data["person"]

    try:
        person = obj.objects.get(id=person_id.id)
    except obj.DoesNotExist:
        raise

    owner = person.owner

    if sf.request.user == owner:
        s.save(owner=sf.request.user, person=person)
    else:
        # print(sf.request.user, person.owner)
        data = {
            'detail': '您目前对该信息无修改权限, 如需修改请联系%s' % owner.email,
            'name': owner.email,
        }
        raise exceptions.PermissionDenied(detail=data)


def create_file_view(s, data, request):
    """
    上传文件视图的数据分析实现方式
    :param s: serializer序列化对象
    :param data: 返回的字典参数
    :return: data
    """
    # 检查文件类型
    file_path = s.data["ivfile"]
    tmp_str = file_path.split('/', 2)
    file_path = settings.MEDIA_ROOT + "/" + tmp_str[2]
    de_path = urllib.parse.unquote(file_path)

    try:
        file_data = readQuestionaireExcel(de_path)
        # print(file_data, type(file_data), "file_data--->>>>")
    except UploadFileException:
        raise UploadFileException
    except Exception as e:
        data["code"] = 1441
        data["msg"] = "文件数据无法分析,查看上传文件是否为模板文件%s" % e
        return data

    # 去除文字内容两边的空格
    try:
        outer_dict = dict()
        inner_dict = dict()
        json_data_dict = json.loads(file_data)
        # print(type(json_data_dict))
        for index, item in json_data_dict.items():
            for i, value in json_data_dict[index].items():
                if isinstance(value, str):
                    inner_dict[i] = value.strip()
                else:
                    inner_dict[i] = value
                
            outer_dict[index] = inner_dict
            inner_dict = dict()
    except Exception as e:
        data["code"] = 1442
        data["msg"] = e
        return data 

    data_str = json.dumps(s.data)

    try:
        data_dict = json.loads(data_str)
    except Exception as e:
        data["code"] = status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
        data["msg"] = "数据转化发生错误 %s" % e
        return data

    # 返回的整体的json数据
    data_dict.update(outer_dict)

    try:
        save_table_data(data_dict, request)
    except exceptions.PermissionDenied:
        return exceptions.PermissionDenied.default_detail
    except Exception as e:
        data["code"] = 1400
        data["msg"] = "数据保存失败 %s！！" % e
        return data

    data["code"] = status.HTTP_200_OK
    data["msg"] = "文件上传成功"
    return data


def group_permission_show(data):
    """
    相当于 def get_queryset(self): 方法重写
    作用: 限制内容只显示给同一组内成员
    :param data:
    :return:
    """
    _ID = []

    groups_queryset = data.request.user.groups.all()

    users_queryset = [g.user_set.all() for g in groups_queryset]

    for u in users_queryset:
        for i in u:
            _ID.append(i.id)

    if not _ID:
        _ID.append(data.request.user.id)

    return GeneralInfo.objects.filter(owner__in=_ID).order_by("-id")


def get_and_post(request, queryset):
    """GET/POST请求页面关于page"""
    gen_page = GenPage()

    every_data = gen_page.paginate_queryset(queryset=queryset, request=request)

    return every_data


# class JudgeStrType(object):
#     """
#     判断字符类型
#     """
#     # 判断一个unicode是否是汉字
#     @staticmethod
#     def is_chinese(s):
#         if '\u4e00' <= s <= '\u9fff':
#             return True
#         else:
#             return False
#
#     # 判断一个unicode是否是数字
#     @staticmethod
#     def is_number(s):
#         return s.isdigit(s)
#
#     # 判断一个unicode是否是英文字母
#     @staticmethod
#     def is_alphabet(s):
#         if ('\u0041' <= s <= '\u005a') or ('\u0061' <= s <= '\u007a'):
#             return True
#         else:
#             return False

def save_table(table_name):
    try:
        table_name.save()
    except Exception as e:
        raise e


def qt_update(st, obj):
    v = qita_[st]
    for value in v:
        print(obj[value])
        if isinstance(obj[value], bool) and obj[value]:
            obj[value] = '其他'
        elif isinstance(obj[value], bool):
            obj[value] = ''

