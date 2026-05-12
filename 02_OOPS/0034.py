''''  
Model a vehicle hierarchy for a ride-sharing app like Ola:

Base class Vehicle with make, model, year, and base_fare_per_km
A method calculate_fare(km) that returns km * base_fare_per_km
A method get_info() that returns a formatted string
Subclass Car(Vehicle) that adds num_seats and overrides get_info()
Subclass Bike(Vehicle) that adds a has_helmet boolean and overrides calculate_fare() to apply a 20% discount
Subclass LuxuryCar(Car) that adds a premium_rate and overrides calculate_fare() to add the premium on top of the base fare
Print the MRO of LuxuryCar and verify the fare calculations for all three vehicle types for a 15km ride
'''