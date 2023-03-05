import nmap

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-v 127.0.0.1') # Scan all ports
    open_ports = []
    for port in nm[target]['tcp'].keys():
        if nm[target]['tcp'][port]['state'] == 'open':
            open_ports.append(port)
    result = open_ports

    return result

target_ip = '127.0.0.1' # Replace with your target IP address
# open_ports = scan_ports(target_ip)
