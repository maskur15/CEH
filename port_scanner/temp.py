

import nmap 
print("<------------Nmap Scanner------------>")
ip=input('Enter the ip(Ex-10.0.2.15) you want to scan : ')
print('IP :',ip)
scanner = nmap.PortScanner()
print(scanner.scan(ip,'80'))

{'nmap': {'command_line': 'nmap -oX - -p 80 -sV 10.0.2.15', 'scaninfo': {'tcp': {'method': 'connect', 'services': '80'}}, 'scanstats': {'timestr': 'Mon Nov 27 03:40:27 2023', 'elapsed': '19.68', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}}, 'scan': {'10.0.2.15': {'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '10.0.2.15'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'syn-ack'}, 'tcp': {80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'Apache httpd', 'version': '1.3.20', 'extrainfo': '(Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b', 'conf': '10', 'cpe': 'cpe:/a:apache:http_server:1.3.20'}}}}}

