import math


def center_point(exray_one: float, yankee_one: float, exray_two: float, yankee_two: float):
    distance_one = math.sqrt(exray_one ** 2 + yankee_one ** 2)
    distance_two = math.sqrt(exray_two ** 2 + yankee_two ** 2)
    return (exray_one, yankee_one) if distance_one <= distance_two else (exray_two, yankee_two)


def line_length(exray_one: float, yankee_one: float, exray_two: float, yankee_two: float):
    return math.sqrt((exray_two - exray_one) ** 2 + (yankee_two - yankee_one) ** 2)


def longer_line(exray_one: float, yankee_one: float, exray_two: float, yankee_two: float,
                exray_three: float, yankee_three: float, exray_fourth: float, yankee_fourth: float):
    line_length_one = line_length(exray_one, yankee_one, exray_two, yankee_two)
    line_length_two = line_length(exray_three, yankee_three, exray_fourth, yankee_fourth)

    if line_length_one > line_length_two:
        start_point = center_point(exray_one, yankee_one, exray_two, yankee_two)
        end_point = (exray_two, yankee_two) if start_point == (exray_one, yankee_one) else (exray_one, yankee_one)
    else:
        start_point = center_point(exray_three, yankee_three, exray_fourth, yankee_fourth)
        end_point = (exray_fourth, yankee_fourth) if start_point == (exray_three, yankee_three) else (
            exray_three, yankee_three)

    print(f"({start_point[0]}, {start_point[1]})({end_point[0]}, {end_point[1]})")


first_exray = float(input())
first_yankee = float(input())
second_exray = float(input())
second_yankee = float(input())
third_exray = float(input())
third_yankee = float(input())
fourth_exray = float(input())
fourth_yankee = float(input())

longer_line(math.floor(first_exray), math.floor(first_yankee), math.floor(second_exray), math.floor(second_yankee),
            math.floor(third_exray), math.floor(third_yankee), math.floor(fourth_exray), math.floor(fourth_yankee))
