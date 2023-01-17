import os 
import time

for i in range(5,0,-1): 
    print(i) 
    time.sleep(1)
    if i == 1:
        print("By By")
        os.system("shutdown /s /t 1")
