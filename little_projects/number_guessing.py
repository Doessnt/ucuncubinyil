import random

def number_guessing(user):
    ai = random.randint(1, 5)
    if user == ai:
        print(f"Tahmin edilen rakam {ai}. Tebrikler doğru bildin ")
    else:
        print(f"Tahmin edilen rakam {ai}. Malesef bir daha ki sefere")

user = int(input("Lütfen rakam tahmininizi yapiniz\n >>>>"))


number_guessing(user)
                