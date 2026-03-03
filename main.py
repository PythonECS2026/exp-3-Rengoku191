# Program to calculate Gross Salary of an employee

# Taking Basic Salary as input
bs = float(input("Enter the Basic Salary (BS): "))

# Calculating allowances
da = 0.70 * bs   # Dearness Allowance (70% of BS)
ta = 0.30 * bs   # Travel Allowance (30% of BS)
hra = 0.10 * bs  # House Rent Allowance (10% of BS)

# Calculating Gross Salary
gross_salary = bs + da + ta + hra

# Displaying the results
print("\n----- Salary Details -----")
print("Basic Salary:", bs)
print("Dearness Allowance (70%):", da)
print("Travel Allowance (30%):", ta)
print("House Rent Allowance (10%):", hra)
print("Gross Salary:", gross_salary)
