line_input = []
valid_input = ["regular", "special"]
discount = False
while True:
    line_input.append(input())
    if line_input[-1] in valid_input:
        break

if line_input[-1] == "special":
    discount = True
line_input.pop(-1)
line_input = list(map(lambda x: float(x), line_input))

for i in range(len(line_input)):
    if line_input[i] < 0:
        line_input[i] = 0
        print("Invalid price!")

no_taxes = sum(line_input)
taxes = no_taxes * 0.20
total_price = taxes + no_taxes

if no_taxes == 0:
    print("Invalid order!")
else:
    if discount:
        total_price -= (total_price * 0.10)
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {no_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
#
# 1050
# 200
# 450
# 2
# 18.50
# 16.86
# special
