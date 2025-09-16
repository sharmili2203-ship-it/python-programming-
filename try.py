try:
    n=int(input("enter a value:"))
    res=50/n
except zeroDivisionError:
    print("it is division by zero error")
else:
    print(res)
finally:
    print("bye")
