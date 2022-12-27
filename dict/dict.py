# Sözlük oluşturma
# "Key":"Value","Key":"Value"
"""
sozluk = {"Color1":"Red", "Color2":"White", "Color3": "Blue"}

print(sozluk["Color1"])
 
print(sozluk.get(["Color1"]))
"""

sozluk = {"1":"Ahmet", "2": "Bartu", 3:5}

print(sozluk.items()) # Sözlük içeriğini gösterir
print(sozluk.keys()) # sözlük anahtar kelimelerini gösterir
print(sozluk.values()) # Sözlük içindeki değerleri gösterir
print(len(sozluk))
print("1" in sozluk) # Keyleri içinde "1" var mı ?
print("Ahmet" in sozluk.values()) # Değerlerin içinde "Ahmet" varmı ?

sozluk["11"] = "Eylül"
print(sozluk)

