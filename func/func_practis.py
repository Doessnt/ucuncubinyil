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

"""