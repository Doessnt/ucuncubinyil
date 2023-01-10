from os import *
"""
open() dosya açar
system()
getcwd() olduğunuz klasörü gösterir
chdir() klosörler arası gezinme
listdir() klasör içeriğini listeler
mkdir() Dosya oluşturur.


from os import *
print("Hangi klasördeyiz\n", getcwd())
chdir("C:\\")
print("Hangi klasördeyiz\n", getcwd())

klasor = "C:\\Users\\202\Desktop\\ucuncubinyil\\bruh"

klasor2 = path.exists(klasor)

if klasor2 == False:
    mkdir(klasor)
    print("Aç")
else:
    print("Var amk")

# belirtilen dizindeki dosya klasör isimlerini listele

path = "C:\\test\\"

folederlist = listdir(path)

for i in folederlist:
    print(i)


import os
# Belirtilen dizindeli dosyaya ekleme yapma
folder_path = "C:\\Test\\bruh.txt"


folder = open(folder_path, mode="a+")
folder.write("Hello World!")
folder.close()
"""

# Hesap makinesi açma
import os
#command = "calc"
#os.system(command)
# what's the pc name
pcName = os.system("hostname")
os.system("ipconfig")