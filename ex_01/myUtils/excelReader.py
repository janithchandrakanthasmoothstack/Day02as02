from openpyxl import load_workbook


baseDIR = ("E:\learn\problem_01")

def excelReader(fileName, sheetName,sheet_X,Sheet_Y):
    book = load_workbook(baseDIR + "\\" + fileName)
    sheet = book['Summary Rolling MoM']
    return tuple(sheet['A2':'F13'])