import sys

city = input()
package = input()
vip = input()
days = int(input())
price = 0.0
discount = 0.0
a_list = ["Bansko", "Borovets", "Varna", "Burgas", "noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]
if days <= 0:
    print("Days must be positive number!")
    quit()
if city in a_list and package in a_list:
    if city == "Bansko" or "Borovets":
        if package == "noEquipment":
            price = 80
            if vip == "yes":
                discount = 5
        elif package == "withEquipment":
            price = 100
            if vip == "yes":
                discount = 10
    if city == "Varna" or "Burgas":
        if package == "noBreakfast":
            price = 100
            if vip == "yes":
                discount = 7
        elif package == "withBreakfast":
            price = 130
            if vip == "yes":
                discount = 12
else:
    print("Invalid input!")
    quit()

if days > 7:
    days -= 1
print(f"The price is {(price * ((100 - discount) / 100)) * days:.2f}lv! Have a nice time!")
