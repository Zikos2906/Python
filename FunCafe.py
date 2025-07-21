from colorama import Fore , Style , init
init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "------Welcome to Fun Cafe------")

items = ["Coffee","Pizza","Crossaint","Cookie"]
price = [10,25,15,20]

for i in range (4):
    print(f"{Fore.GREEN} {items[i]} - {price[i]}")

total_cost = 0
order = []

print(f"{Fore.YELLOW} Type 'Done' after you are done")

while True:
    choice = input(">").title()

    if choice == "Done":
        break

    if choice in items: 
        item_index = items.index(choice)
        item_price = price[item_index]
        total_cost = total_cost+item_price
        order.append(choice)
    else:
        print(f"{Fore.RED} Sorry! We do not Have that")

    print(f"{Fore.CYAN}-----Your Bill-----")
    print(f"{Fore.BLUE}{order}")
    print(f"{Fore.GREEN} {total_cost}")

 
