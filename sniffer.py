from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    """
    This function is called for each captured packet.
    It checks for IP and TCP layers and prints relevant info.
    """
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        print(f"IP Packet: {source_ip} -> {destination_ip}")

    if packet.haslayer(TCP):
        print(f"  -- TCP Packet: {packet.summary()}")

# --- Main Execution ---
# You may need to change the iface value to your network card (e.g., "eth0", "en0", "Wi-Fi")
INTERFACE = "eth0"
PACKET_COUNT = 10

print(f"[*] Sniffing on interface {INTERFACE}... Press Ctrl+C to stop.")
sniff(prn=packet_callback, iface=INTERFACE, count=PACKET_COUNT)

print("\n[*] Sniffing complete.")