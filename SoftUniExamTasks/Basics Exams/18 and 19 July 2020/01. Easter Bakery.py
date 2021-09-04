price_flour = float(input())
kg_flour = float(input()) * price_flour
kg_sugar = float(input()) * (price_flour * 0.75)
carton_eggs = int(input()) * (price_flour * 1.1)
packets_maya = int(input()) * ((price_flour * 0.75) * 0.20)
print(f"{kg_flour + kg_sugar + carton_eggs + packets_maya:.2f}")
