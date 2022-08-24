# 1) Введите число 1
# 2) Введите число 2
# 3) Какую операцию производим


def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print('Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите число 1 (используйте формат: "2 + 3i"):')
        left_value = get_value()
        print('Введите число 2 (используйте формат: "2 + 3i"):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите число 1 (используйте формат дроби: "2/3"):')
        left_value = get_value()
        print('Введите число 2 (используйте формат дроби: "2/3"):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    return (data_type, left_value, oper, right_value)