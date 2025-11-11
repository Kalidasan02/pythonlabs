# Base class: Vehicle
class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        # Protected attributes
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        """Return vehicle details as a formatted string."""
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: ₹{self._base_rate:.2f}"

    def rental_charge(self):
        """Placeholder method to be overridden by subclasses."""
        return 0.0


# Subclass: Car
class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        # Initialize the base class
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        """Calculate daily rental charge for a car."""
        return self._base_rate * self.num_seats


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        # Initialize the base class
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        """Calculate daily rental charge for a bike."""
        return self._base_rate * 0.5


# Polymorphic function
def calculate_rental(vehicle):
    """Accepts any Vehicle object and calculates its rental charge."""
    return vehicle.rental_charge()


# --- Main Program Demonstration ---
def main():
    # Create objects
    car1 = Car("CAR001", 100.0, 4)
    bike1 = Bike("BIKE001", 80.0, "Scooter")

    # Display details and calculate charges
    print("----- VEHICLE RENTAL DETAILS -----\n")

    print(car1.display_details())
    print(f"Vehicle Type: Car (Seats: {car1.num_seats})")
    print(f"Daily Rental Charge: ₹{calculate_rental(car1):.2f}\n")

    print(bike1.display_details())
    print(f"Vehicle Type: Bike ({bike1.bike_type})")
    print(f"Daily Rental Charge: ₹{calculate_rental(bike1):.2f}")


# Run the program
main()
