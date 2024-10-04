def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

yours_number = int(input())

if is_prime(yours_number):
    print(True)
else:
    print(False)


# yours_number = int(input())
#
# if yours_number <= 1:
#     print(False)
#     exit()
# count = 0
# for num in range(2, yours_number + 1):
#     if yours_number % num == 0:
#         count += 1
# if count > 1:
#     print(False)
# else:
#     print(True)

