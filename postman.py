code = input("Scan City Code (BLR/CH): ").upper()

if code == "BLR":
    print("City: Bangalore. Delivering to the Blue Mail Truck.")
elif code == "CH":
    print("City: Chennai. Delivering to the Red Mail Truck.")
else:
    print("Invalid code. Returning to post office.")