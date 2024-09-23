monthly_salary = float(input("How much is your monthly salary? "))
loan = float(input("How much will be your loan? "))

if monthly_salary >= 30000.00:
    max_amount = monthly_salary * 10
    if loan <= max_amount:
        print("Great! You're now eligible to loan")
        months_to_pay = int(input("How many months would you like to pay the loan? "))
        interest = loan * 0.10
        total_amount = interest + loan
        print(f"Loan Amount: ₱{loan:.2f}")
        print(f"Amount to pay back: ₱{total_amount}")
        print(f"Monthly payment over {months_to_pay} months: ₱{total_amount / months_to_pay:.2f}")
    else:
        print(f"You loan is too high for your loan request!")
else:
    print("You can borrow loan because of your salary is too low")            
