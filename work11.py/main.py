# main.py

from tripdata import get_trip
from datetime import datetime
import json

# Step 1: Create a list to store trip dictionaries
trips = []

# Step 2: Add trip entries using the imported function
trips.append(get_trip("Paris", "15-05-2023", "Beautiful city with amazing food"))
trips.append(get_trip("Tokyo", "10-12-2022", "Loved the culture and technology"))
trips.append(get_trip("New York", "25-07-2021", "The city that never sleeps"))

# Step 3: Convert date strings into formatted date objects
for trip in trips:
    # Convert dd-mm-yyyy string → datetime object
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    
    # Format the date to "Month Day, Year"
    formatted_date = date_obj.strftime("%B %d, %Y")
    
    trip["date"] = formatted_date  # Replace the original date string

# Step 4: Convert entire list to JSON string
json_output = json.dumps(trips, indent=4)

# Step 5: Print JSON string
print(json_output)
