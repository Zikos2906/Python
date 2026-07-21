class india():
    def capital(self):
        print("New Dehil is the capital of India")
    def language(self):
        print("Hindi is the most spoken language in India")
    def type(self):
        print("INDIA IS A DEVELOPING COUNTRY")
class spain():
    def capital(self):
        print("Madrid is the capital of spain")
    def language(self):
        print("Spainish is the most spoken language in India")
    def type(self):
        print("Spain is a first world country")
obj = india()
obj1 = spain()

for i in (obj,obj1):
    i.capital()
    i.language()
    i.type()
