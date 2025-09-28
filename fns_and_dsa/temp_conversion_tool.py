FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#User Interaction

temperature = float(input("Enter the temperature to convert: "))
temp_choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if temp_choice == "F":
   print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
else:
   print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")

    