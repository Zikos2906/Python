def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

num1 = float(input())
op = input()
num2 = float(input())

if op == "+": print(add(num1, num2))
elif op == "-": print(sub(num1, num2))
elif op == "*": print(mul(num1, num2))
elif op == "/": print(div(num1, num2))