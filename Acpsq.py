start = int(input())
end = int(input())

squares = [x*x for x in range(start, end + 1)]
even_squares = [x for x in squares if x % 2 == 0]
odd_squares = [x for x in squares if x % 2 != 0]

print(squares)
print(even_squares)
print(odd_squares)






