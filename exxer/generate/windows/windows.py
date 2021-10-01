import os
import sys
import subprocess
import cmd

import pyfiglet

def clear():
    subprocess.call("clear")
def banner():
    try:
        import pyfiglet
        figlet = pyfiglet.figlet_format("windows")
        print(figlet)
    except ImportError:
        print("please install the pyfiglet")
def menus():
    menus = """
    {1}-reverse shell
    {2}-bind shell
    {3}-create user
    """
    print(menus)
class app(cmd.Cmd):
    prompt = 'windows$ '
    clear()
    banner()
    menus()
    def do_1(self, line):
        os.system("ruby /usr/share/xfeezer/exxer/generate/windows/reverse/reverse.rb")
    def do_2(self, line):
        os.system("ruby /usr/share/xfeezer/exxer/generate/windows/bind/bind.rb")
    def do_3(self, line):
        os.system("ruby /usr/share/xfeezer/exxer/generate/windows/create/create.rb")

if __name__ == '__main__':
    app().cmdloop()