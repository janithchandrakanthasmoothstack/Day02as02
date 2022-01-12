x = range(2000,3200+1)

for n in x:
  if((n%7)==0) and ((n%5)!=0):
    print(n,end=",")