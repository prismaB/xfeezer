import requests
import os
import sys
import cmd

class select(cmd.Cmd):
    menu = """
    {1}-wordpress brute force
    [99]-exit
    """
    print(menu)
    def do_1(self, line):
        self.command = '/usr/share/xfeezer/exxer/webmap/cms/wordpressbrute.py'
        os.system("python3" + " " + self.command)
    def do_2(self, line):
        self.command2 = '/usr/share/xfeezer/exxer/webmap/cms/wordpressdirectorysearch.py'
        os.system("python3" + " " + self.command2)
    def do_3(self, line):
        self.command3 = '/usr/share/xfeezer/exxer/webmap/cms/joomlascan.py'
        os.system("python3" + " " + self.command3)
    def do_99(self, line):
        sys.exit(1)
if __name__ == '__main__':
    select().cmdloop()