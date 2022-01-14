import sys
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
        elif fileParts[4]>1900:
            return "Incorrect File Name: Fifth part, incorrect Year Found"
        else: return "ok"
    except:return "Incorrect File Name Found !, format should be : expedia_report_monthly_january_2018.xlsx"

def main():
    fileName = input("File Name Please: ")
    # fileName = 'expedia_report_monthly_january_20x8.xlsx'
    validateResponse = fileNameValidator(fileName)
    print(validateResponse)
if __name__ == '__main__':main()
