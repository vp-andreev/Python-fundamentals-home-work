first_line = input().split()
second_line = input().split()
third_line = input().split()

lines = [first_line, second_line, third_line]

winner = ()

for row in lines:
    for index in range(len(row) - 2):
        if row[index] == row[index + 1] == row[index + 2]:
            if row[index] == '1':
                winner = 'First'
            elif row[index] == '2':
                winner = 'Second'
            else:
                continue

for index in range(len(lines[0])):
    if first_line[index] == second_line[index] == third_line[index]:
        if first_line[index] == '1':
            winner = 'First'
        elif first_line[index] == '2':
            winner = 'Second'
        else:
            continue

if lines[0][0] == lines[1][1] == lines[2][2]:
    if lines[0][0] == '1':
        winner = 'First'

    elif lines[0][0] == '2':
        winner = 'Second'

if lines[0][2] == lines[1][1] == lines[2][0]:
    if lines[0][2] == '1':
        winner = 'First'

    elif lines[0][2] == '2':
        winner = 'Second'

if winner:
    print(f'{winner} player won')
else:
    print('Draw!')
