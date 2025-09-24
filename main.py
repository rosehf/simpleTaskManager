# Cadets Hayden Rose and Siripat Kotipapa
# CIS 302 - Simple Linux Task Manager
# Help Recieved: 

import time
import re

# Static Info
def get_static_info():
    with open("/proc/cpuinfo", 'r') as file:
        cpuinfo = file.read()
        print(re.search(r'model name\s+:\s+(.+)', cpuinfo))
    
    with open("/proc/version", 'r') as file:
        version = file.read()
        print(re.search(r'Linux version\s+(.+?)\s+', version))

    with open("/proc/meminfo", 'r') as file:
        meminfo = file.read()
        print(re.search(r'MemTotal:\s+(\d+)', meminfo))

    with open("/proc/uptime", 'r') as file:
        uptime = file.read()
        print(re.search(r'(\d+\.\d+)', uptime))
    




# Dynamic Montioring