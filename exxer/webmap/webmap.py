import os
import requests
import subprocess
from colorama import Fore,Style,init,Back
import socket
import sys
import cmd

class frames(cmd.Cmd):
    prompt = 'Webmap$ '
    menu = """
    {1}-cms scanning
    [99]-exit
    """
    print(menu)
    def do_1(self, line):
        self.cmd1 = '/usr/share/xfeezer/exxer/webmap/cms/cmshacking.py'
        os.system("python3" + " " + self.cmd1)
    def do_99(self, line):
        sys.exit(1)
if __name__ == "__main__":
    frames().cmdloop()