yours_numbers = input().split()
text_message = input()

new_message = []

for current_number in yours_numbers:
    digit_sum = sum(int(digit) for digit in current_number)

    if digit_sum >= len(text_message):
        index = digit_sum % len(text_message)

    else:
        index = digit_sum

    current_letter = text_message[index]
    new_message.append(current_letter)
    text_message = text_message[:index] + text_message[index + 1:]

print(''.join(new_message))
