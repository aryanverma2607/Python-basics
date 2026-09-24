class student:
    def hello(self):
        print("Hello guy")
s1=student()
s1.hello()

class company:
    def set(self,name,age):
        self.name=name
        self.age=age
    def display(self):    #self can be anything
        print("Data of student is:",self.name,"and",self.age)

s1=company()
s1.set("Aryan",21)
s1.display()

class sum:
    def add(x,a,b):
        x.a=a
        x.b=b
        x.c=x.a*x.b
    def display(self):
        print(self.c)
z=sum()
z.add(4,5)
z.display()

class multi:
    def accept(self,a,b):
        self.a=a
        self.b=b
    def op(self):
        self.c=self.a*self.b
    def show(self):
        return self.c
x=multi()
x.accept(10,9)
x.op()
print(x.show())