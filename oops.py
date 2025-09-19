class stud:
    def __init__(self, a,b,c):
        self.sno=a
        self.name=b
        self.age=c
        self.mark=m1
        self.mark=m2
        self.mark=m3
        self.tot=total
        self.avg=average
        self.res=result
    def calculate(self):
        self.tot=self.mark1+self.mark2+self.mark3
        self.avg=self.tot/3
        
        if m1>40 and m2>40 and m3>40:
            self.result="pass"

        else:
            self.result="fail"

    def disp(self):
         print( "student no:",self.sno)
         print(" student name :",self.name)
         print("student age:",self.age)
         print("mark1=",self.mark1)
         print("mark2=",self.mark2)
         print("mark3=",self.mark3)
         print("total=",self.tot)
         print("average=",self.avg)
         print("result=",self.result)

x=int(input("enter rollno:"))
y=input("enter name:")
z=int(input("enter age:"))
m1=int(input("enter m1:"))
m2=int(input("enter m2:"))
m3=int(input("enter m3:"))



obj=stud(x,y,z,m1,m2,m3,total,average,result)
obj.calculate()
obj.display()
