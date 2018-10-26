import os
from time import sleep
def mymail():
    return
def takesnap():
        os.system("fswebcam -F 4 /home/dl107/h0007/temp.jpg")
        return
for i in range(10):
    takesnap()
    mymail()
    sleep(5)

