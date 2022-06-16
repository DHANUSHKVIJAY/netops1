import os
import subprocess
import matplotlib.pyplot as plt

def srcMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --src-ip", shell=True)
    return direct_output

def dstMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --dst-ip", shell=True)
    return direct_output

def srcPortMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --src-port", shell=True)
    return direct_output

def dstPortMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --dst-port", shell=True)
    return direct_output

def protoMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --proto", shell=True)
    return direct_output

def policyMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --policy", shell=True)
    return direct_output

def interfaceMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --interface", shell=True)
    return direct_output

def packetsMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --packets", shell=True)
    return direct_output

def bytesMetricsall():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt -n 99999 --bytes", shell=True)
    return direct_output