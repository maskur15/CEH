
import nmap 
from ping3 import ping 
def isHostUp(ip):
	try:
		result = ping(ip,timeout=1) #ping to check whether the host is up or not 
		if result is not None:
			return True 
	except Exception as e :
		print('Host is Down : ',e)
	return False  
print("<------------Nmap Scanner------------>")
ip=input('Enter the ip(Ex-10.0.2.15) you want to scan : ')
print('IP :',ip)


if isHostUp(ip):
	start=int(input('Enter the start port: '))
	end = int(input('Enter the end port : '))
	scanner = nmap.PortScanner()
	for port in range(start,end+1):
		result = scanner.scan(ip,str(port))
		if result['scan'][ip]['tcp'][port]['state']=='open':
			print(port , result['scan'][ip]['tcp'][port])

	#print(scanner.scan(ip,'10'))
else:
	pass

