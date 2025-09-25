# Cadets Hayden Rose and Siripat Kotipapa
# CIS 302 - Simple Linux Task Manager
# Help Recieved: AI for questions about proc files, google for python syntax, Canvas resources 

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
        print(f"Processor Type:{GREEN}", re.search(r'model name\s+:\s+(.+)', cpuinfo).group(1))
    
    with open("/proc/version", 'r') as file:
        version = file.read()
        print(f"{RESET}Kernel Version:{GREEN}", re.search(r'Linux version\s+(.+?)\s+', version).group(1))

    with open("/proc/meminfo", 'r') as file:
        meminfo = file.read()
        print(f"{RESET}Total Memory:{GREEN}", re.search(r'MemTotal:\s+(\d+)', meminfo).group(1))

    with open("/proc/uptime", 'r') as file:
        uptime = file.read()
        print(f"{RESET}Uptime:{GREEN}", re.search(r'(\d+\.\d+)', uptime).group(1))
        
    

# Dynamic Montioring
#    Get percentage of time spend in user mode system mode and idle *STAT*
#    Amount and percentage of available memory *MEMINFO*
#    The rate of disk read/write in the system *DISKSTATS*
#    The rate of context switches in the kernel *STAT*
#    The rate of process creations in the system *STAT*

def monitor():
    print("\n" * 100)  # Clear screen
    print(RED + "DYNAMIC SYSTEM MONITOR " + RESET)
    print("Press Ctrl+C to stop monitoring\n")

    print("CPU percentages\n\tUser Mode: \n\tSystem Mode: \n\tIdle: ")
    print("Memory\n\tAvailable Memory: ")
    print("Disk I/O\n\tRead Rate: \n\tWrite Rate: ")
    print("Context Switches Rate: ")
    print("Process Creation Rate: ")

    while True:
        with open("/proc/stat", 'r') as stat:
            line = stat.readline().strip() # We use strip here to remove any whitespace around it
            fields = line.split()
            
            user_time = int(fields[1]) + int(fields[2])
            system_time = int(fields[3])
            idle_time = int(fields[4])
            total_time = user_time + system_time + idle_time

            user_percentage = (user_time / total_time) * 100
            system_percentage = (system_time / total_time) * 100
            idle_percentage = (idle_time / total_time) * 100

            print("\033[1A" * 10, end="")  # Move cursor up to overwrite previous output
            print(f"CPU percentages\n\tUser Mode: {GREEN}{user_percentage:.2f}%{RESET}\n\tSystem Mode: {GREEN}{system_percentage:.2f}%{RESET}\n\tIdle: {GREEN}{idle_percentage:.2f}%{RESET}")
            

        with open("/proc/meminfo", 'r') as meminfo:
            print()
        
        with open("/proc/diskstats", 'r') as diskstats:
            print()
        
        time.sleep(5)



   
        





monitor()
