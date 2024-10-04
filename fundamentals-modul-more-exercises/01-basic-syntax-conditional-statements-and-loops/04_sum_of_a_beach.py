your_word = input().lower()
words_looking_for = ["sand", "water", "fish", "sun"]

total_count = 0
for word in words_looking_for:
    total_count += your_word.count(word)

print(total_count)
