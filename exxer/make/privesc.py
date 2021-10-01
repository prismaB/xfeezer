import os
import socket
import subprocess
import cmd
import sys


def menu():
    menu = """
    {2}-linux exploitation
    """
    print(menu)

class app(cmd.Cmd):
    prompt = 'privesc $=>'
    def do_2(self, line):
        try:
            os.system("python3 /usr/share/xfeezer/exxer/make/linux/linux.py")
        except KeyboardInterrupt:
            sys.exit()
if __name__ == '__main__':
    app().cmdloop()