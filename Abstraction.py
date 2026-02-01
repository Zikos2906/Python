from abc import ABC
class name(ABC):
    def print(self,x):
        print("Passed value",x)
    def task(self):
        print("Bihan")
class name2(name):
    def task(self):
        print("We are inside the child class")
objname = name2()
objname.print(45)
objname.task()