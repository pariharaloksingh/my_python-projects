num = int(input ( "enter your number he:"))

if num == 1:\
    print("it is not a prime number")
    
if num > 1:
    for i in range (2,num):
     if num % i == 0:
      print("its is not a prime number")
    else:
     print("given number is a prime number")            