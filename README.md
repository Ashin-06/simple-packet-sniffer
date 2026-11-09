# Simple Packet Sniffer

A small, readable command-line packet sniffer built with Python and [Scapy](https://scapy.net/).
It captures a few packets on a network interface and prints one line per packet with the
source, destination and protocol. Read-only: it only observes traffic.

A beginner-friendly introduction to packet capture. For a fuller version with filters, a
protocol breakdown and `.pcap` saving, see
[network-packet-sniffer](https://github.com/Ashin-06/network-packet-sniffer).

## Setup

```bash
git clone https://github.com/Ashin-06/simple-packet-sniffer.git
cd simple-packet-sniffer
pip install -r requirements.txt
```

## Usage

Packet capture needs privileges: run with `sudo` on Linux/macOS, or in an Administrator
terminal on Windows (with [Npcap](https://npcap.com/) installed).

```bash
sudo python sniffer.py --interface eth0 --count 10
python sniffer.py --selftest        # no privileges needed
```

Find an interface name with `ip a` / `ifconfig` (Linux/macOS) or `ipconfig` (Windows).

## Tests

```bash
pip install pytest
python -m pytest -q
```

The tests build packets in memory, so they need no interface and no privileges.

## Note on use

Only capture traffic on networks you own or are authorized to monitor. Unauthorized
packet sniffing is illegal in most places. This project is for learning on your own
machine or lab network.

## License

MIT — see [LICENSE](LICENSE).
