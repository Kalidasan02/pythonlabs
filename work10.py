from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Base Class
class User(ABC):
    def __init__(self, name, joining_year):
        self._name = name
        self._joining_year = joining_year

    def years_on_platform(self):
        """Calculate how many years the user has been on the platform."""
        current_year = 2025  # As per the problem statement
        return current_year - self._joining_year

    @abstractmethod
    def show_role(self):
        """Abstract method to define user role."""
        pass

    def __str__(self):
        """Return a user-friendly message (will be customized in subclasses)."""
        return f"{self._name} has been on the platform for {self.years_on_platform()} years."


# Subclass: Customer
class Customer(User):
    def show_role(self):
        return "Customer"

    def __str__(self):
        """Special print message for Customer."""
        return f"Name: {self._name}, Role: {self.show_role()}, Years on Platform: {self.years_on_platform()}"


# Subclass: Vendor
class Vendor(User):
    def show_role(self):
        return "Vendor"

    def __str__(self):
        """Special print message for Vendor."""
        return f"Name: {self._name}, Role: {self.show_role()}, Years on Platform: {self.years_on_platform()}"


# --- Main Program ---
def main():
    # Create Customer and Vendor objects
    customer1 = Customer("Ravi", 2020)
    vendor1 = Vendor("Anjali", 2018)

    # Display user info
    print("----- USER ACCOUNT DETAILS -----\n")
    print(customer1)
    print(vendor1)


# Run the program
main()
