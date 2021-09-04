player1 = int(input())
player2 = int(input())
winner = input()
out_of_eggs = False
while not winner == "End of battle":
    if winner == "one":
        player2 -= 1
    else:
        player1 -= 1

    if 0 == player1:
        print(f"Player one is out of eggs. Player two has {player2} eggs left.")
        out_of_eggs = True
        break
    elif 0 == player2:
        print(f"Player two is out of eggs. Player one has {player1} eggs left.")
        out_of_eggs = True
        break

    winner = input()

if not out_of_eggs:
    print(f"Player one has {player1} eggs left.")
    print(f"Player two has {player2} eggs left.")
