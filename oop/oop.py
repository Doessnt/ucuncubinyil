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
"""

