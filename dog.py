class Dog:
    species = "Dog"   

    def __init__(self, breed, age):
        self.breed = breed      
        self.age = age          

    def show_details(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age)
        print()



dog1 = Dog("German Shepherd", 5)
dog2 = Dog("Golden Retriever", 3)


dog1.show_details()
dog2.show_details()