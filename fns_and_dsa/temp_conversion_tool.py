FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#temp_to_convert = float(input("Enter the temperature to convert: "))
#temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

def convert_to_celsius(fahrenheit):
    temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    #print(f"{fahrenheit}°F is {temperature}°C")
    return temperature

def convert_to_fahrenheit(celsius):
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    #print(f"{celsius}°C is {temperature}°F")
    return temperature

try:
    temp_to_convert = float(input("Enter the temperature to convert: "))
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if temp_type == "c":
        temp_value =  convert_to_fahrenheit(temp_to_convert)
        print(f"{temp_to_convert}°C is {temp_value}°F")
    elif temp_type == "f":
        temp_value = convert_to_celsius(temp_to_convert)
        print(f"{temp_to_convert}°F is {temp_value}°C")
    else:
        raise ValueError("Invalid temperature type. Please enter 'C' or 'F'.")
except ValueError as e:
    print(e)
except:
    print(f"Invalid input. Please enter a numeric value.")
