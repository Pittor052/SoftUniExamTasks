guests = int(input())
price_per_guest = float(input())
budget = float(input()) * 0.90
total_price = 0.0

if 10 <= guests <= 15:
    price_per_guest *= 0.85
    total_price = price_per_guest * guests
elif 16 <= guests <= 20:
    price_per_guest *= 0.8
    total_price = (price_per_guest * guests)
elif 20 < guests:
    price_per_guest *= 0.75
    total_price = (price_per_guest * guests)
else:
    total_price = price_per_guest * guests

if total_price <= budget:
    print(f"It is party time! {abs(budget - total_price):.2f} leva left.")
else:
    print(f"No party! {abs(budget - total_price):.2f} leva needed.")
