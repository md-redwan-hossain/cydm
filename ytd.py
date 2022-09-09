from core import *


while True:
    print(colored.green(" CYDL: A CLI Based YouTube Video Downloader"))
    proceedOrNot = False
    link = regexCheck()
    if link:
        proceedOrNot = downloaderFunc(link)
    else:
        break
    if proceedOrNot:
        break
