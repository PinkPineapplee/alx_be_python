monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
simple_annual_interest_rate = 0.05

#calculate projected savings after one year
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Enter your monthly income: {monthly_income}" )
print(f"Enter your total monthly expenses: {monthly_expenses}")
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")