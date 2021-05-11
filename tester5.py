import nmap
nm = nmap.PortScanner()

#TCP SYN (Stealth) Scan (-sS) &&  -O Enable OS detection
nm.scan(hosts='192.168.0.0/24', arguments='-sS -O') 
for host in nm.all_hosts():
    print(host)
print(nm.csv())