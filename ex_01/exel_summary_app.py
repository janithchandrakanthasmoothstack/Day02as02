import sys
import datetime
from ex_01.myUtils import fileManager
from ex_01.myUtils import myExcelReader
import logging
logging.basicConfig(encoding='utf-8', level=logging.INFO,filename='excel_summary.log')

def main():
    fileName = fileManager.fileSearch();
    logging.debug(f"File Name : {fileName}")
    # print(fileName)
    validateResponse = fileManager.validateFileNames(fileName)
    # print(validateResponse)
    logging.debug(f"validate Response result : {validateResponse}")
    reportMonth = validateResponse[0];reportYear = validateResponse[1];
    if isinstance(validateResponse,list):
        #read Excel File
        t =  myExcelReader.readExcel(fileName,'Summary Rolling MoM','A2','F13')

        for date,calls_offered,abondon,fcr,dsat,csat in filter(lambda c : (c[0].value>=datetime.datetime(reportYear,reportMonth,1)) & (c[0].value<=datetime.datetime(reportYear,reportMonth,31)), t):
            logging.info(f'Calls Offered: {calls_offered.value}')
            logging.info(f'Abandon after 30s :  {abondon.value*100:.2f}:%')
            logging.info(f'FCR: {fcr.value*100:.2f}%')
            logging.info(f'DSAT: {dsat.value*100:.2f}%')
            logging.info(f'CSAT: {csat.value*100:.2f}%')

            print(f'Calls Offered: {calls_offered.value}')
            print(f'Abandon after 30s :  {abondon.value*100:.2f}:%')
            print(f'FCR: {fcr.value*100:.2f}%')
            print(f'DSAT: {dsat.value*100:.2f}%')
            print(f'CSAT: {csat.value*100:.2f}%')
    else:print(validateResponse)

if __name__ == '__main__':main()