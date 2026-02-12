import socket
import threading
from datetime import datetime
import argparse
import time
import os
import sys
from pyfiglet import Figlet 
from termcolor import cprint
from colorama import init
from concurrent.futures import ThreadPoolExecutor, as_completed

print_lock = threading.Lock()
open_ports = []  # Açık portları toplayacağız
init()

# Harf harf yazdırma fonksiyonu
def type_effect(text, color="white", delay=0.01):
    for char in text:
        cprint(char, color, end='')
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Açık portlara göre güvenlik önerileri
def suggest_security(port):
    suggestions = {
         21: "Port 21 (FTP): FTP transmits data in plaintext, including credentials. It is highly recommended to disable standard FTP and migrate to FTPS or SFTP, which provide encryption. Additionally, ensure that anonymous access is disabled and strong authentication is enforced.",
         22: "Port 22 (SSH): Secure Shell (SSH) is widely used for remote server management. Ensure root login is disabled by setting 'PermitRootLogin no' in sshd_config. Use key-based authentication instead of passwords. Change the default port if possible, enable fail2ban, and restrict access via firewall or allow only specific IP addresses.",    
         23: "Port 23 (Telnet): Telnet is outdated and transmits data, including credentials, in plaintext. It should be disabled and replaced with SSH. If Telnet is absolutely necessary, restrict it using IP filtering and tunnel it through a secure VPN.",
         80: "Port 80 (HTTP): HTTP does not provide encryption. If the web service is live, ensure that all HTTP requests are redirected to HTTPS using a proper 301 redirect or HSTS policy. Review server headers and implement security headers such as Content-Security-Policy (CSP) and X-Frame-Options.",
         443: "Port 443 (HTTPS): Ensure the SSL/TLS certificate is valid and not expired. Disable weak protocols such as SSLv3 and TLS 1.0. Prefer TLS 1.2 or TLS 1.3. Consider using a certificate from a trusted CA and check your server using tools like SSL Labs for configuration strength.",   
         3306: "Port 3306 (MySQL): MySQL should not be exposed to the internet unless absolutely necessary. Enforce strong authentication and limit access by IP address. Disable remote root login and regularly update MySQL to patch known vulnerabilities. Use a firewall to restrict access to trusted systems.",
         3389: "Port 3389 (RDP): Remote Desktop Protocol is a common attack vector for brute-force attacks. If RDP must be enabled, use Network Level Authentication (NLA), enforce account lockout policies, implement two-factor authentication, and consider tunneling RDP over VPN. Monitor login attempts and restrict access via firewall."
    }
    return suggestions.get(port, "None")

# Her portu ayrı thread ile tarayan fonksiyon
def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            with print_lock:
                type_effect(f"[+] Port {port} is open", color="green", delay=0.005)
                open_ports.append(port)
        sock.close()
    except:
        pass

def parse_args():
    epilog = "Example: python port_scanner.py -t scanme.nmap.org -sp 20 -ep 100"
    parser = argparse.ArgumentParser(description="🔍 Simple Multithreaded Port Scanner with Security Recommendations", epilog=epilog)
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    parser.add_argument("-sp", "--start_port", type=int, required=True, help="Start port")
    parser.add_argument("-ep", "--end_port", type=int, required=True, help="End port")
    return parser.parse_args()

def splash_screen():
    os.system("clear" if os.name == "posix" else "cls")
    figlet = Figlet(font='slant')
    logo_text = figlet.renderText("Port Scanner by Exilex")

    for line in logo_text.splitlines():
        for char in line:
            cprint(char, 'cyan', end='')
            sys.stdout.flush()
            time.sleep(0.002)
        print()
        time.sleep(0.05)

    time.sleep(0.5)
    type_effect("🔍 Python CLI Port Scanner with Security Recommendations", "yellow", delay=0.01)
    type_effect("📌 Usage Example:", "magenta", delay=0.01)
    type_effect("   python PortScanner_1.0.py -t scanme.nmap.org -sp 20 -ep 100\n", "white", delay=0.005)

def main():
    args = parse_args()
    target = args.target
    start_port = args.start_port
    end_port = args.end_port

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        type_effect("[-] Hostname could not be resolved.", color="red")
        return

    type_effect(f"\n🔍 Scanning {target_ip} from port {start_port} to {end_port}", color="cyan")
    type_effect(f"🕒 Start time: {datetime.now()}\n", color="white")

    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception:
                    pass
    except KeyboardInterrupt:
        type_effect("\n[!] Scan interrupted by user. Shutting down gracefully...", color="red")
        return

    type_effect(f"\n✅ Scan completed at: {datetime.now()}", color="green")
    type_effect(f"\n📖 Open Ports and Security Recommendations:\n", color="yellow")

    if open_ports:
        for port in sorted(open_ports):
            type_effect(f"Port {port}: {suggest_security(port)}", color="white", delay=0.003)
    else:
        type_effect("No open ports found.", color="red")

if __name__ == "__main__":
    splash_screen()
    try:
        main()
    except KeyboardInterrupt:
        type_effect("\n[!] Scan aborted by user.", color="red")
