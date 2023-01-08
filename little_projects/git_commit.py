import os 


def git_commit(folder = "",commit_word = "Sahibim buraya bir şey yazmaya üşendi"): #Burda ön tanımlı olarak gitin hata vermemesi için varsayılan bir bilgilendirme metni bıraktık.
    os.chdir(folder) # Burda dosya konumuna gittik .
    os.getcwd()# ufak kontrol .
    os.system("git add .") #Repoya dosyaları kayıt ettik.
    os.system(f'git commit -m "{commit_word}"') # repoya yazılıcak olan bilgilendirme metnini yazdık.
    os.system("git push") # en son repoya gönderdik. 


folder = input("Lütfen dosya dizinini giriniz\n >>>> ")

git_commit(folder)
    




