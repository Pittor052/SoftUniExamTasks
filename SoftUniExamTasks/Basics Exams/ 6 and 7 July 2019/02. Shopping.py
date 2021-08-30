budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())
price_gpu = gpu * 250
price_cpu = (price_gpu * 0.35) * cpu
price_ram = (price_gpu * 0.1) * ram
total_price = price_gpu + price_cpu + price_ram
if gpu > cpu:
    total_price -= (total_price * 0.15)
if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")