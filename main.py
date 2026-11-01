def main():
    # 1. Collect inputs
    student_name = input("Enter student name: ")
    monthly_income = float(input("Enter monthly income (₹): "))
    
    food_exp = float(input("Food expenses (₹): "))
    travel_exp = float(input("Travel expenses (₹): "))
    study_exp = float(input("Study materials (₹): "))
    mobile_exp = float(input("Mobile/internet expenses (₹): "))
    other_exp = float(input("Other expenses (₹): "))

    # 2. Perform calculations
    total_expenses = food_exp + travel_exp + study_exp + mobile_exp + other_exp
    remaining_balance = monthly_income - total_expenses
    
    # 3. Prevent division by zero for savings rate
    savings_rate = 0.0
    if monthly_income > 0:
        savings_rate = (remaining_balance / monthly_income) * 100

    # 4. Display output report
    print("\n----- MONTHLY BUDGET REPORT -----")
    print(f"Student: {student_name}")
    print(f"Monthly income: ₹{monthly_income:.2f}")
    print(f"Food: ₹{food_exp:.2f}")
    print(f"Travel: ₹{travel_exp:.2f}")
    print(f"Study materials: ₹{study_exp:.2f}")
    print(f"Mobile/internet: ₹{mobile_exp:.2f}")
    print(f"Other: ₹{other_exp:.2f}")
    print(f"Total expenses: ₹{total_expenses:.2f}")
    print(f"Remaining balance: ₹{remaining_balance:.2f}")
    print(f"Savings rate: {savings_rate:.2f}%")

if __name__ == "__main__":
    main()

