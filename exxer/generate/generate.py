import os
import sys
import subprocess
import cmd
from os import path
def error(self):
    self.errorket = 'error'
    try:
        print(self.errorket)
    except:
        pass
def checkpversion():
    try:
        if sys.version_info < (3.9):
            pass
    except KeyboardInterrupt:
        error()
def clear():
    subprocess.call("clear")

def banner():
    file = '/usr/share/xfeezer/exxer/generate/banner/banner.txt'
    path.isfile(file)
    if path.isfile(file):
        try:
            print(file)
        except:
            pass
    else:
        pass
class make(cmd.Cmd):
    prompt = 'generate$ '
    clear()
    banner()
    try:
        menu = """
        {1}-windows
        {4}-other
        """
        print(menu)
    except:
        pass
    def do_exit(self, line):
        sys.exit()
    def do_1(self, line):
        self.generatedir = '/usr/share/xfeezer/exxer/generate/windows/'
        path.isdir(self.generatedir)
        self.generatefile = '/usr/share/xfeezer/exxer/generate/windows/windows.py'
        path.isfile(self.generatefile)
        if path.isdir(self.generatedir):
            os.system("python3 /usr/share/xfeezer/exxer/generate/windows/windows.py")
        else:
            print("file not found")
        if path.isfile(self.generatefile):
            os.system("python3 /usr/share/xfeezer/exxer/generate/windows/windows.py")
        else:
            print("file not found")
    def do_4(self, line):
        clear()
        banner()
        menus = """
        {1}-php reverse shell    {6}-perl reverse shell
        {2}-asp/x -reverse shell  {7}-python reverse shell
        {3}-jsp reverse shell      {8}-bash reverse shell
        {4}-war reverse shell
        {5}-node js reverse shell
        """
        print(menus)
        os.system("python3 /usr/share/xfeezer/exxer/generate/other/other.py")
if __name__ == '__main__':
    make().cmdloop()
    #asd