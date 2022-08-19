# задание: написать модуль логирования действий пользователя в калькуляторе, с дата штампом

from datetime import datetime as dt
from time import time
from pathlib import Path

def data_logger(x, y, z, l):
    path_loger = Path("08_seminar", "logger.csv")
    time = dt.now()#.strftime('%H:%M')
    with open(path_loger, 'a') as log_file:
        log_file.write('-----------------------------------------------')
        
        log_file.write('\nTime of adding new data: {}\n'.format(time))
        
        log_file.write('\nЧисло А: {} {} Число В: {} \nResult: {}\n'
                        .format(x, l, y, z))




# import datetime
# import os

# class Log():
#     def __init__(self, filename):
#         self.filename = filename
#         if self.isnew():
#             f = open(self.filename,'w')
#             f.close()


# def isnew(self):
#     return not os.path.isfile(self.filename)


# def get_event(self, obj, str_in):
#     time_stap = datetime.datetime.today()
#     res_str = str(time_stap) + ' | ' + str(obj) + ' | ' + str_in +'\n'
#     with open(self.filename, 'a') as f:
#         f.write(res_str)

#https://github.com/ekolenko/lesson8.git
#https://github.com/chenskiy/Python/tree/main/calculator

