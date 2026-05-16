import platform
import socket
import os
import subprocess

def get_machine_info():
    # 1. Get Machine Name
    # We try to get the host name passed from Docker, otherwise use socket
    name = os.environ.get('HOST_MACHINE_NAME', socket.gethostname())
    
    # 2. Detect Machine Type (Heuristic)
    m_type = "Desktop"
    
    try:
        # Check if running in a VM (common vendors)
        # We look at dmesg or other logs if possible, but inside docker we check /proc/cpuinfo
        with open('/proc/cpuinfo', 'r') as f:
            cpuinfo = f.read().lower()
            if 'hypervisor' in cpuinfo or 'vmware' in cpuinfo or 'qemu' in cpuinfo:
                m_type = "Virtual Machine"
        
        # Check for battery (Clue for Laptop)
        # In Linux (Docker), battery info is in /sys/class/power_supply/
        if os.path.exists('/sys/class/power_supply/'):
            supplies = os.listdir('/sys/class/power_supply/')
            if any('BAT' in s for s in supplies):
                m_type = "Laptop"
                
    except:
        pass
        
    return f"{name} ({m_type})"

if __name__ == "__main__":
    print(get_machine_info())
