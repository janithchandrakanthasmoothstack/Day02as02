import sys

import datetime
from openpyxl import load_workbook
import logging
from ex_01.myUtils import fileManager,myExcelReader
from ex_01.myUtils.myExcelReader import readExcel, getCustomResult

import logging
logging.basicConfig(encoding='utf-8', level=logging.INFO)

def main():

    fileName = fileManager.fileSearch();
    validateResponse = fileManager.validateFileNames(fileName)
    reportMonth = validateResponse[0];reportYear = validateResponse[1];
    if isinstance(validateResponse,list):
        #read Excel File
        t = myExcelReader.readExcel(fileName, 'VOC Rolling MoM', 'B1', 'J1')
       #for rowOfCellObjects in t:
        for cellObj in filter(lambda d:(d.value>=datetime.datetime(reportYear,reportMonth,1)) &
                                       (d.value<=datetime.datetime(reportYear,reportMonth,31)),t[0]):
            # print(cellObj.coordinate[0])
            r = readExcel(fileName, 'VOC Rolling MoM', f'{cellObj.coordinate[0]}5', f'{cellObj.coordinate[0]}10')
            p = getCustomResult(fileName,'VOC Rolling MoM','B1','J1')

            summary = []
            for title,value in filter(lambda x: x[0]!=None,p):
                print(f"{title} > {value}")
                if title.startswith('Promoters'):
                    summary.append(('Promoters', value,(lambda value:"good Promoters" if (value>200) else "bad" )(value)))
                if title.startswith('Passives'):
                    summary.append(('Passives', value,(lambda value:"good Passives" if (value>100) else "bad" )(value)))
                if title.startswith('Dectractors'):
                    summary.append(('Dectractors', value,(lambda value:"good Decrators" if (value>100) else "bad" )(value)))

            # print("In Net Promoter Score : ",end=" ")
            # print(f'{summary[0][0]} {summary[0][2]} ({summary[0][1]})')
            # print(f'                         {summary[1][0]} {summary[1][2]} ({summary[1][1]})')
            # print(f'                         {summary[2][0]} {summary[2][2]} ({summary[2][1]})')

            logging.info("In Net Promoter Score : ")
            logging.info(f'{summary[0][0]} {summary[0][2]} ({summary[0][1]})')
            logging.info(f'{summary[1][0]} {summary[1][2]} ({summary[1][1]})')
            logging.info(f'{summary[2][0]} {summary[2][2]} ({summary[2][1]})')



    else:print(validateResponse)
if __name__ == '__main__':main()