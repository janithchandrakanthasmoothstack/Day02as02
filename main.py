#!usr/bin/env python3

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform
def main():
  totalMonthCount = calculateMonthlyFee()
  print(f'Monthly Fee : {totalMonthCount}')

def calculateMonthlyFee():

    return 0

def calculateFeeLoop(P=800000,R=6,M=10000):
    #init
    newP = P
    interestval = (P* (R/12))/100
    monthCount = 0

    print('Month        P      P  *  (R/12)%      -M          new P')

    while newP>0:
     monthCount = monthCount +1
     interestval = (newP* (R/12))/100
     xp = newP
     if newP>M:
      newP = newP-M+interestval
      print(f'Paying {monthCount}         {xp}       ${interestval}        {M}       {newP} ')
     else:
      newP = newP+interestval
      print(f'Paying {monthCount}         {xp}       ${interestval}        {newP}       0 ')
      newP = 0
    return monthCount

def calculateFee(P=700000,R=6,M=10000,mc=1):
    interestval = (P* (R/12))/100
    newP = P-M+interestval
    print('Month        P      P  *  (R/12)%      -M          new P')
    if (P>0) & (newP>0):
      mo = mc +1
      if newP>M:
        print(f'Paying {mc}         {P}       ${interestval}        {M}       {newP} ')
        calculateFee(newP,R,M,(mo))
      else:
          print(f'Last Payment {mc}         {P}       ${interestval}        {M}       {newP} ')
    return mo

if __name__ == '__main__': main()
