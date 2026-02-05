class flashcard :
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + " < " + self.meaning + " > "

flash = []
print("Welcome to Flashcard Application")   
while True :
    word = input("Enter the word you want to add : ")
    meaning = input("Enter the meaning you want to add : ")
    flash.append(flashcard(word,meaning))
    choice = int(input("Enter 0 if u want to add a another flashcard"))
    if choice :
        break
print("Your flashcards") 
for i in flash:
    print("--",i)

        
        