
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
"""



