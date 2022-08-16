import oper
from view import input_data, view_data

#метод нажатия на кнопку
def button_click(): 
    numberA = input_data('Введите число А: ')
    #num_data = (int(input_data('Первое число ')), int(input_data('Второе число ')))
    znak = input_data('Укажите действие ')
    numberB = input_data('Введите число B: ')
    #data.init_data(*num_data)
    if znak == '+':
        print(oper.summ(numberA, numberB))
        #result = oper.summ(*data.return_data())
    elif znak == '-':
        print(oper.dif(numberA, numberB))
        #result = oper.dif(*data.return_data())
    elif znak == '*':
        print(oper.mult(numberA,numberB))
        #result = oper.mult(*data.return_data())
    elif znak == '/':
        print(oper.divis(numberA,numberB))
        #result = oper.divis(*data.return_data())
    #view_data(text = 'результат: ', data = result)


