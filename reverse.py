class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        return " ".join(self.text.split()[::-1])


obj = StringReverser("Bihan Banerjee")
print(obj.reverse_words())