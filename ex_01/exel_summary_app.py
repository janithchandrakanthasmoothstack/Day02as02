import sys
from openpyxl import load_workbook

baseDIR = ("E:\learn\problem_01")

def fileNameValidator(fileName):
    fileParts = fileName.split("_");
    monthlist = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                 'november', 'december']

    try:
        if(fileParts[0]!='expedia'):
            return "Incorrect File Name: File Name should start with the word expedia"
        elif fileParts[1]!='report':
            return "Incorrect File Name: File name second part should be 'report'"
        elif fileParts[2]!='monthly':
            return "Incorrect File Name: File third part should be the word 'monthly'"
        elif monthlist.count(fileParts[3])==0:
            return "Incorrect File Name: Fourth Part, Month name format error"
        elif int(fileParts[4].split(".")[0])<1900:
            return "Incorrect File Name: Fifth part, incorrect Year Found"
        else: return [fileParts[3],int(fileParts[4].split(".")[0])]
    except OSError as err:return "Incorrect File Name Found: {0}".format(err)

def main():
    fileName = input("File Name Please: ")
    # fileName = 'expedia_report_monthly_january_20x8.xlsx'
    validateResponse = fileNameValidator(fileName)

    if isinstance(validateResponse,list):
        #read file basic
        print(validateResponse)
        book = load_workbook(baseDIR+"\\"+fileName)
        sheet = book.active
        rows = sheet.rows
        cols = sheet.columns
        for x in rows:
            print(x[0].value)
        # headers = next(rows)

        # headers = [cell.value for cell in next(rows)]
        # print(headers)
        # for row in rows:
        #     data = {}
        #     for title,cell in zip(headers,row):
        #         data[title] = cell.value
        #     print(data)

        # sheet_2 = workbook.get_sheet(1)



if __name__ == '__main__':main()
