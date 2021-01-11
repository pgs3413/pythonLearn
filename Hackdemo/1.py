import os
import random
from time import sleep
os.system('color 2')
index=1
while True:
    print(random.randrange(0,2),end="")
    index+=1
    if index==100 :
        index=1
        sleep(0.1)
        print()
