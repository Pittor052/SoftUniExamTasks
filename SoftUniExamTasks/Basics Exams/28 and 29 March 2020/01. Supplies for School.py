pens = int(input()) * 5.80
markers = int(input()) * 7.20
cleaner = float(input()) * 1.20
discount = int(input())
total = pens + markers + cleaner
final = total - ((total * discount) / 100)
print(f"{final:.3f}")