import os

try:
    os.system("mv /home/" + os.getuid + " " + "xfeezer/ /usr/share/")
    os.system("pip3 install -r /usr/share/xfeezer/requiremets.txt")
    print("run python3 /usr/share/xfeezer/exxer.py")
except:
    pass
