liste0 = [6, 8, 1, 2, 4, 5, 9]
# liste0.sort()
# print("Küçükten büyüğe : ", liste0)
# liste0.reverse()
# print("Büyükten küçüğe",  liste0)

# last_index = liste0.pop()
# print(liste0)
# print("Son elaman : ", last_index)
# print("List now : ", liste0)
#
# print("List is", liste0)
# removed_index = liste0.pop(2)
# print("removed index is ", removed_index)
# print("List now ", liste0)

# liste1 = []
#
# i = 0
# while i < 5:
#     user_listindex = int(input("Sayı alalım"))
#     liste1.append(user_listindex)
#     i += 1
# toplam = 0
# for i in liste1:
#     toplam += i
#
# print("Toplam: ", toplam / 5)


# check = 3 in liste0 # listenin içindekileri kontrol etmek için
# print(check)
"""
liste1 = []
i = 0
while i < 3:
     user_index = int(input("Sayı giriniz \n >>>>"))
     liste1.append(user_index)
     i += 1

if 7 in liste1 :
    print("7 Sayısı bulundu")
else:
    print("You're unlucky")


#Liste birleştirme 

liste1 = [12, 1, 15, 13, 16, 17]

liste3 = liste0+liste1
print(liste3)

#Listenin en büyük ve en küçük elmanı bulma 

print("En küçük elmanı\n >>>>", min(liste3))
print("eN büyük elmanı\n >>>>", max(liste3))

print(sum(liste3)) #listenin indexlerini toplama


numbers = [i for i in range(0, 100, 2)]

answer = sum(numbers) / len(numbers)
print(answer)



#Liste kopyalama ve Çoğaltama işlmeleri

liste1 = [1, 2, 3, 4, 5, 6, 7, 9]
liste2 = liste1 #Bu işlem ram'de aynı adresi gösterir.

liste3 = liste1.copy # Bu fonksion ram'de yeni bir alan içinde oluşturulur.

#Listenin ram'de durduğu yeri öğrenme

print("Lıste1'in ram adresi :", id(liste1))
print("Lıste3'in ram adresi :", id(liste3))



#Üç boyutlu listeler

cok_boyutluLıste = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6]]

print(cok_boyutluLıste[0][1]) #1.istenin 1.elemanına
print(cok_boyutluLıste[1][2]) #2.listenin 2.elemanına

#
#Alıştırmalar 
"""

import random
print("Oyuna Hoşgeldini....")
i = 0
while i < 20:
    sans = []
    sans.append(random.randint(1, 100))
    i += 1
y = 0
while y < 3:
    user = int(input("Lütfen sayı giiniz\n >>>>"))
    aı = random.choice(sans)
    if aı in user:
        print("Doğru")
    else: 
        print("Yanlış")


