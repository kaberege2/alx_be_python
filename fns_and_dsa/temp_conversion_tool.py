
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp_to_convert = float(input("Enter the temperature to convert: "))

temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

def convert_to_celsius(fahrenheit):
    temperature = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{fahrenheit}°F is {temperature}°C")

def convert_to_fahrenheit(celsius):
    temperature =  CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    print(f"{celsius}°C is {temperature}°F")


if temp_type == "c":
    convert_to_fahrenheit(temp_to_convert)
elif temp_type == "f":
    convert_to_celsius(temp_to_convert)
else:
    print("Invalid temperature. Please enter a numeric value.")