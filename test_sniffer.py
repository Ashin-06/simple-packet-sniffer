"""Tests for the summarizer. They build packets in memory, so no interface or privileges are needed."""
from scapy.all import IP, TCP, UDP, Ether

import sniffer


def test_tcp_and_udp_lines():
    assert sniffer.summarize(IP(src="1.1.1.1", dst="2.2.2.2") / TCP()) == "1.1.1.1 -> 2.2.2.2  [TCP]"
    assert sniffer.summarize(IP(src="1.1.1.1", dst="2.2.2.2") / UDP()) == "1.1.1.1 -> 2.2.2.2  [UDP]"


def test_non_ip_packet_does_not_raise():
    assert sniffer.summarize(Ether() / (b"\x00" * 10))


def test_selftest_passes():
    assert sniffer.selftest() == 0
