def monthlySales():
    sales = float(input("Enter the total sales of the month: "))
    return sales

def stateTax():
    stax = S * (4/100)
    return stax

def countyTax():
    ctax = S * (2/100)
    return ctax

def totalTax():
    total = stax + ctax
    return total

S = monthlySales()
stax = stateTax()
ctax = countyTax()
total = totalTax()

print("Monthly sales: $",S)
print("State tax: $",stax)
print("County tax: $",ctax)
print("Total tax: $",total)
