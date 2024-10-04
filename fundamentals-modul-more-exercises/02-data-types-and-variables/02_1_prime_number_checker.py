yours_number = int(input())

if yours_number <= 1:
    print(False)
else:
    is_prime = True
    for num in range(2, int(yours_number ** 0.5) + 1):
        if yours_number % num == 0:
            is_prime = False
            break
    print(is_prime)
