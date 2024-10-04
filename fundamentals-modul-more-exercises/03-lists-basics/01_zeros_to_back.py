list_of_string = input()

list_for_zeros = []
list_for_other = []

list_of_integer = [int(number) for number in list_of_string.split(', ')]
for current_number in list_of_integer:
    if current_number == 0:
        list_for_zeros.append(current_number)
    else:
        list_for_other.append(current_number)
print(list_for_other + list_for_zeros)
