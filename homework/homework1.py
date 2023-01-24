# Parametreli fonksiyon olmak şartıyla sansür uygulama fonksiyonu yapınız
"""
liste = ["Araba çocuk unuttum", "Su güzel bir şey", "Bugün yorgun uyandim"]


liste = ["Araba çocuk unuttum", "Su güzel bir şey", "Bugün yorgun uyandim", "test"]

def alphabet_change(user_select, user_change, user_change2, liste):
  
  name = liste[user_selcet]
 
  liste[user_selcet] = name.replace(user_change, user_change2)

  print(liste)
    

user_selcet = int(input(f"{liste}\n Lütfen listedeki değiştirmek istedeğiniz liste indexini seçiniz\nNOT(0, 1, 2) >>>>"))

user_change = input(f"{liste[user_selcet]}\n Lütfen Bu listede değiştirmek istediğiniz harfleri seçiniz\n >>>>")

user_change2 = input(f"{liste[user_selcet]}\n Lütfen Bu listede değiştireceğini harfleri yaziniz\n >>>>")

alphabet_change(user_selcet, user_change, user_change2, liste)

"""

class gonderen():
  def __init__(self, ad, soyad, iban) -> None:
      self.ad = ad
      self.soyad = soyad
      self.iban = iban
      self.__bakiye = 0

  def setBakiye(self, bakiye):
    self.__bakiye -= bakiye
  def getBakiye(self):
    return self.__bakiye


class alan():
  def __init__(self, ad, soyad, iban) -> None:
      self.ad = ad
      self.soyad = soyad
      self.iban = iban
      self.__bakiye = 0

  def setBakiye(self, bakiye):
    self.__bakiye += bakiye
  def getBakiye(self):
    return self.__bakiye




ad = input("Gönderen kişi adı \n >>>>")
soyad = input("Gönderen kişi soyadı \n >>>>")
bakiye = int(input("Gönderen kişi bakiye \n >>>>"))
iban = int(input("Gönderen kişi ibanı \n >>>>"))
miktar = int(input("Ne verecen\n >>>>"))

adAlan = input("Alan kişi adı \n >>>>")
soyadAlan = input("Alan kişi soyadı \n >>>>")
bakiyeAlan = int(input("Alan kişi bakiye \n >>>>"))
ibanAlan = int(input("Alan kişi ibanı \n >>>>"))


Gonderen = gonderen(ad, soyad, iban)
Alan = alan(adAlan, soyadAlan, ibanAlan)

Alan.setBakiye(bakiyeAlan)
Gonderen.setBakiye(-bakiye)

Alan.setBakiye(miktar)
Gonderen.setBakiye(miktar)

print("{} {} kişisinden hesabınıza {} TL para gönderdi. Bakiyeniz {} ".format(Gonderen.ad, Gonderen.soyad, miktar, Alan.getBakiye()))
print("Gönderen kişini yeni bakiyesi: "+ str(Gonderen.getBakiye()))




























