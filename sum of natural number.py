def naturalnumsum(n):
  if n<=1 :
      return n
  else:
      return  (n) + naturalnumsum(n-1)
n = int(input("enter a number here:"))
  
if n <= 0:
    print("enter a positive number")
else:
  print("the sum of natural number upto given number is", naturalnumsum(n))