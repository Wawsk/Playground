
def hotel_cost(num_nights):
    """Calculates total cost of staying in a hotel depending on
    the number of nights assuming the price per night is £150.
    """
    return num_nights * 150

def plane_cost(city_flight):
    """Calculates total cost for a plane ticket to the chosen city.
    Cost depends on the if statement choice.
    """
    if city_flight == "London":
        return 180
    elif city_flight == "Manchester":
        return 80
    elif city_flight == "Amsterdam":
        return 120
    else:
        raise ValueError(f"{city_flight} not found")

def car_rental(rental_days):
    """Calculates total cost for renting a car for a specific number
    of days assuming the daily cost is £60.
    """
    return rental_days * 60

def holiday_cost(city_flight, num_nights, rental_days):
    """Calculates total cost for the entire trip
    """
    hotel_total = hotel_cost(num_nights)
    plane_total = plane_cost(city_flight)
    car_total = car_rental(rental_days)
    total_cost = hotel_total + plane_total + car_total
    return total_cost

def main():
    """Collects user input to be used in the functions and
    calculates the total cost.
    """
    city_flight = input("""Which city are you flying to?
-London
-Manchester
-Amsterdam
>>> """).capitalize()
    num_nights = int(input("How many nights are you staying?\n>>> "))
    rental_days = int(input("How many days is the car rented for?\n>>> "))
    total_cost = holiday_cost(city_flight, num_nights, rental_days)
    print(f"Total cost of your trip is £{total_cost}")

main()