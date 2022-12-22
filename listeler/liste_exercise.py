import random
"""
#Kodları anlamak için pythontutor.com
liste = []
for i in range(5):
    user = input("Kelime alayım\n>>>> ")
    liste.append(user)
user2 = input("Aradığınız kelime\n>>>> ")

if user2 in liste:
    print("Buldum {}".format(user2))
else:
    print("Bulamadım")
"""
""""""
"""
liste = []

breakk = -1

while True:
    user = int(input("Sayı alayım\n>>>>"))
    if user == breakk:
        break
    else:
        liste.append(user)

list2 =  []
for i in liste:
    if i % 2 == 0:
        list2.append(i)

print(list2)        



#liste.sort()
#print(liste)
#liste.reverse()
#print(liste)


#for i in range(1, 10):
#    print(str(i)*i)



liste = []
for i in range(15):
    j = random.randint(1, 50)
    liste.append(j)


toplam = 0

for i in liste:
    toplam += i #Listenin içindekileri toplama
    toplam2 = toplam // len(liste) #Ortalamasını alma 
    toplam3 = toplam*i+1 #Faktoriyel hesaplama
print(toplam)
print(toplam2)
print(toplam3)

"""


