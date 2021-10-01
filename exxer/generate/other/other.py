import cmd
import os
import sys 
import subprocess
from os import path
def clear(self):
    self.clear = 'clear'
    subprocess.call(self.clear)
def baner():
    menus = """
    {1}-php reverse shell    {6}-perl reverse shell
    {2}-asp/x -reverse shell  {7}-python reverse shell
    {3}-jsp reverse shell      {8}-bash reverse shell
    {4}-war reverse shell
    {5}-node js reverse shell
        """
    print(menus)

def banner(self):
    self.banner = '/usr/share/xfeezer/exxer/generate/banner/banner.txt'
    path.isfile(self.banner)
    if path.isfile(self.banner):
        os.system("cat" + " " + self.banner)
    else:
        pass
def checkpy():
    if sys.version_info < (3,9):
        pass
class app(cmd.Cmd):
    clear()
    banner()
    baner()
    prompt = 'generateothers =>'
    def do_exit(self, line):
        sys.exit()
    def do_1(self, line):
        self.prof = '/usr/share/xfeezer/exxer/generate/php/php.py'
        path.isfile(self.prof)
        if path.isfile(self.prof):
            os.system("python3" + " " + self.prof)
        else:
            print("file not found")
    def do_2(self, line):
        self.proc = '/usr/share/xfeezer/exxer/generate/aspx/aspx.py'
        path.isfile(self.proc)
        if path.isfile(self.proc):
            os.system("python3" + " " + self.proc)
        else:
            print("file not found")
    def do_3(self, line):
        self.proq = '/usr/share/xfeezer/exxer/generate/jsp/jsp.py'
        path.isfile(self.proq)
        if path.isfile(self.proq):
            os.system("python3" + " " + self.proq)
        else:
            pass
    def do_4(self, line):
        self.prok = '/usr/share/xfeezer/exxer/generate/war/war.py'
        path.isfile(self.prok)
        if path.isfile(self.prok):
            os.system("python3" + " " + self.prok)
        else:
            pass
    def do_5(self, line):
        self.prot = '/usr/share/xfeezer/exxer/generate/nodejs/node.py'
        path.isfile(self.prot)
        if path.isfile(self.prot):
            os.system("python3" + " " + self.prot)
        else:
            pass
    def do_6(self, line):
        self.prop = '/usr/share/xfeezer/exxer/generate/perl/perl.py'
        path.isfile(self.prop)
        if path.isfile(self.prop):
            os.system("python3" + " " + self.prop)
        else:
            pass
    def do_7(self, line):
        self.python = '/usr/share/xfeezer/exxer/generate/python/python.py'
        path.isfile(self.python)
        if path.isfile(self.python):
            os.system("python3" + " " + self.python)
        else:
            print("file not found")
    def do_8(self, line):
        self.bash = '/usr/share/xfeezer/exxer/generate/bash/bash.py'
        path.isfile(self.bash)
        if path.isfile(self.bash):
            os.system("python3" + " " + self.bash)
        else:
            pass
if __name__ == '__main__':
    app().cmdloop()