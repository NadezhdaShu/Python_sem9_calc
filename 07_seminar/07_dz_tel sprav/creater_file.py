from data_enter import input_firstname
from data_enter import input_lastname
import string
import secrets

filename = "Tel_book.csv" 
myfile = open(filename, "a+") 
myfile.close




def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input("Введите номер телефона: ") 
    emailID = input("Введите ваш E-mail: ") 
    contactDetails =(f"" + firstname + " " + lastname + "  " + phoneNum + "  " + emailID +  "\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print("Новая запись добавлена в телефонный справочник: \n " + contactDetails + "")  
 