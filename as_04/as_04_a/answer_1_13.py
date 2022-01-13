
#answer 01
def func():
    print('Hello Word')

#answer 02
def func1(name):
    print(f'Hi My name is {name}')

#answer 03
def func3(x,y,z):
    if z==True:
        return x
    else: return y

#answer 04
def func4(x,y):
    return x*y

#answer 05
def is_even(input):
    if (input%2==0) :
        return False
    else:
        return True
#print(is_even(2))

#answer 06
def func6(input1,input2):
    if (input1>input2) :
        return True
    else:
        return False
# print(func6(4,4))

#answer 07
def func7(numberArray):
 total = 0
 for x in numberArray:
    total+=x
 return total
#print(func7([4,34,345,43,4]))


#answer 08
def func8(numberArray):
 even = []
 for x in numberArray:
    if (x%2)==0:
        even.append(x)
 return even
# print(func8([4,34,345,43,4]))

#answer 09
# ???

#answer 10
def func10(input1,input2):
    if input1%2==0 and input2%2==0:
        if(input1>input2):return input2;
        else:return input1;
    elif (input1%2!=0) or (input2%2!=0):
        if (input1 > input2):
            return input1
        else:
            return input2
# print(f'val : {func10(13,15)}')


#answer 11
def func11(text1,text2):
    if text1[0] == text2[0]:
        return True
    else:
        return False

#answer 12
def func12(input):
    return (7-(input*2))

#answer 13
def func13(input):

    try:
        input = input[:2] + input[2].upper() + input[3:]
        input = input[:4] + input[4].upper() + input[5:]
    except:
        print("Incorrect Input")
    return input
# print(func13('Janith'))