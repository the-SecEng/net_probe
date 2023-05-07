import socket  # For network communication
import threading  # For concurrency
import json  # For file input/output operations
import ipaddress  # For handling IP addresses


# Define a function to scan ports of an IP address
def scan_ports(ip_address, results):
    # List of commonly used ports
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 5900, 8080]
    open_ports = []  # List of open ports
    closed_ports = []  # List of closed ports

    # Iterate over the list of ports and try connecting to them
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip_address, port))  # Try connecting to the port
                print(f"{ip_address}:{port} is open")
                open_ports.append(
                    port
                )  # If connection succeeds, add port to open_ports list
        except (socket.timeout, ConnectionRefusedError):
            print(f"{ip_address}:{port} is closed")
            closed_ports.append(
                port
            )  # If connection fails, add port to closed_ports list

    # If any open/closed ports exist, add the info to the results dictionary
    if open_ports or closed_ports:
        results[ip_address] = {"OpenPorts": open_ports,
                               "ClosedPorts": closed_ports}


# Define the main function to start the port scanning
# It scans subnets for open ports and write the results to a JSON file.
def main():
    # subnets = ["192.168.0.0/16", "187.0.0.0/8"]    # Bigger Scan
    subnets = ["192.168.0.0/24"]  # List of subnets to scan
    threads = []
    results = {}

    # Iterate over the subnets and IP addresses to be scanned
    for subnet in subnets:
        for ip_address in ipaddress.IPv4Network(subnet):
            ip = str(ip_address)
            # Create a new thread for each IP address
            thread = threading.Thread(target=scan_ports, args=(ip, results))
            thread.start()  # Start the thread
            threads.append(thread)  # Add the thread to the threads list

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Write the results to a JSON file
    with open("scan_results.json", "w") as f:
        json.dump(results, f, indent=4)


# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
