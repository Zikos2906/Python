def hotel_cost(nights):
    return 140^nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(nights) +  plane_ride_cost(city) + spending_money 
print("cost of car rental : ",rental_car_cost(5))
print("cost of plane ride: ",plane_ride_cost("Los Angeles"))
print("cost of Hotel Room: ",hotel_cost(7))
print("Total cost of trip",trip_cost("Los Angeles",7,500))
    
    
    
    

