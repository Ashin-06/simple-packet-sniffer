# Simple Packet Sniffer

A basic command-line network packet sniffing tool built with Python and the Scapy library. This script captures a limited number of packets on a specified network interface and displays key information about them.

## Features

* Captures a predefined number of network packets.
* Identifies IP packets and displays their source and destination addresses.
* Filters for TCP packets and prints a high-level summary.
* The network interface and packet count can be easily modified within the script.

## Technologies Used

* Python
* Scapy

## Setup and Usage

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Ashin-06/simple-packet-sniffer.git    
    cd simple-packet-sniffer
    ```

2.  **Install Dependencies:**
    This project requires the Scapy library.
    ```bash
    pip install scapy
    ```

3.  **Configure the Interface:**
    Before running, open the `sniffer.py` file and change the `INTERFACE` variable to match your system's network interface name (e.g., "eth0", "en0", "Wi-Fi").

4.  **Run the Script:**
    Packet sniffing requires root/administrator privileges.
    ```bash
    sudo python sniffer.py
    ```

## ⚖️ Disclaimer

This tool is for educational purposes only. Only use it on networks that you own or have explicit permission to monitor. Unauthorized packet sniffing is illegal.