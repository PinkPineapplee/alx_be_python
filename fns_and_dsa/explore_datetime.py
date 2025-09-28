from datetime import datetime, timedelta

def display_current_datetime():
    """Returns the current date and time as a datetime object"""
    current_date = datetime.now()
    return current_date  # Return datetime object, not string

def calculate_future_date(current_date, number_of_days):
    """Calculate and display future date"""
    future_date = current_date + timedelta(days=number_of_days)
    
    # Format both dates for display
    current_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    future_formatted = future_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {current_formatted}")
    print(f"Enter the number of days to add to the current date: {number_of_days}")
    print(f"Future date: {future_formatted}")

def main():
    """Main function to run the program"""
    # Get current date
    current_date = display_current_datetime()
    
    try:
        # Get user input - INSIDE the main function
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate and display future date
        calculate_future_date(current_date, number_of_days)
        
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Run the program
if __name__ == "__main__":
    main()