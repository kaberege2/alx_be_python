import datetime
from datetime import timedelta

current_date = datetime.datetime.now()
formatted_date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")

def display_current_datetime():
    print(f"Current date and time: {formatted_date_time}")

display_current_datetime()


number_of_days = int(input("Enter the number of days to add to the current date: "))

future_date = current_date + timedelta(days=number_of_days)

def calculate_future_date():
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()