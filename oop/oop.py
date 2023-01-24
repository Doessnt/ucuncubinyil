"""
class student:
    info_students = "Bu sınıf kurstaki öğrenci işlemleri için var"
    adi = "Ali"
    soyadi = "Vardar"
    #cls: sınıfı temsil eder. Kullanılması zorunludur
    #Sınıf fonksiyonları
    def bilgiListele(cls):
        print("\nÖğrencilerin geneli ile ilgili bilgileri sınıf metotlarında listeleriz\n")
        print("Bu fonksiyonun kullanım amacı kurs müdürünün kullanacağı bir fonksiyon olabilir\n")
    

ogrenci = student()
ogrenci2 = student()
ogrenci.adi = "Ahmet"
ogrenci.soyadi = "kazma"

print(ogrenci.adi)
print(ogrenci2.adi)

# Nesne oluştururken ototmatik olarak çalışır 
# Aynı zmanda nesneye ait özellikleri burda tanımlarız

###__init__###
class cat():
    def __init__(self): 
        print("Hemen çalıştı!")
    def test(self):
        print("test")


whitcat = cat()
whitcat.test()


class student():
    def __init__(self):
        self.name = str()
        self.birtdate = str()
        self.calssinfo = 0
    def kaydet(self):
        print(self.name, self.calssinfo, self.birtdate, "veri tabanına h.o")
    

student1 = student()
student1.name = "Bruh"
student1.birtdate = "03/12/2003"
student1.calssinfo = 3
student1.kaydet()
print("\n", student1.name,"\n", student1.birtdate, "\n", student1.calssinfo)


### Recap ###


class kopkeler():
    # nitelikleri
    patiSayisi = 4
    kuyrukSayisi = 1
    def __init__(self):
        self.tuyrengi = str()
        self.agirlik = 0
        self.sosyallik = False
        self.gozrengi = str()
        self.cins = ""
        self.havlamasesi = "havhav"
    def havhav(self):
        print("\nHavlayan kopek:", self.cins, "\nHavlama sesi:", self.havlamasesi)

rot = kopkeler()

rot.tuyrengi = "siyah"
rot.gozrengi = "kahve"
rot.sosyallik = False
rot.cins = "rot"
rot.havlamasesi = "HAVHAVHAV!!!!"

#print("ROTUN AĞIRLIĞI: ", rot.agirlik,"ROTUN TUY RENGİ",  rot.tuyrengi, "Sosyelliği", rot.sosyallik)

golden = kopkeler()
golden.tuyrengi = "sarı-kahve"
golden.gozrengi = "kahve"
golden.sosyallik = True
golden.cins = "Golden"
golden.havlamasesi = "HavHav"

rot.havhav()
golden.havhav()


class arabalar():
    def __init__(self, Kapisayisi, Renk, Model, Yil):
        self.kapiSayisi = Kapisayisi
        self.renk = Renk
        self.model = Model
        self.yil = Yil

sahin = arabalar(4, "Renk", "Sahin", 2023)
mersedes = arabalar(2, "Siyah", "Mercedes AMG", 2020)
print(mersedes.model)

### polimorfizm ###
# Kalıtım #
# Miras işte amk anla


class workers():
    def __init__(self, isim, maas, department) -> None:
        print("Çalışan sınıfın __init__'i")
        self.isim = isim
        self.maas = maas
        self.department = department
    def show_info(self):
        print("----- Çalışan bilgileri... -----")
        print("İsim: {} \n Maaş: {} \n Departman: {}\n ".format(self.isim, self.maas, self.department))
    def switch_Department(self, new_department):
        print("Departman GG..")
        self.department = new_department

class Maneger(workers): # --> Kalıtım bu işte amk al 
    def do_zam(self, zam):
        print("Maaşa zam yapılıyor...")
        self.maas += zam

maneger1 = Maneger("Nesat", 50000, "Yonetici")
maneger1.do_zam(5000)
maneger1.show_info()



class Manager():
    def __init__(self, isim, maas, departman, sorumlu_olduğukişisayısı) -> None:
        print("__İNİT_ÇALIŞTI")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kişi_sayisi = sorumlu_olduğukişisayısı
    def show_info(self):
        print("Yönetici sınıfına ait bilgiler...")
        print("isim: {}\n, Maaş: {}\n, Kişi sayısı: {}".format(self.isim, self.maas, self.kişi_sayisi,))
    
class workers():
    def __init__(self, isim, maas, department) -> None:
        print("Çalışan sınıfın __init__'i")
        self.isim = isim
        self.maas = maas
        self.department = department
    def show_info(self):
        super().show_info()
        print("----- Çalışan bilgileri... -----")
        print("İsim: {} \n Maaş: {} \n Departman: {}\n ".format(self.isim, self.maas, self.department))
    def switch_Department(self, new_department):
        print("Departman GG..")
        self.department = new_department
    def do_zam(self, zam):
        print("Zam yapılıyoeda bi boka yaramıyacak haberin olsun xd")
        self.maas += zam


a = workers("Ali", 15000, "Sanayi")
a.show_info()
a.do_zam(15500)
a.show_info()




b = Manager("Ahmet", 10000, "Yönetici", 25)
b.show_info()


class muhendis():
    ad = "Sadi" # public bir değişken
    __soyad = "Kahveci" # priavet bir değişken
    def ekranayaz(self):
        print(self.ad) 
        print(self.__soyad)

muhendiss = muhendis()
print(muhendiss.__soyad)
muhendiss.ekranayaz()



class muhendis():
    ad = "Sadi" # public bir değişken
    __soyad = "Kahveci" # priavet bir değişken
    def __ekranayaz(self): # private fonksiyon
        print(self.ad) 
        print(self.__soyad)
    def __init__(self) -> None:
        self.__ekranayaz()

muhendiss = muhendis()



class muhendis():
    ad = "Sadi" # public bir değişken
    __soyad = "Kahveci" # priavet bir değişken
    def __ekranayaz(self): # private fonksiyon
        print(self.ad) 
        print(self.__soyad)
    def __init__(self) -> None:
        self.__ekranayaz()

class bilgisayar(muhendis):
    pass 

pcmuhendisi = bilgisayar()



# kapsulleme


class kapsul():
    def __init__(self) -> None:
        self.__ad = "FUCK YOU"
        self.__soyad = "FUCK YOU TOO"
    def getIsım(self):
        return self.__ad
    def setIsım(self, isim):
        if(len(isim)>30):
            print("Çok uzun bir isim girdiniz")
        else:
            self.__ad = isim



kapsull = kapsul()
print(kapsul.getIsım())
"""


























