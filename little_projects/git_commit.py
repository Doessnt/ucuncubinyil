import os 


def git_commit(folder,commit_word = "Sahibim buraya bir şey yazmaya üşendi"):
    folder = input("Lütfen dosya dizinini giriniz\n >>>> ")
    os.chdir(folder)
    os.getcwd()
    os.system("git add .")
    os.system(f'git commit -m "{commit_word}"')
    os.system("git push")


folder = input("Lütfen dosya dizinini giriniz\n >>>> ")

git_commit(folder)
    




