import nmap
nm = nmap.PortScanner()

nm.scan(hosts='192.168.0.0/24', arguments='-sS -O')
for host in nm.all_hosts():
    print(host)
