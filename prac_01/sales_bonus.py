"""
CP1404 Practical 1 - Sales Bonus
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = (sales / 100) * 10
        print("Your bonus is: ${:.2f}".format(bonus))
    else:
        bonus = (sales / 100) * 15
        print("Your bonus is: ${:.2f}".format(bonus))
    sales = float(input("Enter sales: $"))
