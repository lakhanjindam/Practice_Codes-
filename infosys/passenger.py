#PF-Assgn-29
def calculate(distance,no_of_passengers):
    price_per_litre = 70
    mileage_fuel = 10
    price_per_ticket= 80
    
    total_amount_recieved = no_of_passengers*price_per_ticket
    fuel_req = distance/mileage_fuel
    fuel_price = fuel_req*price_per_litre
    
    if(fuel_price<total_amount_recieved):
        return total_amount_recieved - fuel_price
        
    else:
        return -1
        


#Provide different values for distance, no_of_passenger and test your program
distance=200
no_of_passengers=10
print(calculate(distance,no_of_passengers))