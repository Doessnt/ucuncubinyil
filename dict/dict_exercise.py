sozluk =  dict()
"""
sozluk["İsim"] = user1 = input("İsim alayım\n>>>>")
sozluk["Soyad"] = user4 = input("Soyad alayım\n>>>>")
sozluk["Cinsiyet"] = user3 = input("Cinsiyet alayım\n>>>>")
sozluk["Yaş"] = user2 = int(input("Yaş alayım\n>>>>"))

user_input = input("Lütfen İstediğiniz bilgiyi yazınız \n>>>")

print(sozluk[user_input])
print(sozluk)

It  = []
Bı = []
Ms = []

for i in range(2):
 userIt = input("It isimi\n>>>>")
 It.append(userIt)

for i in range(2):
 userBI = input("Bı isimi\n>>>>")
 Bı.append(userIt)

for i in range(2):
 userIt = input("Muhasebe isimi\n>>>>")
 Ms.append(userIt)
 
sozluk["It"] = It
sozluk["Bı"] = Bı
sozluk["Ms"] = Ms

user_input = input("Lütfen Departman giriniz\n[It, Bı, Ms]\n>>>>")

print(sozluk[user_input])

sozluk = {"car": "", "cat":"", "driver":""}
for i in sozluk.keys():
    sozluk[i]  = input("{} kelinesinin türkçesini giriniz\n>>>> ".format(i))

print(sozluk)

"""
sozluk = {"Siyah": "Black", "Home": "Ev", "Arkadaş" : "Friend"}

while True:
    user = int(input("""
    Lütfen Yapmak istediğiniz işlemi giriniz 
    1- Arama
    2- Çıkarma
    3- Listeleme
    4- Çıkış
    """))
    if user == 4:
        break
    # Sözlükte arama yapma
    elif user == 1:
        userSearch = input("Lütfen aradığınız kelimeyi giriniz\n>>>>")
        if userSearch in sozluk:
            print(sozluk[userSearch])
        else:
            print("Aradığınız kelime darcığımızı geliştrimek istermsiiniz ? Y/N\n")
            userBool = input("?")
            if userBool == "Y":
                sozluk[userSearch] = input("Lütfen İngilizcesini giriniz\n>>>>")
                print(sozluk)
                break
            else:
                break
    elif user == 2: #Sözlükten item çıkarma
        userDelete = input("Lütfen çıkarmak isteğiniz kelimeleri giriniz {}\n>>>>".format(sozluk))
        sozluk.pop(userDelete)
        print("Silindi")
        print(sozluk)
    elif user == 3:
        print(sozluk)
 


