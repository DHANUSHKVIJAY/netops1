import os
import subprocess

def srcPortMetrics():
    #os.system("python srx.py -f sessiontable.txt --src-ip 10 --dst-ip 10 --src-port 10 --dst-port 10 --proto 10 --policy 10 --interface 10 --packets 10 --bytes 10")
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --src-port 10", shell=True)
    print(direct_output)
    return direct_output