plastic = (int(input()) + 2) * 1.50
paint = int(input())
coreselin = int(input()) * 5
hours = int(input())
expenses = plastic + ((paint + (paint * 0.1)) * 14.50) + coreselin + 0.40
work = (expenses * 0.30) * hours
print(f"Total expenses: {work + expenses:.2f} lv.")
