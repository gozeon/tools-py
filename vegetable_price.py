import requests
import xlsxwriter
from datetime import datetime

eudName = "天津市红旗农贸综合批发市场有限公司"
def fetchData(data, result):
    response = requests.post("http://nc.mofcom.gov.cn/jghq/marketDetail", data)
    res = response.json()
    print(res)
    if res['result'] is not None:
        result += res['result']
    if res['hasNext'] is True:
        nextData = data
        nextData['pageNo'] = res['nextPage']
        return fetchData(nextData, result)
    return result

postData = {
    'eudName': eudName,
    "queryDateType": 0,
}
result = fetchData(postData, [])
print(result)

def writeExcel(filename, data):
    # Create a new Excel file
    workbook = xlsxwriter.Workbook(filename)

    # Add a worksheet
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    # Write header row
    header_row = 0
    headers = ['日期', '产品', '价格', '市场']
    for col, header in enumerate(headers):
        worksheet.write(header_row, col, header, bold)

    # Write data rows
    for row, item in enumerate(data):
        worksheet.write(row + 1, 0, datetime.fromtimestamp(item['GET_P_DATE'] / 1000).strftime("%Y-%m-%d"))
        worksheet.write(row + 1, 1, item['CRAFT_NAME'])
        worksheet.write(row + 1, 2, "{} {}".format(item['AG_PRICE'],item['C_UNIT']))
        worksheet.write(row + 1, 3, item['EUD_NAME'])

    # Close the workbook
    workbook.close()

writeExcel('{}.xlsx'.format(eudName), result)

