from colorama import Fore,Back,Style,init
init(autoreset=True)
import os
from os import path
import requests
import sys
import time
if os.geteuid() != 0:
    exit("please run script on root account")
def animation():
    try:
        from tqdm import tqdm
        for i in tqdm(range(250)):
            pass
    except KeyboardInterrupt:
        print("exitting")
        sys.exit()
def checknetwork():
    r = requests.get('https://github.com/')
    if r.status_code == 200 or r.status_code == 404:
        print(Fore.GREEN + "connected network" + Fore.GREEN)
    else:
        print(Fore.RED + "NETWORK CONNECTİON NOT FOUND" + Fore.RED)
        sys.exit()
class checkfile:
    animation()
    checknetwork()
    checkfold1 = '/usr/share/xfeezer/'
    checkfold2 = '/usr/share/xfeezer/exploits/'
    checkfold3 = '/usr/share/xfeezer/exploits/webapp/'
    checkfold4 = '/usr/share/xfeezer/scanner/'
    checkfold5 = '/usr/share/xfeezer/scanner/exploitscanner/'
    checkfold6 = '/usr/share/xfeezer/scanner/exploitscanner/cve_scanner/'
    checkfold7 = '/usr/share/xfeezer/scanner/exploitscanner/webappscanners/'
    error_message = 'error'
    true_message = 'success'
    print("check started please wait")
    path.isdir(checkfold1)
    if path.isdir(checkfold1):
        print(Fore.GREEN + checkfold1 + Fore.GREEN + " " + "found")
        print(Fore.GREEN + "FOLDER FOUND CHECKİNG THE ALL FOLDERS" + Fore.GREEN)
        path.isdir(checkfold2)
        time.sleep(2)
        if path.isdir(checkfold2):
            print(Fore.GREEN + checkfold2 + Fore.GREEN + " " + "folder found" + Fore.GREEN)
        else:
            print(Fore.RED + "folder not found creating the folder" + Fore.RED)
            os.system("mkdir /usr/share/xfeezer/exploits/")
    path.isdir(checkfold3)
    if path.isdir(checkfold3):
        print(Fore.GREEN + "folder found" + " " + checkfold3 + " " + Fore.GREEN)
        time.sleep(1)
    else:
        print(Fore.RED + "Folder not found" + " " + checkfold3 + Fore.RED)
        print(Fore.RED + "creating folder" + Fore.RED)
        os.system("mkdir " + " " + checkfold3)
    path.isdir(checkfold4)
    if path.isdir(checkfold4):
        print(Fore.GREEN + "folder found" + " " + checkfold4 + " " + Fore.GREEN)
        time.sleep(1)
    else:
        print(Fore.RED + "FOLDER NOT FOUND CREATİNG THE FOLDER" + Fore.RED)
        os.system("mkdir" + " " + checkfold4)
    path.isdir(checkfold5)
    if path.isdir(checkfold5):
        print(Fore.GREEN + "FOLDER FOUND" + " " + checkfold5 + Fore.GREEN)
        time.sleep(1)
    else:
        print(Fore.RED + "FOLDER NOT FOUND" + Fore.RED + " " + checkfold5 + Fore.RED)
        print(Fore.RED + "creating the folder" + Fore.RED)
        os.system("mkdir" + " " + checkfold5)
    path.isdir(checkfold6)
    if path.isdir(checkfold6):
        print(Fore.GREEN + "FOLDER FOUND" + " " + checkfold6 + Fore.GREEN)
        time.sleep(1)
    else:
        print("folder not found")
        # artik fore more sıktı
        print("folder creating")
        os.system("mkdir" + " " + checkfold6)
    path.isdir(checkfold7)
    if path.isdir(checkfold7):
        print(Fore.GREEN + "folder found" + " " + checkfold7 + " " + Fore.GREEN)
        os.system("python3 xfeezer.py")
    else:
        print("folder not found")
        os.system("mkdir" + " " + checkfold7)
    #check folder finish
if __name__ == '__main__':
    os.system("python3 exxer.py")