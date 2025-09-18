weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Convert input to lowercase for comparison
weather = weather.lower()

if weather == "sunny":
  print("Wear a t-shirt and sunglasses. ")
elif weather == "rainy":
  print("Don't forget your unbrella and a raincoat. ")
elif weather == "cold":
  print("Make sure to wear a warm coat and a scarf. ")
else:
  print("Sorry, I don't have a recommendations for this weather. ")    
