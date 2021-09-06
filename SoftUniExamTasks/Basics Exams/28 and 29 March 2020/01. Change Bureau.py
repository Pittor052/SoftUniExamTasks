bitcoins = float(input()) * 1168
yuan = float(input())
commission = float(input())
total = ((bitcoins + ((yuan * 0.15) * 1.76)) / 1.95) * ((100 - commission) / 100)
print(f"{total:.2f}")
