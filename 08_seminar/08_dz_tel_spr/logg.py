from datetime import datetime
from time import time
from pathlib import Path
from creater_file import newcontact

def data_logger(contactDetails):
    path_loger = Path('08_seminar', '08_dz_tel_spr', 'logger-tel.csv')
    time = datetime.now().strftime('%H:%M')
    with open(path_loger, 'a') as log_file:
       #log_file.write(time + ';' + data + ';\n')   
        log_file.write('\n {}\n'.format(time))
        log_file.write('\n imya{} familia{} nomer tel {} \n e-mail{}\n'
                .format(contactDetails))

# def data_logger(x, y, z, l):
#     path_loger = Path("08_seminar", "logger.csv")
#     time = dt.now()#.strftime('%H:%M')
#     with open(path_loger, 'a') as log_file:
#         log_file.write('-----------------------------------------------')
        
#         log_file.write('\nTime of adding new data: {}\n'.format(time))
        
#         log_file.write('\nЧисло А: {} {} Число В: {} \nResult: {}\n'
#                         .format(x, l, y, z))
