yours_numbers = input().split()
text_message = input()

new_message = []

for current_number in yours_numbers:
    digit_sum = sum(int(digit) for digit in current_number)
    if digit_sum >= len(text_message):
        current_letter = text_message[digit_sum % len(text_message)]
        new_message.append(current_letter)
        text_message = text_message[:digit_sum % len(text_message)] + text_message[digit_sum % len(text_message) + 1:]
    else:
        current_letter = text_message[digit_sum]
        new_message.append(current_letter)
        text_message = text_message[:digit_sum] + text_message[digit_sum + 1:]

print(''.join(new_message))
