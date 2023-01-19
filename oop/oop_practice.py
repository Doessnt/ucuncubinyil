import ast
import os
"""
class shcool():
    def __init__(self):
        self.name = str()
        self.sınıfSayısı = 0
        self.ogrenciSayisi = 0
        self.okulRengi = "Beyaz"
    def zil(self):
        print(f"{self.sınıfSayısı}, {self.ogrenciSayisi}, {self.okulRengi}, {self.name} için iftar vakti")

sisli = shcool()
sisli.sınıfSayısı = 15
sisli.ogrenciSayisi = 15*10
sisli.name = "A/1"
sisli.zil()

class ders():
    def __init__(self, dersAdi, dersSaati, dersOgretmeni,dersBaslamaTarihi):
        self.dersadi = dersAdi
        self.derssaati = dersSaati
        self.dersOgretmen = dersOgretmeni
        self.dersbt = dersBaslamaTarihi
    def kaydet(self):
        asd = self.dersadi+self.derssaati+self.dersOgretmen+self.dersbt
        os.mkdir("C:\\Dersler")
        path = "C:\\Dersler\\Dersler.txt"
        dersler = open(path, mode = "a+")
        dersler.write(asd)
        dersler.close()

python = ders("Python", "1350", "Doğkan", "14122033") 

ders.kaydet(python)
"""
class car():
    def bilgi_goster(self):
        print("HİTLER WAS RİGHT")
        print("HİTLER WAS RİGHT")
        



class Mersedes(car):
    def __init__(self, isim, model, fiyat) -> None:
        self.isim = isim
        self.model = model 
        self.fiyat = fiyat
    def bilgi_goster(self):
        print(f"{self.isim}'in bilgileri")
        print(f"İsim = {self.isim}, Model = {self.model}, Fiyat = {self.fiyat}")


class Aston_Martin(car):
    def __init__(self, isim, model, fiyat) -> None:
        self.isim = isim
        self.model = model 
        self.fiyat = fiyat
    def bilgi_goster(self):
        print(f"{self.isim}'in bilgileri")
        print(f"İsim = {self.isim}, Model = {self.model}, Fiyat = {self.fiyat}")
        
class Honda(car):
    def __init__(self, isim, model, fiyat) -> None:
        self.isim = isim
        self.model = model 
        self.fiyat = fiyat
    def bilgi_goster(self):
        print(f"{self.isim}'in bilgileri")
        print(f"İsim = {self.isim}, Model = {self.model}, Fiyat = {self.fiyat}")

honda = Honda("Honda", "civic", 500000)
merso = Mersedes("Mersedes", "AMG", 1000000)
aston = Aston_Martin("Aston Martin", "db5", 5000000)
merso.bilgi_goster()
print("\n")
honda.bilgi_goster()
print("\n")

aston.bilgi_goster()