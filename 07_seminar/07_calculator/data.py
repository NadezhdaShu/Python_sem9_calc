def init_data(x_1, x_2): # метод отвечает за инициализацю начальных значений х и у
    global a, b
    a = x_1
    b = x_2

def return_data():
    global a, b
    return a, b

a = 0
b = 0
