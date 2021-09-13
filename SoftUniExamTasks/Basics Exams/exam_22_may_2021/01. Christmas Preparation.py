packages = int(input()) * 5.80
rolls = int(input()) * 7.20
glue = float(input()) * 1.20
discount = int(input())
final = (packages + rolls + glue) * ((100 - discount) / 100)
print(f"{final:.3f}")