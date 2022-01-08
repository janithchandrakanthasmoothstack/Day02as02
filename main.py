#!usr/bin/env python3

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform
def main():
  calculateFee()
monthCount = 1
def calculateFee(P=800000,R=6,M=10000,mc=1):
    interestval = (P* (R/12))/100
    newP = P-M+interestval
    print('Month        P      P  *  (R/12)%      -M          new P')
    print(f'{mc}         {P}       ${interestval}        {M}       {newP} ')
    if P>0 :
      mo = mc +1
      calculateFee(newP,R,M,(mo))


if __name__ == '__main__': main()
