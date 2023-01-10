import os 
import time

def git_commit(folder = "",commit_word = "Sahibim buraya bir şey yazmaya üşendi"): #Burda ön tanımlı olarak gitin hata vermemesi için varsayılan bir bilgilendirme metni bıraktık.
    os.chdir(folder) # Burda dosya konumuna gittik .
    os.getcwd()# ufak kontrol .
    os.system("git add .") #Repoya dosyaları kayıt ettik.
    time.sleep(2)
    print("Dosyalar repoya eklendi\n") #Bilgilendirmeler 
    time.sleep(2)
    os.system(f'git commit -m "{commit_word}"') # repoya yazılıcak olan bilgilendirme metnini yazdık.
    print("\n\n")
    print(f"Commit edildi. Bilgilendirme metni: '{commit_word}'") #Bilgilendirmeler 
    time.sleep(2)
    os.system("git push") # en son repoya gönderdik.
    time.sleep(2)
    print("Repoya gönderildi.") 


folder = input("Lütfen dosya dizinini giriniz\n >>>> ")
commit_word = input("Lütfen Bilgilendirme metnini yazınız\n >>>>")

git_commit(folder, commit_word)
    




