class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling price ",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price
obj = computer()
obj.sell()
obj.setmaxprice(1000)
obj.sell()