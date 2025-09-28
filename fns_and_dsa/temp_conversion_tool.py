FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    # User Interaction
    try:
        temperature = float(input("Enter the temperature to convert: "))  # Use float, not int
        temp_choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()  # Add ()
        
        if temp_choice == "F":
            converted_temp = convert_to_celsius(temperature)  # Pass temperature argument
            print(f"{temperature}°F is {converted_temp:.2f}°C")  # Correct order
        elif temp_choice == "C":  # Use elif for better logic
            converted_temp = convert_to_fahrenheit(temperature)  # Pass temperature argument
            print(f"{temperature}°C is {converted_temp:.2f}°F")  # Correct order
        else:
            print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        print("Please enter a valid number for temperature.")

if __name__ == "__main__":
    main()