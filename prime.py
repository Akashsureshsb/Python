
print("Enter  a number")
n=input()
def primegen(a):
  b=[]
  flag=0
  for i in range (1,a):
    flag=0
    for j in range(1,i):
      if (i%j) == 0:
        flag=flag+1
    if flag<2:
      b.append(i)
  print(b)   
primegen(n) 
