
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
"""

