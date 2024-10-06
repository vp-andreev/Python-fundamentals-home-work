def data_type(key_word: str, data: input):
    if key_word == 'int':
        return int(data) * 2
    elif key_word == 'real':
        return f'{(float(data) * 1.5):.2f}'
    elif key_word == 'string':
        return f'${data}$'


some_word = input()
some_data = input()

print(data_type(some_word, some_data))
