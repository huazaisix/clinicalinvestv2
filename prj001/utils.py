from .models import GeneralInfo, Menstruation, Symptom, ClinicalConclusion, Other


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

    owner_id = data_dict.get("owner")

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
        sy_info.save()
        ot_info.save()
        con_info.save()
    except Exception as e:
        raise e
