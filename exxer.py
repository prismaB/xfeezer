#!/usr/bin/env python3
#start
import subprocess
import cmd
import sys
import os
import socket
from colorama import Fore,Back,Style,init
import cowsay
import time
import datetime
#start
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
def clearcreen():
    subprocess.call("clear")

def exploits():
    print("""
    1-exploit/windows/smb/windows_eternalblue_windows_7
    2-exploit/webapp/php/php-8.1.0-dev_remote_code_execution
    3-exploit/windows/smb/windows_eternalblue_windows_8
    4-exploit/webapp/ruby/Gitlab_13.9.3_remote_code_execution
    5-exploit/webapp/cms/magento_Unauthenticated_sql_injection
    6-exploit/webapp/Shellshock
    7-exploit/webapp/Apache_Struts_2_CVE-2013-2251
    8-exploit/webapp/apache_tomcat_exploit
    9-exploit/webapp/cms/codiac_remote_code_execution
    """)

def scanner():
    print("""
    s1-windows/eternalblue_scanner
    """)
def commands():
    command = """
        help = show the all commands
        show_exploits = show the all exploits
        use_exploit_menu = run the exploit menu
        clear = clear screen
        quit or exit command = exit the tool
        info = info the module
        edit = edit the module
        privesc = privesc tool start
        generate_trojan = GENERATE the virus
        version = show program version command
        coder = show the program authors
        discord = show the discord link
        multi_scanner = use the windows exploit scanner with nmap
        webmap = scan websites
        privesc = privesc exploit search
        """
    print(command)

#start class

class exxer(cmd.Cmd):
    prompt = 'xfeezer > '
    def do_EOF(self, line):
        print("bye!")
        sys.exit()
    def do_exit(self, line):
        sys.exit()
    def do_help(self, line):
        commands()
    def do_show_exploits(self, line):
        exploits()
    def do_use_exploit_menu(self, line):
        print("checking the exploit menu exploits")
        try:
            from os import path
            def errorcheckfile():
                print("folderfound")
            def foundcheckthefile():
                import sys
                print("folder found")
                sys.exit()
            
            #.
            patha = '/usr/share/xfeezer/exxer/'
            path.isdir(patha)
            if path.isdir(patha):
                errorcheckfile()
                import os
                os.system("python3 /usr/share/xfeezer/exxer/exploitmenu/exploits.py")
            else:
                foundcheckthefile()
        except KeyboardInterrupt:
            pass
    def do_clear(self, line):
        clearcreen()
    def do_coder(self, line):
        coders = """
        {1}-prisma
        """
        print(coders)
    def do_discord(self, line):
        invites = """
        https://discord.gg/3yHyzrSJ6x => winst
        https://discord.gg/sGr4FcNKP5 => penguin tux
        """
        print(invites)
    def do_webmap(self, line):
        try:
            from os import path
            pathfolder = '/usr/share/xfeezer/exxer/webmap/webmap.py'
            path.isfile(pathfolder)
            if path.isfile(pathfolder):
                print("folder found")
                os.system("python3 /usr/share/xfeezer/exxer/webmap/webmap.py")
            else:
                print("webmap menu not found")
        except:
            pass
    def do_multi_scanner(self, line):
        print("chekcing the folder")
        try:
            pathae = '/usr/share/xfeezer/exxer/windows/multiscanner/multi/'
            pathfileu = '/usr/share/xfeezer/exxer/windows/multiscanner/multi/multi.py'
            from os import path
            path.isdir(pathae)
            if path.isdir(pathae):
                print("folder found")
            else:
                print("folder not found")
            path.isfile(pathfileu)
            if path.isfile(pathfileu):
                print("file found")
                os.system("python3 /usr/share/xfeezer/exxer/windows/multiscanner/multi/multi.py")
            else:
                pass
        except:
            pass
    def do_generate_trojan(self,line):
        print("chekcing the folder")
        try:
            path1 = '/usr/share/xfeezer/exxer/generate/'
            from os import path
            path.isdir(path1)
            if path.isdir(path1):
                print("folder found")
                os.system("python3 /usr/share/xfeezer/exxer/generate/generate.py")
            else:
                print("folder not found")
        except:
            pass
    def do_privesc(self, line):
        os.system("python3 /usr/share/xfeezer/exxer/make/privesc.py")
if __name__ == '__main__':
    try:
        exxer().cmdloop()
    except KeyboardInterrupt:
        sys.exit()