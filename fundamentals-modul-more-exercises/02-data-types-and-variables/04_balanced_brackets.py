number_of_lines = int(input())

opening_bracket = '('
closing_bracket = ')'

balance = 0
balanced = True

for value in range(number_of_lines):
    random_text = input()
    if random_text == opening_bracket:
        if balance != 0:
            balanced = False
            break
        balance += 1
    elif random_text == closing_bracket:
        if balance == 0:
            balanced = False
            break
        balance -= 1

if balanced and balance == 0:
    print('BALANCED')
else:
    print('UNBALANCED')
