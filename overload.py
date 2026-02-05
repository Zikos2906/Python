class a :
    def __init__(self,x):
        self.x = x
    def __lt__(self,y):
        if (self.x) < (y.x):
            return "ob1 < ob2"
        else:
            return "ob2 < ob1"
    def __eq__(self,y):
        if (self.x==y.x):
            return "both are equal"
        else:
            return "not equal"

obj1 = a(20)
obj2 = a(16)
print("Passed values",obj1.x,obj2.x)
print(obj1<obj2)


obj3 = a(20)
obj4 = a(20)
print("Passed values",obj3.x,obj4.x)
print(obj3==obj4)