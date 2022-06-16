import os
import subprocess

def srcMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --src-ip", shell=True)
    return direct_output

def dstMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --dst-ip", shell=True)
    return direct_output

def srcPortMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --src-port", shell=True)
    return direct_output

def dstPortMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --dst-port", shell=True)
    return direct_output

def protoMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --proto", shell=True)
    return direct_output

def policyMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --policy", shell=True)
    return direct_output

def interfaceMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --interface", shell=True)
    return direct_output

def packetsMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --packets", shell=True)
    return direct_output

def bytesMetrics():
    direct_output=subprocess.check_output("python srx.py -f sessiontable.txt --bytes", shell=True)
    return direct_output