# tripdata.py

def get_trip(city, date, comment):
    """
    Returns a dictionary containing trip details.
    city: string
    date: string in dd-mm-yyyy format
    comment: string
    """
    return {
        "city": city,
        "date": date,
        "comment": comment
    }
