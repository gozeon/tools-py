import os

import requests
import xlsxwriter

api_url = os.getenv("api_url")
project_id = os.getenv("project_id")

# 获取项目
response = requests.get("{}/api/project/{}".format(api_url, project_id))
project_res = response.json()
project_info = project_res['data']

# 获取记录
response = requests.get("{}/api/record/{}".format(api_url, project_id))
record_res = response.json()
record_info = record_res['data']

# 写入
workbook = xlsxwriter.Workbook('{}.xlsx'.format(project_info['title']))
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write_row(0, 0, ['标题', '状态'], bold)

B_width = 0
row_num = 1
for record in record_info:
    worksheet.write(row_num, 0, record["title"])
    worksheet.write(row_num, 1, ["", "提议", "通过",
                    "完成", "已弃用", "已取代"][record["status"]])
    row_num += 1
    B_width = max(len(record["title"]), B_width)

worksheet.set_column('A:A', B_width * 1.9)
worksheet.set_column('B:B', 3 * 1.9)

format1 = workbook.add_format({'bg_color': '#F2D388', 'font_color': '#ffffff'})
format2 = workbook.add_format({'bg_color': '#377D71', 'font_color': '#ffffff'})
format3 = workbook.add_format({'bg_color': '#E41655', 'font_color': '#ffffff'})
format4 = workbook.add_format({'bg_color': '#B30753', 'font_color': '#ffffff'})

worksheet.conditional_format('B1:B%d' % row_num,    {'type':     'text',
                                                     'criteria': 'containing',
                                                     'value':    '提议',
                                                     'format':   format1})
worksheet.conditional_format('B1:B%d' % row_num,    {'type':     'text',
                                                     'criteria': 'containing',
                                                     'value':    '通过',
                                                     'format':   format2})

worksheet.conditional_format('B1:B%d' % row_num,    {'type':     'text',
                                                     'criteria': 'containing',
                                                     'value':    '已弃用',
                                                     'format':   format3})
worksheet.conditional_format('B1:B%d' % row_num,    {'type':     'text',
                                                     'criteria': 'containing',
                                                     'value':    '已取代',
                                                     'format':   format4})
workbook.close()
