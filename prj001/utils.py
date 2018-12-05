from .models import GeneralInfo, Menstruation, Symptom, ClinicalConclusion, Other
from django.core.files.uploadedfile import InMemoryUploadedFile

from myusers.models import MyUser
from rest_framework import serializers
from django.conf import settings


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
    # print(info.get(""))

    gen_info = GeneralInfo(**info, owner_id=owner_id)
    gen_info.save()

    info_id = gen_info.id

    # 2.月经情况
    men_info = Menstruation(**menstruation, owner_id=owner_id, person_id=info_id)
    # 3.全身情况
    sy_info = Symptom(**symptom, owner_id=owner_id, person_id=info_id)
    # 4.其他情况
    ot_info = Other(**other, owner_id=owner_id, person_id=info_id)
    # 5.临床诊断
    con_info = ClinicalConclusion(**conclusion, owner_id=owner_id, person_id=info_id)

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


def validate_file(data):
    """
    InvestFileUploadSerializer 验证
    :param data:
    :return:
    """
    try:
        user = MyUser.objects.filter(id=data["owner_id"])
    except Exception as e:
        raise serializers.ValidationError("用户查询错误")

    if not user:
        raise serializers.ValidationError("用户不存在")

    file_obj = data['ivfile']

    if not file_obj:
        raise serializers.ValidationError("并未选择文件")

    if not (type(file_obj) == InMemoryUploadedFile):
        raise serializers.ValidationError("上传的非文件类型")

    file_name = file_obj.name

    upload_type = file_name.split(".")[::-1][0]

    print(upload_type)

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

    p_id = data.get("person_id", None)

    print(p_id)

    if not p_id:
        raise serializers.ValidationError("表内容填写不完整")

    if sf.context["view"].action == "create":

        try:
            obj_obj = obj.objects.filter(id=p_id)
        except obj.DoesNotExist:
            raise serializers.ValidationError("一般信息表格不存在")

        try:
            obj_own = obj_o.objects.filter(person_id=p_id)
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
    person_id = s.validated_data["person_id"]

    person = obj.objects.get(id=person_id)

    s.save(owner=sf.request.user, person=person)

