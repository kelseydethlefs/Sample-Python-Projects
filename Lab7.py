# Lab7.py
# calculates the amount of taxes that people pay and keeps that list.

total_tax = 0    #sets the sum for total tax amount

name = input("Please enter your name here. ")
income = int(input ("How much do you make per year? "))

while income >= 0:
    if income <=15000:
        print ("Tax rate = 2%")
        tax = income * .02      #calculates tax
        income = income - tax   #calculates new income
        print ("Tax deducted = ", tax)
        print ("Total income = ", income)
        total_tax = total_tax + tax    #adds the amount to the total tax
        print (":::" * 15)       #creates a spacer between people
        name = input("Please enter your name here. ")
        income = int(input ("How much do you make per year? "))
    elif 15000 < income <= 50000:
        print ("Tax rate = 3%")
        tax = income * .03
        income = income - tax
        print ("Tax deducated = ", tax)
        print ("Total income = ", income)
        total_tax = total_tax + tax
        print (":::" * 15) 
        name = input("Please enter your name here. ")
        income = int(input ("How much do you make per year? "))
    elif 50000 < income <= 75000:
        print ("Tax rate = 4%")
        tax = income * .04
        income = income - tax
        print ("Tax deducated = ", tax)
        print ("Total income = ", income)
        total_tax = total_tax + tax
        print (":::" * 15) 
        name = input("Please enter your name here. ")
        income = int(input ("How much do you make per year? "))
    elif 75000 < income <= 250000:
        print ("Tax rate = 5%")
        tax = income * .05
        income = income - tax
        print ("Tax deducated = ", tax)
        print ("Total income = ", income)
        total_tax = total_tax + tax
        print (":::" * 15) 
        name = input("Please enter your name here. ")
        income = int(input ("How much do you make per year? "))
    else:
        print ("Tax rate = 6%")
        tax = income * .06
        income = income - tax
        print ("Tax deducated = ", tax)
        print ("Total income = ", income)
        total_tax = total_tax + tax
        print (":::" * 15) 
        name = input("Please enter your name here. ")
        income = int(input ("How much do you make per year? "))

print ("Total taxes collected = ", total_tax)    #prints the total taxes collected
