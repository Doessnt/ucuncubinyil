import os
import datetime


path = "C:\\Users\\202\\bruh"

zaman = datetime.datetime.now()
newname = zaman.strftime("%Y-%m-%d")

os.mkdir(path)

os.rename("bruh", newname)
