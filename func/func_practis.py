"""
def example():
    number1 = int(input("Lütfen Sayınızı giriniz\n>>>> "))
    number2 = int(input("Lütfen Sayınızı giriniz\n>>>> "))
    islem = input("Lütfen isleminizi giriniz(+,-,/,*)\n>>>> ")
    if islem == "+":
        print(number2 + number1)
    elif islem == "-":
        print(number2 - number1)
    elif islem == "/":
        print(number2 / number1) 
    elif islem == "*":
        print(number2 * number1)
example()

##################################################

def example1(sting, number):
    print("Welcome to Los Pollos Hermanos family")

    print(sting*number)   

example1("Ali\n", 13)

##################################################

def example2(how_many_chracter, user, liste):
    print("\n\nWelcome to Los Pollos Hermanos family\n\n")
    how_many_chracter = int(input("Sayıyı giriniz\n>>>> "))
    for i in range(how_many_chracter):
        user = input("İsim giriniz\n>>>> ")
        liste.append(user)
        
    print(liste)

liste = []
how_many_chracter = 0
user = ""

example2(how_many_chracter, user, liste)    

##################################################

def example3(user, user_bool = 0):
    if user % 2 == user_bool:
        print("Çift")
    else:
        print("Tek")

user = int(input("Lütfen sayı giriniz\n>>>> "))

example3(user)
    

##################################################

def example4(liste):
    for i in liste:
        if i % 2 == 0:
            print(f"{i} bir çift sayıdır")
        else:
            print(f"{i} bir tek sayıdır")

liste = [1, 2, 3, 4, 5]
example4(liste)           

##################################################

def example5(en, boy, harf):
    for i in range(en):
        print(harf*boy)
        
    
example5(14,2,"o")

##################################################

def login():
     global user_loginName, user_loginPassword
     user_loginName = input("Lütfen isiminizi giriniz\n>>>> ")
     user_loginPassword = int(input("Lütfen parola giriniz\n>>> "))
     check()

def check():
    if user_loginName == user_name and user_loginPassword == user_password:
       
        print(f"Hoşgeldiniz {user_name} {user_surname} Tc'niz {user_id}")  
    else:
        print("HaTA")          
    
def register():
    
    global user_surname, user_password, user_email, user_first_ch, user_id, user_name
    print("Giriş ekranına hoşgeldin\n1.Kayıt\n2.Giriş\n")
    user_first_ch = int(input(">>>>"))
    if user_first_ch == 1:
        user_name = input("Lütfen isiminizi giriniz\n>>>> ")
        user_surname = input("Lütfen soyadınızı giriniz\n>>>> ")
        user_id = int(input("Lütfen TC giriniz\n>>>> "))
        user_email = input("Lütfen emailinizi giriniz\n>>>> ")
        user_password = int(input("Lütfen parola giriniz\n>>>> "))
        print("İşlem başarılı!!!")
        login()
    else:
        login()


register()

##################################################

def example7(*numbers):
    global result
    result = 0
    for i in numbers:
        result += i
    
    return result / 4

print(example7(1, 2, 3, 4))


##################################################

numbers = [1, 2, 3]
def example7(numbers):
    global result
    result = 0
    for i in numbers:
        result += i

    
    return result // len(numbers)

print(example7(numbers))

##################################################

class1 = [10, 22, 45, 65, 56]
class2 = [25, 35, 45, 55]
class3 = [90, 80, 78, 67, 98]
class4 = [56, 34, 2]

def calculation(list):
    toplam = 0
    for i in list:
        toplam += i
    
    return toplam / len(list)

liste = list()

liste.append(calculation(class1))
liste.append(calculation(class2))
liste.append(calculation(class3))
liste.append(calculation(class4))

print("Sınıf ortalamaları", liste)
print("En iyi ", max(liste))
print("En kötü ", min(liste))

def example9(number):
    if number % 2 == 0:
        return True
    else:
        return False


user = int(input("Lütfen sayı gitiniz\n>>>> "))

print(example9(user))

def example10(number1 = 0, number2 = 0):
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else: 
        return "Fuck off"

print(example10())


import time 
 
for i in range(10,0,-1): 
    print(i) 
    time.sleep(1)
"""

import datetime as dt
from tkinter import N
from unicodedata import name

zaman = dt.datetime.now()


def bruh():
    global bugun
    global after
    global toplam
    toplam = 0
    bugun = zaman.day
    after = bugun + 2
    while after > bugun:
        user = int(input("Lütfen sayı giriniz"))
        toplam += user
        print(toplam) 
    
     
bruh()

