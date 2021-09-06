minutes_day = int(input())
walks_day = int(input())
calories_day = int(input())
total_minutes_walk = minutes_day * walks_day
burned_calories_daily = total_minutes_walk * 5
if burned_calories_daily >= (calories_day / 2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories_daily}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {abs(burned_calories_daily)}.")
