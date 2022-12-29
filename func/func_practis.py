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


def example1(sting, number):
    print("Welcome to Los Pollos Hermanos family")

    print(sting*number)   

example1("Ali\n", 13)
"""

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






