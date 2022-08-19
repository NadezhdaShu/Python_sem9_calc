from datetime import datetime
from time import time
from pathlib import Path
from creater_file import newcontact

def data_logger(firstname, lastname, phoneNum, emailID):
    path_loger = Path('08_seminar', '08_dz_tel_spr', 'logger-tel.csv')
    time = datetime.now().strftime('%H:%M')
    with open(path_loger, 'a') as log_file:
       #log_file.write(time + ';' + data + ';\n')   
        log_file.write('\n {}\n'.format(time))
        log_file.write('\n {} {}  {} \n {}\n'
                .format(firstname, lastname, phoneNum, emailID))

# def data_logger(x, y, z, l):
#     path_loger = Path("08_seminar", "logger.csv")
#     time = dt.now()#.strftime('%H:%M')
#     with open(path_loger, 'a') as log_file:
#         log_file.write('-----------------------------------------------')
        
#         log_file.write('\nTime of adding new data: {}\n'.format(time))
        
#         log_file.write('\nЧисло А: {} {} Число В: {} \nResult: {}\n'
#                         .format(x, l, y, z))

    # firstname = input_firstname() 
    # lastname = input_lastname() 
    # phoneNum = input("Введите номер телефона: ") 
    # emailID = input("Введите ваш E-mail: ") 
    # contactDetails =(f"" + firstname + " " + lastname + "  " + phoneNum + "  " + emailID +  "\n") 
    # # myfile = open(filename, "a") 
    # # myfile.write(contactDetails) 
    # with open('Tel_book.txt', 'a') as myfile:
    #     myfile.write(contactDetails)
    # print("Новая запись добавлена в телефонный справочник: \n " + contactDetails + "")