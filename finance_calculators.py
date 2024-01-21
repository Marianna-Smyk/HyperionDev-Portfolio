import math

print("""----------------------------------- Welcome! -----------------------------------
This program allows you to access two different financial calculators:
an investment calculator and a home loan repayment calculator.""")

print("--------------------------------------------------------------------------------")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("--------------------------------------------------------------------------------")
calc_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if calc_type == "investment":
    deposit = float(input("What is the amount of money you are depositing (£)? "))
    interest_rate = float(input("What is your interest rate (%)? "))
    years = float(input("What is the number of years you plan on investing? "))
    interest = input("Enter either 'simple' or 'compound' interest to proceed: ").lower()

    P = deposit
    t = years
    r = interest_rate / 100

    if interest == "simple":                    # investment with simple interest
        A = round(P * (1 + r*t), 2)
    elif interest == "compound":                # investment with compound interest
        A = round(P * math.pow((1 + r),t), 2)   # A = round(P * (1 + r) ** t, 2)
    else:
        print("Sorry, you entered wrong type of interest(")

    if (interest == 'simple') or (interest == 'compound'):
        print("--------------------------------------------------------------------------------")
        print(f"Calculator type:  {calc_type}")
        print(f"Interest type:    {interest}")
        print(f"Amount of money:  £{deposit}")
        print(f"Interest rate:    {interest_rate}%")
        print(f"Number of years:  {years}")
        print(f"Total amount:     £{A}")
        print("--------------------------------------------------------------------------------")

elif calc_type == "bond":
    house_value = float(input("What is the present value of your house (£)? "))
    interest_rate = float(input("What is your interest rate (%)? "))
    months = float(input("What is the number of months you plan to take to repay the bond? "))

    P = house_value
    n = months
    r = interest_rate / 100
    i = r / 12 # monthly interest rate

    # repayment = round((i * P)/(1 - math.pow((1 + i),-n)), 2)
    repayment = round((i * P)/(1 - (1 + i)**(-n)), 2)

    print("--------------------------------------------------------------------------------")
    print(f"Calculator type:                         {calc_type}")
    print(f"Present value of the house:              £{house_value}")
    print(f"Interest rate:                           {interest_rate}%")
    print(f"Number of months:                        {months}")
    print(f"Amount to pay on a home loan each month: £{repayment}")
    print("--------------------------------------------------------------------------------")

else:
    print("Sorry, you entered wrong type of calculator(")
