# a = input("enter a word here:")

# rev = a [: :-1]

# if a == rev:
#     print("it is palindrom")
# else:
#     print("it is not palindrom")
    
# mericrush="wow"

# ans=True

# for i in range(int(len(mericrush)/2)):
#     if(mericrush[i]!=mericrush[len(mericrush)-i-1]):
#         ans=False
#         break

# print(ans)

memory={}

def fib(n):
    if n==0:
        return 0;
    if n==1:
        return 1;
    if n in memory:
        return memory[n]
    memory[n]=fib(n-1)+fib(n-2)
    return memory[n]

print(fib(40))


teriCrush="ananya" 
meriCrush="aaanny" 
ll= sorted(teriCrush)
yy=sorted(meriCrush)

if ll == yy:
    print('anagram hai ye ')
else:
    print('nahi ha loda')
    
