from datetime import datetime as dt
from time import time
from pathlib import Path

def result_logger(data, result):
    path_loger = Path("09_lec&sem_PIP", "09_DZ_Calc", "log.csv")
    left_value, oper, right_value = data
    data_str = f'{str(left_value)} {oper} {str(right_value)}'
    time = dt.now().strftime('%H:%M')
    # print('{}; операция : {} результат : {}\n'.format(time, data_str, data))
    
    with open(path_loger, 'a') as file:
        file.write('{}; операция : {} результат :{}\n'.format(time, data_str, result))


