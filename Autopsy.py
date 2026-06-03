import os
import sys
import socket
import re
import time
import json
import requests
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def gradient_text(text, start_color=(0, 255, 0), end_color=(255, 255, 255)):
    result = ""
    steps = len(text)
    for i, char in enumerate(text):
        ratio = i / max(steps - 1, 1)
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        result += f"\033[38;2;{r};{g};{b}m{char}"
    return result + Style.RESET_ALL


def print_section(title):
    print(f"\n{Fore.WHITE}{Style.BRIGHT}{'=' * 60}")
    print(f"{Fore.GREEN}{Style.BRIGHT}  {title}")
    print(f"{Fore.WHITE}{Style.BRIGHT}{'=' * 60}")


def print_field(key, value):
    print(f"  {Fore.GREEN}{key}: {Fore.WHITE}{value}")


def print_success(msg):
    print(f"{Fore.GREEN}[OK] {Fore.WHITE}{msg}")


def print_error(msg):
    print(f"{Fore.RED}[ER] {Fore.WHITE}{msg}")


def print_info(msg):
    print(f"{Fore.YELLOW}[!] {Fore.WHITE}{msg}")


def animate_banner():
    clear_screen()

    lines = [
        "╔══════════════════════════════════════════════════════════════════════════════╗",
        "║                                                                              ║",
        "║           █████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ███████╗██╗   ██╗        ║",
        "║          ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝╚██╗ ██╔╝        ║",
        "║          ███████║██║   ██║   ██║   ██║   ██║██████╔╝███████╗ ╚████╔╝         ║",
        "║          ██╔══██║██║   ██║   ██║   ██║   ██║██╔═══╝ ╚════██║  ╚██╔╝          ║",
        "║          ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║     ███████║   ██║           ║",
        "║          ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚══════╝   ╚═╝           ║",
        "║                                                                              ║",
        "╚══════════════════════════════════════════════════════════════════════════════╝"
    ]

    for line in lines:
        if 'AUTOPSY' in line or '█' in line or '╗' in line or '╔' in line or '╝' in line or '╚' in line or '║' in line:
            for char in line:
                if char in '╔╗╚╝║═':
                    print(f"{Fore.GREEN}{char}", end='', flush=True)
                elif char in '█':
                    print(f"{gradient_text(char)}", end='', flush=True)
                else:
                    print(f"{Fore.WHITE}{char}", end='', flush=True)
                time.sleep(0.0003)
            print()
        else:
            print(f"{Fore.GREEN}{line}")
        time.sleep(0.03)

    print(f"\n{Fore.WHITE}{Style.BRIGHT}┌─────────────────────────────────────────────────────────┐")
    print(
        f"{Fore.WHITE}{Style.BRIGHT}│  {Fore.GREEN}Author: {Fore.WHITE}@Fell1ksx                                    {Fore.WHITE}{Style.BRIGHT}  │")
    print(
        f"{Fore.WHITE}{Style.BRIGHT}│  {Fore.GREEN}Channel: {Fore.WHITE}@FelliksxBestSoft                          {Fore.WHITE}{Style.BRIGHT}   │")
    print(
        f"{Fore.WHITE}{Style.BRIGHT}│  {Fore.GREEN}Price: {Fore.WHITE}FREE                                          {Fore.WHITE}{Style.BRIGHT}  │")
    print(
        f"{Fore.WHITE}{Style.BRIGHT}│  {Fore.GREEN}Version: {Fore.WHITE}1.1                                       {Fore.WHITE}{Style.BRIGHT}    │")
    print(f"{Fore.WHITE}{Style.BRIGHT}└─────────────────────────────────────────────────────────┘{Style.RESET_ALL}")

    input(f"\n{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Press {Fore.GREEN}ENTER {Fore.WHITE}to continue...")


def validate_email(email):
    print_section("EMAIL VALIDATION")
    print_success(f"Checking: {email}")

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        print_error("Invalid email format")
        return

    print_success("Format is valid")

    domain = email.split('@')[1]
    print_field("Domain", domain)

    try:
        socket.gethostbyname(domain)
        print_success("Domain exists")
    except:
        print_error("Domain not found")
        return

    print_info("Clearout API: POST https://api.clearout.io/v2/email_finder/instant")
    print_info("Header: Authorization: Bearer YOUR_TOKEN")
    print_info('Body: {"name": "User Name", "domain": "' + domain + '"}')


def search_email_by_domain(domain):
    print_section("EMAIL SEARCH BY DOMAIN")
    print_success(f"Searching for: {domain}")

    try:
        socket.gethostbyname(domain)
        print_success("Domain is active")
    except:
        print_error("Domain not found")
        return

    patterns = ['admin', 'info', 'support', 'contact', 'sales', 'hello', 'mail', 'webmaster', 'postmaster', 'abuse',
                'security', 'hostmaster']

    print_success("Common email patterns:")
    for p in patterns:
        print(f"    {Fore.CYAN}|- {p}@{domain}")

    print_info("API: Hunter.io, Clearout.io")


def google_search(query):
    print_section("GOOGLE SEARCH")
    print_success(f"Query: {query}")

    from urllib.parse import quote
    encoded = quote(query)
    url = f"https://www.google.com/search?q={encoded}"

    print_field("Search URL", url)

    dorks = [
        f'site:{query.split()[-1] if query else "target.com"}',
        f'intitle:"{query}"',
        f'inurl:{query.split()[-1] if query else "admin"}'
    ]

    print_success("Google Dorks:")
    for dork in dorks:
        print(f"    {Fore.CYAN}|- {dork}")


def dns_lookup(domain):
    print_section("DNS LOOKUP")
    print_success(f"DNS for: {domain}")

    try:
        ip = socket.gethostbyname(domain)
        print_success(f"A Record: {ip}")
    except:
        print_error("A record not found")

    try:
        import dns.resolver
        types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        for t in types:
            try:
                answers = dns.resolver.resolve(domain, t)
                print_success(f"{t} Records:")
                for rdata in answers:
                    print(f"    {Fore.CYAN}|- {rdata}")
            except:
                pass
    except ImportError:
        print_info("Install: pip install dnspython")

    try:
        whois_url = f"https://api.domainscan.in/v1/whois?domain={domain}"
        resp = requests.get(whois_url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            print_success("WHOIS Information:")
            if isinstance(data, dict):
                for key, value in data.items():
                    if value and key not in ['_id', '__v']:
                        print_field(key.replace('_', ' ').title(), str(value))
        else:
            print_info("WHOIS data not available")
    except Exception as e:
        print_info(f"WHOIS API error: {e}")
        print_info("Try manual: whois.domaintools.com")


def ip_lookup(target):
    print_section("IP LOOKUP")
    print_success(f"Looking up: {target}")

    try:
        resp = requests.get(f"http://ip-api.com/json/{target}", timeout=10)
        data = resp.json()

        if data.get('status') == 'success':
            print(f"\n  {Fore.CYAN}{'-' * 50}")
            fields = {
                'IP': 'query',
                'Country': 'country',
                'Country Code': 'countryCode',
                'Region': 'regionName',
                'City': 'city',
                'ZIP': 'zip',
                'Coordinates': ('lat', 'lon'),
                'Timezone': 'timezone',
                'ISP': 'isp',
                'Organization': 'org',
                'AS': 'as',
                'Reverse DNS': 'reverse',
                'Mobile': 'mobile',
                'Proxy': 'proxy',
                'Hosting': 'hosting'
            }

            for label, key in fields.items():
                if isinstance(key, tuple):
                    val = f"{data.get(key[0], 'N/A')}, {data.get(key[1], 'N/A')}"
                elif key in ['mobile', 'proxy', 'hosting']:
                    val = "Yes" if data.get(key) else "No"
                else:
                    val = data.get(key, 'N/A')
                print_field(label, val)
            print(f"  {Fore.CYAN}{'-' * 50}")
        else:
            print_error("Failed to get data")
    except Exception as e:
        print_error(f"Error: {e}")


def my_ip_lookup():
    print_section("MY IP LOOKUP")

    try:
        resp = requests.get("http://ip-api.com/json/", timeout=10)
        data = resp.json()

        if data.get('status') == 'success':
            print(f"\n  {Fore.CYAN}{'-' * 50}")
            print_field("IP", data.get('query', 'N/A'))
            print_field("Country", data.get('country', 'N/A'))
            print_field("Region", data.get('regionName', 'N/A'))
            print_field("City", data.get('city', 'N/A'))
            print_field("ISP", data.get('isp', 'N/A'))
            print_field("Timezone", data.get('timezone', 'N/A'))
            print(f"  {Fore.CYAN}{'-' * 50}")
    except:
        print_error("Failed to get IP")


def ssl_checker(domain):
    print_section("SSL CERTIFICATE CHECKER")
    print_success(f"Checking SSL: {domain}")

    try:
        ssl_url = f"https://api.domainscan.in/v1/ssl?domain={domain}"
        resp = requests.get(ssl_url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            print_success("SSL Certificate Info:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print_info("SSL data not available via API")
    except:
        pass

    try:
        import ssl
        import OpenSSL

        cert = ssl.get_server_certificate((domain, 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

        print_success("Direct SSL Check:")
        print_field("Issuer", x509.get_issuer().CN)
        print_field("Subject", x509.get_subject().CN)
        print_field("Valid From", str(x509.get_notBefore().decode()))
        print_field("Valid Until", str(x509.get_notAfter().decode()))
        print_field("Serial", str(x509.get_serial_number()))
    except ImportError:
        print_info("For direct check install: pip install pyOpenSSL")
    except Exception as e:
        print_info(f"Direct check failed: {e}")


def domain_health(domain):
    print_section("DOMAIN HEALTH LOOKUP")
    print_success(f"Health check: {domain}")

    try:
        resp = requests.get(f"https://api.domainscan.in/v1/health?domain={domain}", timeout=10)
        data = resp.json()
        print_success("Domain health data:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except:
        print_error("API unavailable")


def domain_lookup(domain):
    print_section("DOMAIN LOOKUP")

    try:
        whois_url = f"https://api.domainscan.in/v1/whois?domain={domain}"
        resp = requests.get(whois_url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            print_success(f"WHOIS for: {domain}")
            if isinstance(data, dict):
                for key, value in data.items():
                    if value and key not in ['_id', '__v', 'raw_text']:
                        print_field(key.replace('_', ' ').title(), str(value))
        else:
            print_error("WHOIS data not available")
    except Exception as e:
        print_error(f"Error: {e}")


def reverse_ip_lookup(ip):
    print_section("REVERSE IP LOOKUP")
    print_success(f"Reverse: {ip}")

    try:
        hostname = socket.gethostbyaddr(ip)
        print_field("Hostname", hostname[0])
    except:
        print_error("No reverse DNS")

    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = resp.json()
        if data.get('status') == 'success':
            print_field("Reverse DNS", data.get('reverse', 'N/A'))
            print_field("ISP", data.get('isp', 'N/A'))
    except:
        pass


def ping_tool(host):
    print_section("PING TOOL")
    print_success(f"Pinging: {host}")

    import platform
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    cmd = f"ping {param} 4 {host}"

    try:
        result = os.popen(cmd).read()
        print(f"{Fore.CYAN}{result}")
    except:
        print_error("Ping failed")


def open_port_lookup(host):
    print_section("OPEN PORT LOOKUP")
    print_success(f"Scanning: {host}")

    ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
        443: "HTTPS", 993: "IMAPS", 995: "POP3S",
        3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 8080: "HTTP-Alt"
    }

    print_info("Scanning ports...")
    for port, service in ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"    {Fore.GREEN}|- {port} {service} - OPEN")
            sock.close()
        except:
            pass


def hash_generator(text):
    print_section("HASH GENERATOR")
    print_success(f"Hashes for: {text}")

    import hashlib

    hashes = {
        'MD5': hashlib.md5(text.encode()).hexdigest(),
        'SHA1': hashlib.sha1(text.encode()).hexdigest(),
        'SHA256': hashlib.sha256(text.encode()).hexdigest(),
        'SHA512': hashlib.sha512(text.encode()).hexdigest()
    }

    for name, value in hashes.items():
        print_field(name, value)


def base64_converter(text, mode):
    print_section("BASE64 CONVERTER")

    import base64

    if mode == 'encode':
        result = base64.b64encode(text.encode()).decode()
        print_success("Encoded:")
    else:
        try:
            result = base64.b64decode(text).decode()
            print_success("Decoded:")
        except:
            print_error("Invalid Base64 string")
            return

    print_field("Result", result)


def show_menu():
    clear_screen()

    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║              AUTOPSY - THE SEARCH TOOL                   ║
    ╚══════════════════════════════════════════════════════════╝
    """

    for line in banner.split('\n'):
        if 'AUTOPSY' in line:
            print(gradient_text(line))
        else:
            print(f"{Fore.GREEN}{line}")

    print(f"\n{Fore.WHITE}{Style.BRIGHT}{'=' * 60}")
    print(f"{Fore.GREEN}{Style.BRIGHT}                 --- ( MAIN MENU ) ---")
    print(f"{Fore.WHITE}{Style.BRIGHT}{'=' * 60}\n")

    menu = [
        ("1", "Email Validation"),
        ("2", "Email Search by Domain"),
        ("3", "Google Search"),
        ("4", "DNS Lookup"),
        ("5", "IP Lookup"),
        ("6", "My IP Lookup"),
        ("7", "SSL Certificate Checker"),
        ("8", "Domain Health Lookup"),
        ("9", "Domain Lookup (WHOIS)"),
        ("10", "Reverse IP Lookup"),
        ("11", "Ping Tool"),
        ("12", "Open Port Lookup"),
        ("13", "Hash Generator"),
        ("14", "Base64 Converter"),
        ("0", "Exit")
    ]

    left = menu[:7]
    right = menu[7:14]
    exit_item = menu[14]

    print(f"  {Fore.CYAN}{'─' * 28}  {Fore.CYAN}{'─' * 28}")
    
    for i in range(7):
        left_num, left_desc = left[i]
        right_num, right_desc = right[i] if i < len(right) else ("", "")
        
        left_str = f"{Fore.GREEN}{Style.BRIGHT}[{left_num}] {Fore.WHITE}{left_desc}"
        right_str = f"{Fore.GREEN}{Style.BRIGHT}[{right_num}] {Fore.WHITE}{right_desc}" if right_num else ""
        
        print(f"  {left_str:<42}{right_str}")
    
    print(f"  {Fore.CYAN}{'─' * 28}  {Fore.CYAN}{'─' * 28}")
    print(f"\n  {Fore.YELLOW}{Style.BRIGHT}{'─' * 58}")
    print(f"  {Fore.RED}{Style.BRIGHT}[{exit_item[0]}] {Fore.WHITE}{exit_item[1]}")
    print(f"  {Fore.YELLOW}{Style.BRIGHT}{'─' * 58}")

    print(f"\n{Fore.WHITE}{Style.BRIGHT}{'=' * 60}\n")

    choice = input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Select {Fore.GREEN}(0-14){Fore.WHITE}: ")

    if choice == '0':
        print(f"\n{Fore.GREEN}[OK] {Fore.WHITE}Thanks for using {Fore.GREEN}Autopsy{Fore.WHITE}!")
        sys.exit(0)

    functions = {
        '1': lambda: validate_email(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Email: ")),
        '2': lambda: search_email_by_domain(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Domain: ")),
        '3': lambda: google_search(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Query: ")),
        '4': lambda: dns_lookup(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Domain: ")),
        '5': lambda: ip_lookup(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}IP/Domain: ")),
        '6': lambda: my_ip_lookup(),
        '7': lambda: ssl_checker(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Domain: ")),
        '8': lambda: domain_health(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Domain: ")),
        '9': lambda: domain_lookup(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Domain: ")),
        '10': lambda: reverse_ip_lookup(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}IP: ")),
        '11': lambda: ping_tool(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Host/IP: ")),
        '12': lambda: open_port_lookup(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Host/IP: ")),
        '13': lambda: hash_generator(input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Text: ")),
        '14': lambda: base64_converter(
            input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Text: "),
            input(f"{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Mode (encode/decode): ").lower()
        )
    }

    if choice in functions:
        functions[choice]()
        input(f"\n{Fore.YELLOW}[{Fore.GREEN}>{Fore.YELLOW}] {Fore.WHITE}Press ENTER to return...")
        show_menu()
    else:
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Invalid choice!")
        time.sleep(1)
        show_menu()

def main():
    try:
        animate_banner()
        show_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] {Fore.WHITE}Interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[ER] {Fore.WHITE}{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()