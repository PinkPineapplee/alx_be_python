pattern = int(input("Enter the size of the pattern: "))

count = 0    
while count < pattern:
     # Reset count for each row
    for square in range(pattern):
        print("*", end="")
        
    print()  # Add newline after each row
    count += 1  # Increment count to avoid infinite loop 
 
   
          