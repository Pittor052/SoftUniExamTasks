computers = int ( input () )
total_computers = computers
total_rating = 0
total_sales = 0
while not computers == 0:
    command = int ( input () )
    possible_sales = 0
    last_digit = command % 10
    first_two_digits = command // 10
    rating = last_digit
    if rating == 3:
        possible_sales = first_two_digits * 0.5
    elif rating == 4:
        possible_sales = first_two_digits * 0.70
    elif rating == 5:
        possible_sales = first_two_digits * 0.85
    elif rating == 6:
        possible_sales += first_two_digits
    total_rating += rating
    total_sales += possible_sales
    computers -= 1
print(f"{total_sales:.2f}")
print(f"{total_rating / total_computers:.2f}")
