import os 
import time

def git_commit(folder = "",commit_word = "Sahibim buraya bir şey yazmaya üşendi"): #Burda ön tanımlı olarak gitin hata vermemesi için varsayılan bir bilgilendirme metni bıraktık.
    os.chdir(folder) # Burda dosya konumuna gittik .
    os.getcwd()# ufak kontrol .
    os.system("git add .") #Repoya dosyaları kayıt ettik.
    time.sleep(1)
    print("Dosyalar repoya eklendi\n")
    time.sleep(1)
    os.system(f'git commit -m "{commit_word}"') # repoya yazılıcak olan bilgilendirme metnini yazdık.
    print(f"Commit edildi. Bilgilendirme metni {commit_word}")
    time.sleep(1)
    os.system("git push") # en son repoya gönderdik.
    time.sleep(1)
    print("Repoya gönderildi.") 


folder = input("Lütfen dosya dizinini giriniz\n >>>> ")

git_commit(folder)
    




