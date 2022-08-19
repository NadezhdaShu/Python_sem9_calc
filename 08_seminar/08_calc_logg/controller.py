import oper
import view
from view import input_data
from logg import data_logger

#метод нажатия на кнопку
def button_click(): 
    numberA = int(input_data('Введите число А: '))
    znak = input_data('Укажите действие ')
    numberB = int(input_data('Введите число B: '))
    if znak == '+':
        print(oper.summ(numberA, numberB))
        result = oper.summ(numberA, numberB)
    elif znak == '-':
        print(oper.dif(numberA, numberB))   
        result = oper.dif(numberA, numberB)
    elif znak == '*':
        print(oper.mult(numberA,numberB))
        result = oper.mult(numberA, numberB)        
    elif znak == '/':
        print(oper.divis(numberA,numberB))
        result = oper.divis(numberA, numberB)
    view.view_data(result, 'result')  
    data_logger(numberA, numberB, result, znak)
