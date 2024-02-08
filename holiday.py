"""Task 14 - Programming with User-defined Functions

This program allows to calculate the total holiday cost,
which includes the flight cost, hotel cost, and car-rental cost.
The list of the cities can be changed easily
as well as the hotel and flight prices.
"""

def input_num(prompt, min_value):
    """Prompt the user to enter a number which is greater
    or equal to the minimum value and validate the input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            print(f"Please enter {min_value} or greater number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def hotel_cost(num_nights, city_flight, hotel_price):
    """Calculate a total cost at a hotel
    for a user input number of nights.
    """
    total_hotel_cost = hotel_price[city_flight] * num_nights
    return total_hotel_cost

def plane_cost(city_flight, flight_price):
    """Return a flight cost to a user input city."""
    return flight_price[city_flight]

def car_rental(rental_days):
    """Calculate a total car-rental cost
    for a user input number of days.
    """
    total_car_rental = 35 * rental_days
    return total_car_rental

def holiday_cost(hotel_cost, plane_cost, car_rental):
    """Calculate a total cost of the holiday."""
    total_holiday_cost = hotel_cost + plane_cost + car_rental
    return total_holiday_cost

cities = ["Paris", "Amsterdam", "London", "Rome", "Vienna"]

hotel_price = {
"Paris": 120,
"Amsterdam": 115,
"London": 140,
"Rome": 155,
"Vienna": 135
}

flight_price = {
"Paris": 190,
"Amsterdam": 150,
"London": 110,
"Rome": 205,
"Vienna": 165
}

print("-" * 55)
print("The list of the cities you can fly to:")
print("-" * 55)
for city in cities:
    print(city)
print("-" * 55)

# Request a city from the user and validate it.
while True:
    city_flight = input("Please enter the city from the list above: ")
    city_flight = city_flight.capitalize().strip()
    if city_flight in cities:
        break
    print("There is no such city in the list, try again.")
    continue

# The number of nights at a hotel must be greater or equal to 1.
num_nights = input_num("Please enter a number of nights at a hotel: ", 1)

# The number of days to rent a car must be greater or equal to 0.
rental_days = input_num("Please enter a number of days for hiring a car: ", 0)

hotel_cost = hotel_cost(num_nights, city_flight, hotel_price)
plane_cost = plane_cost(city_flight, flight_price)
car_rental = car_rental(rental_days)
holiday_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

print("-" * 55)
print(f"City of travelling:           {city_flight}")
print(f"Cost for the flight:          £{plane_cost}")
print(f"Number of nights at a hotel:  {num_nights}")
print(f"Total cost of the hotel stay: £{hotel_cost}")
print(f"Number of days to rent a car: {rental_days}")
print(f"Total cost of the car rental: £{car_rental}")
print("-" * 55)
print(f"Total cost of the holiday:    £{holiday_cost}")
print("-" * 55)
