income = int(input("Enter your monthly income: "))

expenses = int(input("Enter your monthly expenses: "))

Monthly_Savings = income - expenses

print(f"Your monthly savings are {Monthly_Savings}")

Projected_Savings = (Monthly_Savings * 12) + (Monthly_Savings * 12 * 0.05)

print(f"Projected savings after one year, with interest, is: {Projected_Savings}")