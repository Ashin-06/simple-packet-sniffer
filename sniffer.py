"""A small, readable network packet sniffer built with Scapy.

It captures a handful of packets on a network interface and prints one line per packet
showing the source and destination and the protocol. Read-only: it only observes
traffic. Capturing live traffic needs administrator/root privileges.

    sudo python sniffer.py --interface eth0 --count 10
    python sniffer.py --selftest        # parse built-in packets, no privileges needed
"""
from __future__ import annotations

import argparse
import sys

from scapy.all import IP, TCP, UDP, Ether, sniff


def summarize(packet) -> str:
    """One line describing a packet: source -> destination and protocol."""
    if packet.haslayer(IP):
        proto = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "IP"
        return f"{packet[IP].src} -> {packet[IP].dst}  [{proto}]"
    return packet.summary()


def selftest() -> int:
    examples = [
        IP(src="10.0.0.1", dst="10.0.0.2") / TCP(),
        IP(src="10.0.0.2", dst="8.8.8.8") / UDP(),
        Ether() / b"not an IP packet",
    ]
    lines = [summarize(p) for p in examples]
    for line in lines:
        print(line)
    assert lines[0] == "10.0.0.1 -> 10.0.0.2  [TCP]"
    assert lines[1] == "10.0.0.2 -> 8.8.8.8  [UDP]"
    print("self-test passed")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Capture and print a few network packets (read-only).")
    parser.add_argument("-i", "--interface", help="interface to capture on, e.g. eth0 or Wi-Fi")
    parser.add_argument("-c", "--count", type=int, default=10, help="number of packets to capture (default: 10)")
    parser.add_argument("--selftest", action="store_true", help="parse built-in packets and exit")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    print(f"Sniffing {args.count} packet(s) on {args.interface or 'the default interface'}... Ctrl+C to stop.")
    try:
        sniff(prn=lambda p: print(summarize(p)), iface=args.interface, count=args.count)
    except KeyboardInterrupt:
        pass
    except PermissionError:
        sys.exit("Capturing traffic needs privileges. Re-run with sudo (Linux/macOS) or as Administrator (Windows).")
    except OSError as exc:
        sys.exit(f"Could not capture: {exc}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
