import os
import signal

# Команды для включения перенаправления пакетов и добавления правила iptables
enable_ip_forward_cmd = "sudo sysctl -w net.ipv4.ip_forward=1"
iptables_cmd = "sudo iptables -I FORWARD -j NFQUEUE --queue-num 0"

# Команды для отключения перенаправления пакетов и удаления правила iptables
disable_ip_forward_cmd = "sudo sysctl -w net.ipv4.ip_forward=0"
iptables_remove_cmd = "sudo iptables -D FORWARD -j NFQUEUE --queue-num 0"

def enable_forwarding():
    try:
        os.system(enable_ip_forward_cmd)
        os.system(iptables_cmd)
        print("Перенаправление пакетов и правило iptables включены.")
    except Exception as e:
        print("Ошибка при включении перенаправления пакетов и правила iptables:", str(e))

def disable_forwarding():
    try:
        os.system(disable_ip_forward_cmd)
        os.system(iptables_remove_cmd)
        print("Перенаправление пакетов и правило iptables отключены.")
    except Exception as e:
        print("Ошибка при отключении перенаправления пакетов и правила iptables:", str(e))

def signal_handler(sig, frame):
    disable_forwarding()
    exit(0)

# Обработчик сигнала Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Включение перенаправления пакетов и правила iptables
enable_forwarding()

# Ожидание завершения программы (Ctrl+C)
print("Нажмите Ctrl+C для остановки...")
signal.pause()