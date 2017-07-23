initialInvestment = input("How much would you like to invest today?")
numberOfYears = input("How many years would you like to invest your money?")
annualInterestRate = input("What interest rate would you like to invest at? Enter as a decimal: (For 2.5% enter 0.025)")


x=1
print "Month\t,   Interest Earned\t,   Total To Date"

while x <= (numberOfYears + 1):
    interestEarned = initialInvestment * (annualInterestRate/12)
    initialInvestment = interestEarned + initialInvestment
    print x, "\t", "$", "{:.2f}".format(interestEarned), "\t", "$", "{:.2f}".format(initialInvestment)
    if x == x + 1:
        break




