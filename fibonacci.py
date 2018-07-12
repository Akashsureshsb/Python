print("Enter a no")
a=input()
def fibonacci(a):
  s=[]
  i=0
  a1=0
  a2=1
  s.append(a1)
  s.append(a2)
  while i<a:
    (a1,a2)=(a2,a1+a2)
    s.append(a2)
    i=i+1 
  print(s)
fibonacci(a)
