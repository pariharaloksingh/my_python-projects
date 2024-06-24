mass1= float(input("enter the weight of 1st body"))
mass2=float(input("enter the weight of 2nd body"))

r=float(input("enter the distance between two body"))

G = 6.67*(10**-11)

force = (G*mass1*mass2)/r**2

print(force)