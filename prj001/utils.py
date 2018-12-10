from .models import GeneralInfo, Menstruation, Symptom, ClinicalConclusion, Other

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.db import transaction

from rest_framework import serializers, status
from rest_framework.response import Response

# 引入读取离线文件的工具包
from utils.read_file_util.questionairetojson import readQuestionaireExcel

import urllib.parse
import json


def save_table_data(data_dict):
    """
    保存表格中的数据至数据库
    :return:
    """
    info = data_dict.get("general_info")
    menstruation = data_dict.get("menstruation")
    symptom = data_dict.get("symptom")
    other = data_dict.get("other")
    conclusion = data_dict.get("conclusion")

    owner_id = data_dict.get("owner_id")

    # 1.一般情况
    #######
    info.pop("recdate")
    with transaction.atomic():
        point = transaction.savepoint()

        try:
            gen_info = GeneralInfo(owner_id=owner_id, **info)
            gen_info.save()

            info_id = gen_info.id

            # 2.月经情况
            men_info = Menstruation(owner_id=owner_id, person_id=info_id, **menstruation)
            # 3.全身情况
            sy_info = Symptom(owner_id=owner_id, person_id=info_id, **symptom)
            # 4.其他情况
            ot_info = Other(owner_id=owner_id, person_id=info_id, **other)
            # 5.临床诊断
            con_info = ClinicalConclusion(owner_id=owner_id, person_id=info_id, **conclusion)


            try:
                men_info.save()
            except Exception as e:
                raise e

            try:
                sy_info.save()
            except Exception as e:
                raise e

            try:
                ot_info.save()
            except Exception as e:
                raise e

            try:
                con_info.save()
            except Exception as e:
                raise e
        except Exception as e:
            transaction.savepoint_rollback(point)
            raise e

        transaction.savepoint_commit(point)


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

    print(p_id.id, type(p_id), "-------validate_person--------")

    if not p_id:
        raise serializers.ValidationError("表内容填写不完整")

    if sf.context["view"].action == "create":

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
    :param obj:  对象
    :param s: 序列化对象
    :return:
    """
    person_id = s.validated_data["person"]

    person = obj.objects.get(id=person_id.id)

    s.save(owner=sf.request.user, person=person)


def create_file_view(s, data):
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
    # print(de_path, "+++++++++++")

    # if "Microsoft Excel" in :
    #
    # 参数是文件路径
    try:
        file_data = readQuestionaireExcel(de_path)
    except Exception as e:
        data["code"] = 1441
        data["msg"] = "文件数据无法分析,查看上传文件是否为模板文件"
        return Response(data)
    #
    #     # #########old v
    #     # # 读取文件内容，进行处理
    #     # wb = xlrd.open_workbook(de_path)
    #     # table = wb.sheets()[0]
    #     # row = table.nrows
    #     # for i in range(1, row):
    #     #     col = table.row_values(i)
    #     #     print(col)
    # else:
    #     resp_data["code"] = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    #     resp_data["msg"] = "文件格式不是Excel"
    #     return Response(resp_data)

    # if "ASCII text" in checkresult:
    #     file_object = open('test.txt')
    #     try:
    #         file_context = file_object.read()
    #         print(file_context)
    #         # file_context是一个list，每行文本内容是list中的一个元素
    #         # file_context = open(file).read().splitlines()
    #     finally:
    #         file_object.close()
    # else:
    #     return Response(data="上传文件不是文本文件！", status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    data_str = json.dumps(s.data)

    try:
        data_dict = json.loads(data_str)

        data_dict_file = json.loads(file_data)
    except Exception as e:
        data["code"] = status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
        data["msg"] = "数据转化发生错误"
        return Response(data)

    # 返回的整体的json数据
    data_dict.update(data_dict_file)

    try:
        save_table_data(data_dict)
    except Exception as e:
        print(e)
        data["code"] = 1400
        data["msg"] = "数据保存失败！！"
        return Response(data)

    data["code"] = status.HTTP_200_OK
    # resp_data["msg"] = data_dict

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

    return GeneralInfo.objects.filter(owner__in=_ID)
