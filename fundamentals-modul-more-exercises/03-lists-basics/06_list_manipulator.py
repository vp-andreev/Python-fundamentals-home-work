def exchange_list(list_of_numbers, index):
    if index < 0 or index >= len(list_of_numbers):
        print("Invalid index")
    else:
        list_of_numbers[:] = list_of_numbers[index + 1:] + list_of_numbers[:index + 1]


def max_even_odd(list_of_numbers, equality):
    max_index = [i for i in range(len(list_of_numbers)) if (list_of_numbers[i] % 2 == 0) == (equality == "even")]
    if not max_index:
        print("No matches")
    else:
        print(max(max_index, key=lambda i: (list_of_numbers[i], i)))


def min_even_odd(list_of_numbers, equality):
    min_index = [i for i in range(len(list_of_numbers)) if (list_of_numbers[i] % 2 == 0) == (equality == "even")]
    if not min_index:
        print("No matches")
    else:
        print(min(min_index, key=lambda i: (list_of_numbers[i], -i)))


def first_even_odd(list_of_numbers, count, parity):
    if count > len(list_of_numbers):
        print("Invalid count")
    else:
        filtered = [x for x in list_of_numbers if (x % 2 == 0) == (parity == "even")]
        print(filtered[:count])


def last_even_odd(list_of_numbers, count, parity):
    if count > len(list_of_numbers):
        print("Invalid count")
    else:
        filtered = [x for x in list_of_numbers if (x % 2 == 0) == (parity == "even")]
        print(filtered[-count:])


list_of_numbers = list(map(int, input().split()))
while True:
    command = input().split()
    if command[0] == "end":
        break
    elif command[0] == "exchange":
        exchange_list(list_of_numbers, int(command[1]))
    elif command[0] == "max":
        max_even_odd(list_of_numbers, command[1])
    elif command[0] == "min":
        min_even_odd(list_of_numbers, command[1])
    elif command[0] == "first":
        first_even_odd(list_of_numbers, int(command[1]), command[2])
    elif command[0] == "last":
        last_even_odd(list_of_numbers, int(command[1]), command[2])
print(list_of_numbers)
