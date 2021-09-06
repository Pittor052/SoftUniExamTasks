import math

days = int(input())
food = float(input())
count = 0
total_cookies = 0.0
eaten_food = 0.0
total_dogy = 0.0
total_koty = 0.0
for i in range(1, days + 1):
    days -= 1
    count += 1
    dogy = int(input())
    koty = int(input())
    cookie = 0
    eaten_food += dogy + koty
    if count == 3:
        count = 0
        cookie = ((dogy + koty) * 0.1)
        total_cookies += cookie
    total_dogy += dogy
    total_koty += koty

print(f"Total eaten biscuits: {round(total_cookies)}gr.")
total_food = (eaten_food / food) * 100
print(f"{total_food:.2f}% of the food has been eaten.")
total_dogy = (total_dogy / eaten_food) * 100
print(f"{total_dogy:.2f}% eaten from the dog.")
total_koty = (total_koty / eaten_food) * 100
print(f"{total_koty:.2f}% eaten from the cat.")

