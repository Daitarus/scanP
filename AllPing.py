import os
host = "192.168.1.1"
if os.name=="nt":
    response = os.system("ping -n 1 " + host)
else:
    response = os.system("ping -c 1 " + host)

if response == 0:
  print(host + ' is up!')
else:
  print(host +' is down!')