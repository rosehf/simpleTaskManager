# Cadets Hayden Rose and Siripat Kotipapa
# CIS 302 - Simple Linux Task Manager
# Help Recieved: Github Copilot for regex explaination, Canvas resources 

import time
import re

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

# Static Info
def get_static_info():
    print(RED + "SYSTEM INFO" + RESET)

    with open("/proc/cpuinfo", 'r') as file:
        cpuinfo = file.read()
        print("Processor Type:" + GREEN, re.search(r'model name\s+:\s+(.+)', cpuinfo).group(1))
    
    with open("/proc/version", 'r') as file:
        version = file.read()
        print(RESET + "Kernel Version:" + GREEN, re.search(r'Linux version\s+(.+?)\s+', version).group(1))

    with open("/proc/meminfo", 'r') as file:
        meminfo = file.read()
        print(RESET + "Total Memory:" + GREEN, re.search(r'MemTotal:\s+(\d+)', meminfo).group(1))

    with open("/proc/uptime", 'r') as file:
        uptime = file.read()
        print(RESET + "Uptime:" + GREEN, re.search(r'(\d+\.\d+)', uptime).group(1))
        
    
    




# Dynamic Montioring

#def monitor():
    

get_static_info()
