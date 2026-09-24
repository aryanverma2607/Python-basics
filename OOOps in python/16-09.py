'''class company:
    def __init__(self):
        self.name="Aryan"
        self.age=32
        print("Default Constructor")
c=company()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Parameter Constructor",id(self.name),id(self),self.age)
s=student("Muskiii",21)
print(id(s))

'''
class Counter:
    def __init__(self):
        self.count=0
    def inc(self):
        self.count+=1
    def dec(self):
        self.count-=1
    def getcount(self):
        return self.count
c1=Counter()
print(c1.getcount())
c1.inc()
c1.inc()
c1.inc()
c1.inc()
c1.dec()
print(c1.getcount())




