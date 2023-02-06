# This is a program to calculate either the interest received on an investment or a home loan repayment, depending on
# the user's need.

import math

calculator = input("Please choose either 'investment' or 'bond' to proceed: \n \nInvestment - to calculate the amount "
                   "of interest you'll earn on your investment \nBond - to calculate the amount you'll have to pay on "
                   "a home loan \n \nI choose: \n")

# This will convert all the letters into lowercase so that whether the user uses capital letters or not, as long as
# the spelling is accurate, 'investment' and 'bond' will be recognised in order to move forward.
calculator = calculator.lower()

# This will show an error message if the user does not input one of the two available options.
while calculator != "investment" and calculator != "bond":
    print("You have not chosen one of the two available options.")

    calculator = input("Please choose investment or bond: \n")

    calculator = calculator.lower()

# The following will calculate the total investment received on a simple or compound interest using if/ else
# statements and using the f string to present the result.
if calculator == "investment":

    deposit = int(input("What is the amount that you are depositing? \n"))
    rate = int(input("Please enter the interest rate as a percentage, using just a number: \n"))
    years = int(input("How many years are you planning on investing? \n"))
    interest = input("Do you want 'simple' or 'compound' interest? \n")

    interest = interest.lower()

    if interest == "simple":
        total_amount = deposit * (1 + (rate / 100) * years)
        total_amount = round(total_amount, 2)

        print(f"The total amount you would receive after {years} years on an interest rate of {rate}% "
              f"would be £{total_amount}.")

    else:
        total_amount = deposit * math.pow((1 + rate / 100), years)
        total_amount = round(total_amount, 2)

        print(f"The total amount you would receive after {years} years on an interest rate of {rate}% "
              f"would be £{total_amount}.")

# The following will calculate the monthly amount the user will have to repay and present the result using the f string.
if calculator == "bond":
    value_of_house = int(input("What is the present value of your house? \n"))
    interest_rate = int(input("What is the interest rate? \n")) / 100 / 12
    number_of_months = int(input("How many months do you plan to take to repay the bond? \n"))
    total_repayment = (interest_rate * value_of_house) / (1 - math.pow(1 + interest_rate, -number_of_months))
    total_repayment = round(total_repayment, 2)

    print(f"The total amount you would have to repay each month is £{total_repayment}.")
