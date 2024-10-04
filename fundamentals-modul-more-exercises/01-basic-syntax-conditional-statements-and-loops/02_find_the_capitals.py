your_word = input()
capital_index = []
for index, char in enumerate(your_word):
    if char.isupper():
        capital_index.append(index)
print(capital_index)
