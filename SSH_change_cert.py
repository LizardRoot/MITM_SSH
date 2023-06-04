from scapy.all import *
import os

# Функция-обработчик для изменения пакетов SSH
def ssh_packet_handler(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        # Проверяем, что пакет SSH
        if packet[TCP].dport == 22 or packet[TCP].sport == 22:
            payload = packet[Raw].load
            print(packet.show())
            # Ищем и заменяем сертификат в пакете SSH
            # Вместо замены сертификата можно производить любые другие изменения
            #modified_payload = payload.replace(b'original_certificate', b'new_certificate')

            # Заменяем полезную нагрузку пакета на измененную версию
            #packet[Raw].load = modified_payload

            # Обновляем контрольные суммы и длину пакета
            #del packet[IP].chksum
            #del packet[TCP].chksum
            #del packet[IP].len
            #del packet[TCP].len

            # Отправляем измененный пакет
            send(packet, verbose=0)

# Запускаем перехват пакетов
sniff(filter="tcp", prn=ssh_packet_handler)
