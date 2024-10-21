# Net Probe
Net Probe is a Python program that allows you to scan all devices connected to your local network. It can identify the IP address of each device and determine if any ports are open, helping you to identify vulnerable devices and potential security risks.
<hr>
<h2> Installation </h2>
To use Net Probe, you need to have Python 3 installed on your computer. Once you have Python 3 installed, you can download the <strong>net_probe.py</strong> file and run it from the command line.
<br>
<h2> Usage </h2>
To use Net Probe, simply run the net_probe.py file from the command line. The program will scan all devices connected to your local network and display their IP addresses and any open ports.
<br>
<h2>Features</h2>
Net Probe can scan devices on multiple subnets, including <strong>192.168.0.0/16</strong> and <strong>187.0.0.0/8.</strong> It scans for open ports on the following common ports:

* 21 (FTP)
* 22 (SSH)
* 23 (Telnet)
* 25 (SMTP)
* 53 (DNS)
* 80 (HTTP)
* 110 (POP3)
* 143 (IMAP)
* 443 (HTTPS)
* 3306 (MySQL)
* 3389 (Remote Desktop Protocol)
* 5900 (Virtual Network Computing)
* 8080 (HTTP alternate)
<br>
Net Probe also generates a JSON file with the scan results, which can be used for further analysis.
<hr>
<h2>License</h2>
<strong>This program is licensed under the Apache 2.0 License. See the NOTICE and LICENSE file for more information.</strong>
