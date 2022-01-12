import sys

def main():
    #input number
   text = int(input("Input Number : "))
   print(factorialNumber(text))
def factorialNumber(input):
    if input == 1:
        return 1
    elif input < 1:
        return "Incorrect Input found !"
    else:
        return (input * factorialNumber(input-1))

main()
