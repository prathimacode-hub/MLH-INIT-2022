# Program functions as an investment calculator and a home loan calculator

import math


#######  TOP MENU  #######
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("")
print("investment      - to calculate the amount of interest you'll earn on investment")
print("bond            - to calculate the amount you'll have to pay on a home loan")

menu_input = input("\n")
print("")


#######  Investment  #######
if(menu_input.lower() == "investment"):

    # user input
    principal = float(input("Enter amount of money to deposit: "))
    rate      = float(input("Enter interest rate (numerical value only): "))
    time      = float(input("Enter number of years to invest: "))
    interest  = input("Choose interest type: \"simple\" or \"compound\": ")

    rate      /= 100  # convert to decimal rate
    interest  = interest.lower()

    ## case: simple interest
    if interest == "simple":
        amt = principal * (1 + rate * time)

    ## case: compound interest
    if interest == "compound":
        amt = principal * math.pow((1 + rate), time)

    ## print result
    print("")
    print(f"The total amount after ${principal} is invested for {time} years "
          f"with {rate * 100}% {interest} interest is ${round(amt,2)}.")


                      
#######  Bond  #######
elif(menu_input.lower() == "bond"):

    # user input
    value    = float(input("Enter the present value of the house: "))
    ann_rate = float(input("Enter the annual interest rate (numerical value only): "))
    num_months = int(input("Enter the number of months to repay the bond: "))

    # calcalate bond repayment
    # x = (i*P)/(1 - (1+i)^(-n)) 
    monthly_rate = ann_rate / 1200   # convert to decimal monthly rate
    monthly_amount = (monthly_rate * value) / (1 - math.pow((1 + monthly_rate), -1 * num_months))

    
    # print result             
    print("")
    print(f"For a house valued at ${value} with an annual interest rate of {ann_rate}%, "
          f"you will need to pay ${round(monthly_amount,2)} "
          f"each month for {num_months} months to repay the bond.")

    

#######  Bad input  #######
else:
    print("Error: invalid input")
