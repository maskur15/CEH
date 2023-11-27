

import nmap 
print("<------------Nmap Scanner------------>")
ip=input('Enter the ip(Ex-10.0.2.15) you want to scan : ')
print('IP :',ip)
scanner = nmap.PortScanner()
print(scanner.scan(ip,'80'))

