from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time
import os

LOG_FILE = "datasets/traffic_log.csv"

# Ensure dataset directory exists
os.makedirs("datasets", exist_ok=True)

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)

        print(f"[+] {src_ip} -> {dst_ip}, Protocol: {proto}, Length: {length}")

        log_packet(src_ip, dst_ip, proto, length)

def log_packet(src_ip, dst_ip, proto, length):
    data = {'Timestamp': [time.time()], 'Source IP': [src_ip], 'Destination IP': [dst_ip], 'Protocol': [proto], 'Length': [length]}
    df = pd.DataFrame(data)

    df.to_csv(LOG_FILE, mode='a', index=False, header=not os.path.exists(LOG_FILE))

def start_sniffing():
    print("[*] Starting packet capture...")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing()
