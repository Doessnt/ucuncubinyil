
"""
def merhaba_write():
    print("merhaba")


merhaba_write()



#Local değişken 
def toplama():
    number1 = 10
    number2 = 5
    toplam = number1 + number2
    print(toplam)

toplama()

#global değişkenler

def toplama():
    number1 = 10
    number2 = 5
    global toplam #global değişken
    toplam= number1 + number2 

toplama()
print(toplam)

# Parametre ihtiyacı duyan fonksiyonlar

def toplam(number1, number2):
    result = number1 + number2
    print(result)

toplam(10, 5)

# Defualt değerler
def toplam(number1, number2 = 10):
    result = number1 + number2
    print(result)

toplam(10)



# Çoklu parametreler
def example(*numbers):
    for i in numbers:
        print(i)

example(1,4,5, 13131232131, 31231232131,41423534523534)



def example(*number):
    toplam = 0
    for i in number:
        toplam += i
    print(toplam)

example(1,4,5, 13131232131, 31231232131,41423534523534)

######################Return###########################
#def pow1(nunber1, up):
#    return nunber1 ** up


def example0(number1 = 0, number2 = 0):
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else: 
        return "Fuck off"


def example1(x, y, z):
    return example0(x, example0(y, z))

print(example1(20, 15, 21))

####################Hazır fonksiyonlar###########################
words = "Bugün.hava.çok.sıcak.değildi."
wordList = words.split(".") #Kelimeleri .'lardan itibaren parçala
print(wordList)


# Time func
from datetime import timedelta, timezone
import datetime as dt

time = dt.datetime.now()
print(time.month)
print(time.year)
print(time.second)
print(time.hour)
print("Formatlı hali :", time.strftime("%A/%m/%Y"))

import datetime as dt
import locale as lc

lc.setlocale(lc.LC_ALL, 'Turkish_Turkey.1254')
print(time.strftime("%A"))

"""

