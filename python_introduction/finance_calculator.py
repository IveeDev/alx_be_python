MONTHS = 12
# monthly_income = int(input("Enter your monthly income: "))
# monthly_expenses = int(input("Enter your total monthly expenses: "))
# monthly_savings = monthly_income - monthly_expenses
# yearly_interest = monthly_savings * MONTHS * 0.05
# projected_savings = monthly_savings * MONTHS + yearly_interest

# print(f"Projected saving after one year, with interest, is ${
#       projected_savings}")


def calc_projected_savings():
    monthly_income = int(input("Enter your monthly income: "))
    monthly_expenses = int(input("Enter your total monthly expenses: "))
    monthly_savings = monthly_income - monthly_expenses
    yearly_interest = monthly_savings * MONTHS * 0.05
    projected_savings = monthly_savings * MONTHS + yearly_interest

    print(f"Projected saving after one year, with interest, is ${
        projected_savings}")


calc_projected_savings()
