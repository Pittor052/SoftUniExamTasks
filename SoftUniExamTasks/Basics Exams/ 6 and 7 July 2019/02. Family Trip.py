budget = float(input())
days = int(input())
price = float(input())
more_expenses = int(input())
if days > 7:
    price *= 0.95
expenses = (budget * (more_expenses / 100)) + (days * price)
if budget >= expenses:
    print(f"Ivanovi will be left with {abs(budget - expenses):.2f} leva after vacation.")
else:
    print(f"{abs(budget - expenses):.2f} leva needed.")