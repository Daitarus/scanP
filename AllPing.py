import os
import platform
import threading
from datetime import datetime

def scan_Ip(ip):
    addr = net + str(ip)
    comm = ping_com + addr
    response = os.popen(comm)
    data = response.readlines()
    for line in data:
        if 'TTL' in line:
            print(addr, "--> Ping Ok")
            break


net = "192.168.1."
start_point = int(input("Enter the Starting Number: "))
end_point = int(input("Enter the Last Number: "))

oc = platform.system()
if (oc == "Windows"):
    ping_com = "ping -n 1 "
else:
    ping_com = "ping -c 1 "

t1 = datetime.now()
print("Scanning in Progress:")

for ip in range(start_point, end_point):
    potoc = threading.Thread(target=scan_Ip, args=[ip])
    potoc.start()

potoc.join()
t2 = datetime.now()
total = t2 - t1

print("Scanning completed in: ", total)