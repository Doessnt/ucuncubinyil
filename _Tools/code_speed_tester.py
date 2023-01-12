import datetime
import os





__all__ = ['sc_file',"speed_code",]

def sc_file():
    user_folder_path = input("Lütfen kodunuzun yazdığı dosya dizinini giriniz\n>>>> ")
    os.chdir(user_folder_path)
    user_folder_name = input("Lütfen dosya isimini uzantısyla yazınız\n>>>> ")


    user_folder = open(f"{user_folder_name}","r+")
    read = user_folder.read()
    script = read
    start = datetime.datetime.now()
    exec(script)
    finish = datetime.datetime.now()
    print(finish-start)




    


def speed_code(user):
    start = datetime.datetime.now()
    eval(user)
    finish = datetime.datetime.now()
    print(finish.microsecond-start.microsecond)




