import os
import datetime
"""

path = "C:\\Users\\202\\bruh"

zaman = datetime.datetime.now()
newname = zaman.strftime("%Y-%m-%d")

os.mkdir(path)

os.rename("bruh", newname)
"""

forlder_path = "C:\\Test\\test.txt"
for i in range(1, 11):
    formule = i ** 2
    folder = open(forlder_path, mode="a+")
    folder.write("{} sayısının karesi{} \n".format(i, formule))

folder.close()


