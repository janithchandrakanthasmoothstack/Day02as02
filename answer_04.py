#!usr/bin/env python3
# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform

def main():
  rental = monthlyCal()
  print('!!!!!!!!!!!!!!Final Answer !!!!!!!!!!!')
  print(f'Monthly Rental >>> {rental:.0f}')
  print('=====================================')

def monthlyCal(P=800000,R=6,N=103):
      #formula >   M = P [(1+r)^n]/[(1+r)^n - 1]]
      #interest rate
      r = (R/100)/12
      print(f'interest : {r}')
      # if k = (1+r)^n
      K = pow((1+r),N)
      print(f'k : {K}')
      M = P *((r*K)/(K-1))
      return M  #month count

# def calculateFeeLoop(P=800000,R=6,M=10000):
#     #init
#     newP = P
#     interestval = (P* (R/12))/100
#     monthCount = 0
#     interest = 0
#     print('Month        P      P  *  (R/12)%      -M          new P')
#
#     while newP>0:
#      monthCount = monthCount +1
#      interestval = (newP* (R/12))/100
#      interest = interest + interestval
#      xp = newP
#      if newP>M:
#       newP = newP-M+interestval
#       print(f'Paying {monthCount}         {xp:.2f}       ${interestval:.2f}        {M}       {newP:.2f} ')
#      else:
#       newP = newP+interestval
#       print(f'Paying {monthCount}         {xp:.2f}       ${interestval:.2f}        {newP:.2f}       0 ')
#       newP = 0
#     print(f'interest val : {interest:.2f}...total {(P+interest):.2f} ... monthly total: {((P+interest)/103):.2f} ')
#     return ((P+interest)/103)
#
# def calculateFee(P=700000,R=6,M=10000,mc=1):
#     interestval = (P* (R/12))/100
#     newP = P-M+interestval
#     print('Month        P      P  *  (R/12)%      -M          new P')
#     if (P>0) & (newP>0):
#       mo = mc +1
#       if newP>M:
#         print(f'Paying {mc}         {P}       ${interestval}        {M}       {newP} ')
#         calculateFee(newP,R,M,(mo))
#       else:
#           print(f'Last Payment {mc}         {P}       ${interestval}        {M}       {newP} ')
#     return mo
# if __name__ == '__main__': main()