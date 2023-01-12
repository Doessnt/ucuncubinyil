### Try - Catch ###

"""
try:
    Hata oluşturma ihtimali olan kodlar
except:
    Hata oluştuğunda çalışıcak komut



# for example:
try:
    number = int(input("Lütfen sayı alayım \n>>>> "))
except:
    print("Lütfen sayıyı giriniz!!!!!")

while True:
    try:
        number = int(input("Lütfen sayı alayım \n>>>> "))
        break
    except:
        print("Sayıyı doğru gir artık amk")

print(f"girdiğiniz sayı {number}")


while True:
    try:
        number = int(input("Lütfen sayı alayım \n>>>> "))
        break
    except ValueError:
        print("Sayı gir amk")
    except MemoryError:
        print("Fakir oç")


try:
    import os
except ImportError:
    print("None")

sayi1 = 10
sayi2 = 0

try: 
    bolum = sayi1/sayi2
except:
    print("sıfır olmaz")
"""
"""
ValueError: veri tipi uymadığında
ImportError: İçeri aktarırken modülde bir hata olursa 
ModuleNotFoundError: içeri katarılmaya çalışılan modül yerinede yoksa
MemoryError: Bellek yetersiz olduğunda
OverflowError: Bir değişkene verilmesi gereken fazla sayı verildiğinde 
IndexError: olmayan elemanı çağırdığımızda 


### Error trowing (raise) ###

not1 = int(input("Lütfen not veriniz"))

if not1 < 0 or not1 > 100:
    raise Exception("Not aralığı hatalı")
# Assert iddia etmek anlımına gelir #

eposta = input("Lütfen e-posta alayım")

assert eposta == "sivasli@gmail.com"

print("Gel içeri")
"""

















