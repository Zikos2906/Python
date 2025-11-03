#Array
import array as arr
a = arr.array('i', [1, 2, 3, 4])
print(a[0])
print(a[1])
b = arr.array('i', [5, 6, 7, 8])
print(b[0])

b.insert(2, 4)
b.insert(3, 9)
b.append(100)
b.append(90)

print(b)

b.reverse()
print(b)