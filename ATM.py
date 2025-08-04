print("Welcome to ATM")
global balance
balance = 1000

def Add(amount):
    global balance
    balance = balance + amount
    print("Successfully Deposited")
    print("Current Balance ", balance)

def Withdraw(amount):
    global balance
    balance = balance - amount
    print("Successfully withdrawn")
    print("Current Balance ", balance)

def Check():
    global balance
    print(balance)

Add(20000)
Add(4000)
Withdraw(3000)
Check()