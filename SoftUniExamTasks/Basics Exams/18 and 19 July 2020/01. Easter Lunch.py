sweet_bread = int(input()) * 3.20
carton_eggs = int(input())
kg_cookies = int(input()) * 5.40
price_eggs = carton_eggs * 4.35
price_paint = (carton_eggs * 12) * 0.15
print(f"{sweet_bread + price_eggs + price_paint + kg_cookies:.2f}")
