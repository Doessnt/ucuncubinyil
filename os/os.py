import os

"""
open() dosya açar
system()
getcwd() olduğunuz klasörü gösterir
chdir() klosörler arası gezinme
listdir() klasör içeriğini listeler
mkdir() Dosya oluşturur.

"""
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