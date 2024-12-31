#Tax Calculator
income = float(input("Enter your annual income in ₹: "))
tax = 0
if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
elif income <= 900000:
    tax = (300000 * 0.05) + (income - 600000) * 0.10
elif income <= 1200000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (income - 900000) * 0.15
elif income <= 1500000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (income - 1200000) * 0.20
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (income - 1500000) * 0.30
print("Your total tax payable under the new tax regime is: ₹", tax)

