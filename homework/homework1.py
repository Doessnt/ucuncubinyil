# Parametreli fonksiyon olmak şartıyla sansür uygulama fonksiyonu yapınız
"""
liste = ["Araba çocuk unuttum", "Su güzel bir şey", "Bugün yorgun uyandim"]

"""
liste = ["Araba çocuk unuttum", "Su güzel bir şey", "Bugün yorgun uyandim", "test"]

def alphabet_change(user_select, user_change, user_change2, liste):
 name = liste[user_selcet]
 
 liste[user_selcet] = name.replace(user_change, user_change2)

 print(liste)
    

user_selcet = int(input(f"{liste}\n Lütfen listedeki değiştirmek istedeğiniz liste indexini seçiniz\nNOT(0, 1, 2) >>>>"))

user_change = input(f"{liste[user_selcet]}\n Lütfen Bu listede değiştirmek istediğiniz harfleri seçiniz\n >>>>")

user_change2 = input(f"{liste[user_selcet]}\n Lütfen Bu listede değiştireceğini harfleri yaziniz\n >>>>")

alphabet_change(user_selcet, user_change, user_change2, liste)




