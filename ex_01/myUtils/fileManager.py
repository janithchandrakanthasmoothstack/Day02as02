from os import listdir
from os.path import isfile, join
baseDIR = ("E:\learn\problem_01")

def fileSearch():
    correctFile = ""
    for fileName in [f for f in listdir(baseDIR) if isfile(join(baseDIR, f))]:
        #print(validateFileNames(fileName))
        if isinstance(validateFileNames(fileName),list):
            correctFile = fileName
    return correctFile

def validateFileNames(fileName):
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
        else: return [monthlist.index(fileParts[3])+1,int(fileParts[4].split(".")[0])]
    except OSError as err:return "Incorrect File Name Found: {0}".format(err)

# print(f'correct file > {fileSearch()}')