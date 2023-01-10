
import os
import datetime
"""

path = "C:\\Users\\202\\bruh"

zaman = datetime.datetime.now()
newname = zaman.strftime("%Y-%m-%d")

os.mkdir(path)

os.rename("bruh", newname)


forlder_path = "C:\\Test\\test.html"
for i in range(1, 11):
    formule = i ** 2
    folder = open(forlder_path, mode="a+")
    folder.write("{} sayısının karesi{} \n".format(i, formule))

folder.close()
"""


folder_path = "C:\\Test\\test.txt"
folder = open(folder_path, mode= "a+")

user_input1 = input("Lütfen sayı giriniz")
user_input2 = input("Lütfen sayı giriniz")
for i in range(user_input1, user_input2+1):
    folder.write(str(i) + "\n")
folder.close()