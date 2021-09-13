budget = float(input()) * 5
income = float(input()) * 5
expenses = float(input())
gift_price = float(input())
total_income = (budget + income) - expenses
if total_income >= gift_price:
    print(f"Profit: {total_income:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {abs(total_income - gift_price):.2f} BGN.")