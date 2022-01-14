import sys
import datetime
from openpyxl import load_workbook
import logging
from ex_01.myUtils import validator,excelReader


def main():
    fileName = input("File Name Please: ")
    # fileName = 'expedia_report_monthly_january_20x8.xlsx'
    validateResponse = validator.fileNameValidator(fileName)
    reportMonth = validateResponse[0];reportYear = validateResponse[1];
    if isinstance(validateResponse,list):
        #read Excel File
        t = excelReader(fileName,'VOC Rolling MoM','A2','F13')

        for date,calls_offered,abondon,fcr,dsat,csat in filter(lambda c : (c[0].value>=datetime.datetime(reportYear,reportMonth,1)) & (c[0].value<=datetime.datetime(reportYear,reportMonth,31)), t):
            print(f'Calls Offered: {calls_offered.value}')
            print(f'Abandon after 30s :  {abondon.value*100:.2f}:%')
            print(f'FCR: {fcr.value*100:.2f}%')
            print(f'DSAT: {dsat.value*100:.2f}%')
            print(f'CSAT: {csat.value*100:.2f}%')
    else:print(validateResponse)

if __name__ == '__main__':main()