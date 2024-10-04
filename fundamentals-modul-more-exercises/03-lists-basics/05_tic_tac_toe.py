first_line = input().split()
second_line = input().split()
third_line = input().split()

winner = ()

for index in range(len(first_line)):
    if first_line[index] == second_line[index] == third_line[index]:
        if first_line[index] == '1':
            winner = 'First'
        elif first_line[index] == '2':
            winner = 'Second'
        else:
            continue

for index in range(len(first_line) - 2):
    if first_line[index] == second_line[index + 1] == third_line[index + 2]:
        if first_line[index] == '1':
            winner = 'First'
        elif first_line[index] == '2':
            winner = 'Second'
        else:
            continue

for index in range(len(first_line)):
    if first_line[index] == second_line[index - 1] == third_line[index - 2]:
        if first_line[index] == '1':
            winner = 'First'
        elif first_line[index] == '2':
            winner = 'Second'
        else:
            continue

for index in range(len(first_line) - 2):
    if first_line[index] == first_line[index + 1] == first_line[index + 2]:
        if first_line[index] == '1':
            winner = 'First'
        elif first_line[index] == '2':
            winner = 'Second'
        else:
            continue

for index in range(len(second_line) - 2):
    if second_line[index] == second_line[index + 1] == second_line[index + 2]:
        if second_line[index] == '1':
            winner = 'First'
        elif second_line[index] == '2':
            winner = 'Second'
        else:
            continue

for index in range(len(third_line) - 2):
    if third_line[index] == third_line[index + 1] == third_line[index + 2]:
        if third_line[index] == '1':
            winner = 'First'
        elif third_line[index] == '2':
            winner = 'Second'
        else:
            continue

if winner:
    print(f'{winner} player won')
else:
    print('Draw!')
