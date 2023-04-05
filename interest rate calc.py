# This program calculates compound interest

# Define the variables
principal = int(input("Enter the principal amount: "))
capital = principal
Monthly = int(input("Enter Monthly deposit: "))
rate = float(input("Enter the interest rate: "))
n = int(input("Enter the number of years: "))

# Calculate the compound interest
# interest = principal * ((1 + rate / 100)**n - 1)

# Calculate the total amount
total_interest = 0

# Print the table header
print("{:<8}{:<15}{:<12}{:<15}{:<15}{:<12}".format("Year", "Principal", "Interest","Year end","Cumu Return %","Annu Return %"))

# Calculate and print the values for each year
for i in range(1, n+1):
    year_interest = principal * (rate / 100)
    year_end = principal + year_interest + Monthly*12
    total_interest = year_interest + total_interest
    cumu_return = (total_interest / capital)* 100
    annu_return = cumu_return/i
    print("{:<8}{:<15.2f}{:<12.2f}{:<15.2f}{:<15.2f}{:<12.2f}".format(i, principal, year_interest,year_end,cumu_return,annu_return))
    principal = year_end

 
    

# Print the total amount
print("{:<8}{:<15}{:<12}{:<24}".format("Total", "", total_interest, "")) 
