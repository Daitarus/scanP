import os
import platform
import threading
import socket

def scan_Ip(ip):
    addr = net + str(ip)
    commP = ping_com + addr
    responseP = os.popen(commP)
    dataP = responseP.readlines()
    for lineP in dataP:
        if 'TTL' in lineP:  
            addrP.append(addr)    
            break

def scan_Mac(ip):
    commA="arp /a "+ (ip)
    responseA = os.popen(commA)
    dataA = responseA.readlines()
    for lineA in dataA:
        if str(ip) in lineA:
            print(lineA)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

addrP=[]
print("Scan IP in LAN from 255.255.255.0 mask, v1.2")
oc = platform.system()
o = bool(1)
if (oc == "Windows"):
    ping_com = "ping -n 1 "
elif (oc=="Linux"):
    ping_com = "ping -c 1 "
else:
    o = bool(0)
    print("ERROR: Sript not for your system!")
if o:
    net = get_ip()
    print("Your IP: " + str(net))
    net_split=net.split('.')
    net = net_split[0] + '.' + net_split[1] + '.' + net_split[2] + '.'
    start_point = int(input("Enter the Starting Number: "))
    end_point = int(input("Enter the Last Number: "))
    print("Scanning in Progress:")

    for ip in range(start_point, end_point):
        thP = threading.Thread(target=scan_Ip, args=[ip])
        thP.start()
    thP.join()
    for i in range(len(addrP)):
        if addrP[i]==str(net):
            addrP.pop(i)
            break
    for i in range(len(addrP)):
        thA = threading.Thread(target=scan_Mac, args=[addrP[i]])
        thA.start()
    thA.join()   