# Tax breakdowns are below:
# No tax paid on £12,570 personal allowance.
# £12,571 to £23,000 starter rate of 19%
# £23,000 to £40,000 intermediate rate of 30%
# £40,001 to £150,000 higher rate of 41%
# Above £150,000 top rate of 46%

def incomeTax(salary):
    if salary <= 12750:
        print("No tax to be paid")
    elif salary >= 12571 and salary < 23000:
        tax = salary * 0.19
        print(f"You will pay £{tax}")
    elif salary >= 23000 and salary < 40000:
        tax = salary * 0.30
        print(f"You will pay £{tax}") 
    elif salary >= 40001 and salary <=150000:
        tax = salary * 0.41
        print(f"You will pay £{tax}")  
    else:
        tax = salary * 0.46
        print(f"You will pay £{tax}") 
        
incomeTax(45000)
incomeTax(12000)
incomeTax(30000)