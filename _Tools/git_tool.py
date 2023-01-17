import os 
import time

def git_configer(user_name = "Hpcodecraftt", user_email="hpcodecraftt@gmail.com"):
    try:
        os.system(f'git config --global user.name "{user_name}"')
        time.sleep(2)
        print("User name girildi şimdi")
        time.sleep(2)
        print("Şimdi emailinizi güncelliyorum")
        os.system(f'git config --global user.email "{user_email}"')
        time.sleep(2)
        print("Kontrol yapıyoruz\n")
        time.sleep(2)
        print("Git isiminiz", os.system("git config --global user.name"))
        print("Git mailiniz", os.system("git config --global user.email"))

        print("İşleminiz tamamlandı. İyi kodlamalar :)")
        time.sleep(2)
        
    except:
        print("Bir hata oluştu")






def git_commit(folder = "",commit_word = "Sahibim buraya bir şey yazmaya üşendi"): #Burda ön tanımlı olarak gitin hata vermemesi için varsayılan bir bilgilendirme metni bıraktık.
    folder = input("Lütfen dosya dizinini giriniz\n >>>> ")
    commit_word = input("Lütfen Bilgilendirme metnini yazınız\n >>>>")
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



    

def main_script():
    while True:
        user = int(input("""
            1- Git config ayarlama
            2- Git commit ve push
            3- Çıkış
        """))
        if user == 1:
            git_configer()
        elif user == 2:
            git_commit()
        elif user == 3:
            break
        else:
            print("Adam akıllı bir seçim yaap canımı sıkma")
        

main_script()


























