class myclass :
    __privateVar = 28
    def __privmath(self):
        print("I am inside my class.")
    def hello(self):
        print("Value of private varible",myclass.__privateVar)
obj = myclass()
obj.hello()
obj.__privmath()