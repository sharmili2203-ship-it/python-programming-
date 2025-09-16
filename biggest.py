def biggest(a,b,c):
    if a>b and a>c:
        return(a)
    elif b>a and b>c:
        return(b)
    else:
        return(c)
x=int(input("enter the x:"))
y=int(input("enter the y:"))
z=int(input("enter the z:"))
big=biggest(x,y,z)
print("the biggest number is :",big)
