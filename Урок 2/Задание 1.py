first_list = ['add', 22, ['cry', 'why'], 'bread', 'sky', 1 + 8j]
print(f"Список first_list содежить следующие значения:  {first_list}")
print('Каждое значение соответствует следующему типу данных:')
for i in first_list:
    print(f"{i} = {type(i)}")
