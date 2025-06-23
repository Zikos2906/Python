# age = 10

# if age>=18 :
#     print("You are eligible to vote")

# else:
#     print("You are not eligible")


# number = 2

# if number % 2 == 0:
#     print("Even number")
# else :
#     print("Odd number")
    

number_of_apple = int(input("Enter total number of apples: "))
selling_price = int(input("Selling price for each apple:"))
buying_price = int(input("buying price for each apple:"))

total_selling_price = number_of_apple*selling_price
total_buying_price = number_of_apple*buying_price

if total_selling_price > total_buying_price:
    print(f"profit{total_selling_price-total_buying_price}ruppes")
else:
    print(f"Loss of {total_buying_price-total_selling_price}Ruppes")