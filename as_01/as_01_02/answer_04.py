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
