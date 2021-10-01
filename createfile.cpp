#include <iostream>
#include <unistd.h>

using namespace std;

int main()
{
    cout << "please run root \n";
    cout << "creating the folderss\n";
    cout << "please wait \n";
    system("mkdir /usr/share/xfeezer");
    cout << "created folders => /usr/share/xfeezer";
    system("mkdir /usr/share/xfeezer/exploits/");
    cout << "created folderss => /usr/share/xfeezer/exploits/ \n";
    system("mkdir /usr/share/xfeezer/exploits/webapp");
    cout << "created folderss => /usr/share/xfeezer/exploits/webapp/ \n";
    system("mkdir /usr/share/xfeezer/scanner/");
    cout << "created folder => /usr/share/xfeezer/scanner/ \n";
    system("mkdir /usr/share/xfeezer/scanner/exploitscanner");
    cout << "created folder => /usr/share/xfeezer/scanner/exploitscanner \n";
    system("mkdir /usr/share/xfeezer/scanner/exploitscanner/cve_scanner");
    cout << "created folder => usr/share/xfeezer/scanner/exploitscanner/cve_scanner \n";
    system("mkdir /usr/share/xfeezer/scanner/exploitscanner/webappscanners");
    cout << "created folder => /usr/share/xfeezer/scanner/exploitscanner/webappscanners \n";
    cout << "created all folder now checking the folders \n";
    cout << "now moving and checking files please run checkfiles.py \n";
    system("mkdir /usr/share/xfeezer/exxer/");
    cout << "created folder /usr/share/xfeezer/exxer/ \n";
    system("mkdir  /usr/share/xfeezer/other/banner/");
    system("mkdir /usr/share/xfeezer/exxer/windows/ && mkdir /usr/share/xfeezer/exxer/windows/multiscanner && mkdir /usr/share/xfeezer/exxer/generate/ && /usr/share/xfeezer/exxer/make && /usr/share/xfeezer/exxer/privesc");
    system("sudo bash command.sh");
}
