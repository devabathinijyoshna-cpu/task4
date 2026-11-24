basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentives: "))

gross = basic + allowance + overtime + incentive

if gross >= 50000:
    deduction = gross * 0.10
elif gross >= 25000:
    deduction = gross * 0.05
else:
    deduction = 0

net = gross - deduction

print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)