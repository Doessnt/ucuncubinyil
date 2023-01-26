import sqlite3

db = sqlite3.connect("C:\\Users\\202\\Desktop\\ucuncubinyil.py\\sql\\database\\TEST.db")

cursor = db.cursor()

#cursor.execute("Kodlar burda çalışır")
"""
try:
# Veri tabanı oluşturma
 command = "INSERT INTO ders (Name, soyad, numara) VALUES('ADOLF', 'HİTLER', '911') " # VERİ TABANINA KAYIT

 cursor.execute(command)

 db.commit() # Yazdığımız komudu işle
 print("Kayıt işi bendeeeeeeeeee :P")
except:
    print("KNK AYNI NUMARA OLMAZ")

db.close() # db kapama

for i in range(3):
    user_name = input("Lütfen giriniz")
    user_surname = input("Lütfen soyad")
    user_number = input("Lütfen number")

    command = f"INSERT INTO ders (Name, soyad, numara) VALUES('"+user_name+", "+user_surname+","+user_number+"')"
    cursor.execute(command)
    db.commit() # Yazdığımız komudu işle

db.close() # db kapama

# veri okuma

def getders():
    students = list()
    try:
        komut = "SELECT * FROM ders"
        cursor.execute(komut)
        students = cursor.fetchall() # tüm kayıtları listeye atar
    except:
        print("HATA")
    print(students)

getders()

try:
    komut = "SELECT * FROM ders"
    cursor.execute(komut)
    while True:
        recorde = cursor.fetchone()
        if recorde == None:
            break
        else:
            print(recorde)
except:
    print("NN")
"""
# veri tabanında silme işlemi
# Kullanıcı numarası ile kayıt sileme

silineceknumara = input("Lütfen yazın\n >>>>")

komut = "DELETE FROM ders WHERE numara = "+ silineceknumara
try:
    cursor.execute(komut)
    db.commit()
except:
    print("HATAAAAA")