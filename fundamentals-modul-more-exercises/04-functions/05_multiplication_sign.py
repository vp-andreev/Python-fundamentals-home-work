def multiplication_result(first_number: int, second_number: int, third_number: int):
    if first_number == 0 or second_number == 0 or third_number == 0:
        return 'zero'

    negative_digits = 0
    for digit in [first_number, second_number, third_number]:
        if digit < 0:
            negative_digits += 1
    if negative_digits % 2 != 0:
        return 'negative'

    else:
        return 'positive'




number_one = int(input())
number_two = int(input())
number_three = int(input())

print(multiplication_result(number_one, number_two, number_three))