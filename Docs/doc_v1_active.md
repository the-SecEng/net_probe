<html>

<body>
  <pre>
  <h1>Net Probe</h1>

  <p>Net Probe is a Python program that allows you to scan all devices connected to your local network. It can identify the IP address of each device and determine if any ports are open, helping you to identify vulnerable devices and potential security risks.</p>

  <hr>

  <h2>Installation</h2>
  <p>To use Net Probe, you need to have Python 3 installed on your computer. Once you have Python 3 installed, you can download the <strong>net_probe.py</strong> file and run it from the command line.</p>

  <hr>

  <h2>Usage</h2>
  <p>To use Net Probe, simply run the <code>net_probe.py</code> file from the command line. The program will scan all devices connected to your local network and display their IP addresses and any open ports.</p>

  <p>You can modify the IP ranges that are scanned by changing the value of the <code>subnets</code> variable in the <code>main</code> function. By default, the program scans devices on the following subnets:</p>

  <ul>
    <li>192.168.0.0/16</li>
    <li>187.0.0.0/8</li>
  </ul>

  <p>The number after the slash in the IP address (e.g. <code>/16</code>) specifies the subnet mask. This determines how many bits in the IP address are used to identify the network and how many are used to identify the host. In the default configuration, the first 16 bits of the IP address are used to identify the network, and the remaining 16 bits are used to identify the host. This allows the program to scan all devices on the local network.</p>

  <p>If you change the subnet mask to a smaller value (e.g. <code>/24</code>), the program will only scan devices on the same local network as your computer. If you change it to a larger value (e.g. <code>/8</code>), the program will scan devices on a wider range of networks, but this will also increase the scanning time.</p>

  <hr>

  <h2>Features</h2>
  <p>Net Probe can scan devices on multiple subnets. It scans for open ports on the following common ports:</p>

  <ul>
    <li>21 (FTP)</li>
    <li>22 (SSH)</li>
    <li>23 (Telnet)</li>
    <li>25 (SMTP)</li>
    <li>53 (DNS)</li>
    <li>80 (HTTP)</li>
    <li>110 (POP3)</li>
    <li>143 (IMAP)</li>
    <li>443 (HTTPS)</li>
    <li>3306 (MySQL)</li>
    <li>3389 (Remote Desktop Protocol)</li>
    <li>5900 (Virtual Network Computing)</li>
    <li>8080 (HTTP alternate)</li>
  </ul>

  <p>Net Probe also generates a JSON file with the scan results, which can be used for further analysis.</p>

  <hr>

  <h1>Disclaimer</h1>
  <p><strong>Net Probe is intended to be used for white hat security testing and should only be used on networks that you have permission to test. Misusing Net Probe or using it for illegal activities is strictly prohibited.</strong></p>
