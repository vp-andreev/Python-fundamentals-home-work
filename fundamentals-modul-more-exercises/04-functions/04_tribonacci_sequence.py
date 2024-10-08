def tribonacci_sequence(number: int):
    tribonacci = [1, 1, 2]
    for digit in range(number):
        if digit < 3:
            print(tribonacci[digit], end=' ')
        else:
            next_value = tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
            print(next_value, end=' ')
            tribonacci.append(next_value)


some_number = int(input())
tribonacci_sequence(some_number)
