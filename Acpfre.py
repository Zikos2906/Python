test_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

value = 10

frequency = list(test_dict.values()).count(value)

print(frequency)