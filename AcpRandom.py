import random
import string


length = 12


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits


all_chars = lowercase + uppercase + digits


password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits)
]


for _ in range(length - 3):
    password.append(random.choice(all_chars))


random.shuffle(password)


final_password = ''.join(password)

print("Generated Password:", final_password)