try:
    import os
    import sys
    import time
    from os import path
    import subprocess
    from colorama import Fore,Back,Style,init
except ImportError:
    pass
def clear():
    subprocess.call("clear")
def banner():
    bannerlocation = '/usr/share/xfeezer/exxer/windows/multiscanner/banner/banner.txt'
    path.isfile(bannerlocation)
    if path.isfile(bannerlocation):
        system("cat" + " " + bannerlocation)
    else:
        print("banner not found")
        time.sleep(1)
        subprocess.call("clear")
        animation()
def animation():
    init(autoreset=True)
    #coded by prisma
    #coded by anıl
    bred = Fore.GREEN + Style.BRIGHT
    z = """
                        Version 4.0.0
            [+] █████████████████████████████████████████████████████ [+]
                        Coded by github.com/prismaB/exxer\n\n
    """
    for c in z:
        sys.stdout.write(f"{bred}{c}")
        sys.stdout.flush()
        time.sleep(0.02)
class multiscanner:
    clear()
    banner()
    ip = input("add ip adress => ")
    os.system("python3 /usr/share/xfeezer/exxer/windows/multiscanner/multi/scanners/nmap.py" + " " + ip)

if __name__ == "__main__":
    multiscanner()