nums = list(range(1, 21))

squares = [x*x for x in nums]
evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]
even_squares = [x*x for x in nums if x % 2 == 0]
div_by_3_5 = [x for x in nums if x % 3 == 0 and x % 5 == 0]

words = ["python", "list", "comprehension", "practice"]
lengths = [len(w) for w in words]
upper_words = [w.upper() for w in words]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]

print(squares)
print(evens)
print(odds)
print(even_squares)
print(div_by_3_5)
print(lengths)
print(upper_words)
print(flat)