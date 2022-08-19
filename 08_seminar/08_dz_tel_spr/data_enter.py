# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


#имя
def input_firstname(): 
    first = input("Введите имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# фамилия 
def input_lastname(): 
    last = input("Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname