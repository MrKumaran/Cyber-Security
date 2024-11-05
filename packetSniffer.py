# Description: This script is a simple packet sniffer that uses scapy to capture packets from the network.
from scapy.all import sniff


def packet_analyzer(packet):
    print(packet.summary())


try:
    sniff(prn=packet_analyzer)
except KeyboardInterrupt:
    print("\nSniffing stopped.")
