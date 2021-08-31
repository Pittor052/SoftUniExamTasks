voucher = int(input())
tickets = 0
other = 0
while voucher > 0:
    command = input()
    price_ticket = 0
    price_other = 0
    if command == "End":
        break
    elif len(command) > 8:
        for i in range(2):
            price_ticket += int(ord(command[i]))
    elif len(command) <= 8:
        for i in range(1):
            price_other += int(ord(command[i]))
    if price_ticket <= voucher and not price_ticket == 0:
        tickets += 1
        voucher -= price_ticket
    elif price_other <= voucher and not price_other == 0:
        other += 1
        voucher -= price_other
    else:
        print()
        break

print(tickets)
print(other)
