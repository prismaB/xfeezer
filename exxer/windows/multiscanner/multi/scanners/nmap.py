import os
import sys
import subprocess
import time
import self
class monke:
    def __init__(self):
        subprocess.call("clear")
        ip = sys.argv[1]
        print("ip =>" + " " + ip)
        time.sleep(1)
        print("starting the smb os discovery")
        self.smbdiscovery = 'nmap --script smb-os-discovery.nse -p445'
        os.system(self.smbdiscovery + " " + ip)
        print("starting the smb system info script")
        self.smbdscovery = 'nmap --script smb-system-info.nse -p445'
        print("starting the smb system info")
        os.system(self.smbdscovery + " " + ip)
        print("starting the crackmapexec smb discovery")
        self.smbcrackmapexec = '/usr/share/xfeezer/exxer/multi/scanners/crackmapexec.py'
        os.system("python3" + " " + self.smbcrackmapexec + " " + ip)
    __init__(self)
if __name__ == '__main__':
    monke()