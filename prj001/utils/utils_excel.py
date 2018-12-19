import pandas as pd

obj_str = {
    'clinicalconclusion': '临床诊断',
    'other': '其他病症',
    'symptom': '全身症状',
    'menstruation': '月经情况',
    'geninfo': '一般信息'
}

table_title = {
    'fg_color': '#D7E4BC',
    'bold': True,
    'font_size': '23',
}

inner_table_key = {
    'fg_color': '#ABEBC6',
    'font_size': '18',
    'align': 'center',
    'bottom': 1,
    'font_charset': 'utf-8'
}

inner_table_value = {
    'fg_color': '#AED6F1',
    'font_size': '18',
    'align': 'center',
    'bottom': 1,
    'font_charset': 'utf-8'
}


def save_excel(s):
    """s是序列化器对象"""
    data_json = s.data

    # 创建一个表
    pd.set_option('display.max_colwidth', 1000)
    df = pd.DataFrame()
    writer = pd.ExcelWriter('excel_name.xlsx', engine='xlsxwriter')

    for index, item in enumerate(data_json):

        p, q = 0, 1
        m, n = 0, 4
        for key, value in list(item.items()):
            sheet_name = item['name']
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            ws = writer.sheets[sheet_name]
            wb = writer.book

            format01 = wb.add_format()
            format01.set_bold(True)
            table_title_style = wb.add_format(table_title)
            inner_table_key_style = wb.add_format(inner_table_key)
            inner_table_value_style = wb.add_format(inner_table_value)

            ws.write(0, 0, obj_str['geninfo'], table_title_style)
            if isinstance(value, type(None)):
                # 如果是空对象, 直接删除当前的单元格
                # item[key] = '该患者无此相关信息'
                item.pop(key)
            else:
                if isinstance(value, str) or isinstance(value, bool) or isinstance(value, int):
                    # 保存正常的key,value
                    ws.write(p, q, key, format01)
                    if isinstance(value, bool):
                        if value:
                            ws.write(p, q + 1, '有', inner_table_value_style)
                        else:
                            ws.write(p, q + 1, '无', inner_table_value_style)
                    else:
                        ws.write(p, q + 1, value, inner_table_value_style)
                    p += 1
                else:

                    if key in [key for key in obj_str]:
                        ws.write(0, n-1, obj_str[key], table_title_style)

                    # 如果不空, 创建
                    _obj = item.pop(key)

                    for ks, vs in list(_obj.items()):
                        if ks in ('url', 'person', 'owner'):
                            _obj.pop(ks)
                            continue
                        ws.write(m, n, ks, inner_table_key_style)

                        if isinstance(vs, bool):
                            if vs:
                                ws.write(m, n + 1, '有', inner_table_value_style)
                            else:
                                ws.write(m, n + 1, '无', inner_table_value_style)
                        else:
                            ws.write(m, n + 1, vs, inner_table_value_style)

                        m += 1

                    m, n = 0, n+3
    writer.save()






