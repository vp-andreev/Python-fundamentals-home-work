import math


def center_point(number_one: float, number_two: float, number_three: float, number_four: float):
    distance_one = math.sqrt(number_one ** 2 + number_two ** 2)
    distance_two = math.sqrt(number_three ** 2 + number_four ** 2)
    if distance_one < distance_two:
        return f'({math.floor(number_one)}, {math.floor(number_two)})'
    else:
        return f'({math.floor(number_three)}, {math.floor(number_four)})'


xray_one = float(input())
yankee_one = float(input())
xray_two = float(input())
yankee_two = float(input())

print(center_point(xray_one, yankee_one, xray_two, yankee_two))
