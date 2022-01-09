import platform
import subprocess
host="192.168.1.5"
if platform.system().lower()=='windows': param = '-n'
else: param ='-c'
command = ['ping', '-a', param, '1', host]
if subprocess.call(command) == 0:
    print(host + " up")
else:
    print(host + " down")