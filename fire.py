import random

fire_size = 10

while fire_size > 0:
    flicker = random.randint(-2, 2)
    fire_size += flicker
    
    if fire_size > 15:
        fire_size = 15
        
    print("Fire intensity:" + "*" * fire_size)
    
    if fire_size < 3:
        print("Fire is dying out!")
        break