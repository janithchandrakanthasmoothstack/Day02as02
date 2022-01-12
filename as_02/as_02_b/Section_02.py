
def main():
   print(factorialNumber(4))

def factorialNumber(input):

    if input == 1:
        return 1
    elif input < 1:
        return "Incorrect Input found !"
    else:
        return (input * factorialNumber(input-1))


if __name__ == '__main__': main()
