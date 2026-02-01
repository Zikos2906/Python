class india():
    def capital(self):
        print("New Dehil is the capital of India")
    def langauge(self):
        print("Hindi is the most spoken langauge in India")
    def type(self):
        print("INDIA IS A DEVELOPING COUNTRY")
class spain():
    def capital(self):
        print("Madrid is the capital of spain")
    def langauge(self):
        print("Spainish is the most spoken langauge in India")
    def type(self):
        print("Spain is a first world country")
obj = india()
obj1 = spain()

for i in (obj,obj1):
    i.capital()
    i.langauge()
    i.type()
