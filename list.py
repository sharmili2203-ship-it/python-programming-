lst=[]
print(lst)
n=int(input("enter the no.of element to be inserted:"))
for i in range(0,n):
      m=int(input("enter a number:"))
      lst.append(m)
print(lst)
print(lst[0])
print(lst[-1])
print(lst[2])
print(lst[-3:])
print(lst[2:5])
a=lst.extend([100,95,86])
print(a)
