time_to_pass = list(map(int, input().split()))

necessary_index = len(time_to_pass) // 2

total_time_left_car = 0
total_time_right_car = 0

time_of_left_car = time_to_pass[:necessary_index]
time_of_right_car = time_to_pass[necessary_index + 1:]
time_of_right_car.reverse()

for current_time in time_of_left_car:
    if current_time != 0:
        total_time_left_car += current_time
    else:
        total_time_left_car *= 0.80

for current_time in time_of_right_car:
    if current_time != 0:
        total_time_right_car += current_time
    else:
        total_time_right_car *= 0.80

if total_time_left_car < total_time_right_car:
    winer = 'left'
    total_time = total_time_left_car
else:
    winer = 'right'
    total_time = total_time_right_car

print(f"The winner is {winer} with total time: {total_time:.1f}")
