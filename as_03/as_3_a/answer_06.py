import sys



userIn = input("Input Word : ")
finalWord=[]
index = len(userIn)
while index > 0:
    print(userIn[index - 1],end="")
    index = index - 1
