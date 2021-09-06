days = int(input())
d = days
win = 0
lose = 0
money = 0
total_won = 0
total_lost = 0
total_money = 0
while not d == 0:
    command = input()
    if command == "win" or command == "lose":
        if command == "win":
            win += 1
            money += 20
        elif command == "lose":
            lose += 1
    elif command == "Finish":
        d -= 1
        if win > lose:
            total_won += 1
            total_money += money + ((money * 10) / 100)
            win = 0
            lose = 0
            money = 0
        else:
            total_money += money
            win = 0
            lose = 0
            money = 0
            total_lost += 1

if float(days / 2) < float(total_won):
    total_money += ((total_money * 20) / 100)
if total_won > total_lost:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
