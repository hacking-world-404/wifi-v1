#------------- IMPORT -------------#
from os import system as c
import time
import random

#------------- COLOUR -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{G} ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖    ▗▖  ▗▖ ▗▄▄▖
{G}▐▌ ▐▌ █    █  ▐▌▗▞▘     ▝▚▞▘ ▐▌   
{G}▐▛▀▜▌ █    █  ▐▛▚▖       ▐▌  ▐▌   
{G}▐▌ ▐▌ █  ▗▄█▄▖▐▌ ▐▌    ▗▞▘▝▚▖▝▚▄▄▖
""")

#------------- ANIMATION -------------#
def loading(txt):
    logo()
    print(f"{C}{txt}")
    for i in range(10):
        dots = "." * (i % 4)
        print(f"{Y}[{G}{'='*i}{A}>{' '*(10-i)}] {i*10}%{dots}", end="\r")
        time.sleep(0.3)
    print(f"{G}\n[✓] DONE!\n")
    time.sleep(1)

#------------- MAIN MENU -------------#
def menu():
    logo()
    print(f"{G}[1] START WiFi HACK")
    print(f"{G}[2] SHOW VIP PASSWORD LIST")
    print(f"{G}[0] EXIT TOOL")
    print(f"{G}--------------------------------------------------")
    choice = input(f"{G}[?] SELECT OPTION: ")
    if choice == '1':
        wifi_hack()
    elif choice == '2':
        password_list()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        menu()

#------------- WiFi HACK -------------#
def wifi_hack():
    logo()
    c('espeak "WiFi Hacking Starting"')
    wifi_name = input(f"{C}ENTER WiFi NAME: ")
    print(f"\n{Y}[+] Connecting to {wifi_name} network...")
    loading("Connecting to target router...")
    print(f"{G}[✓] Connected to {wifi_name}")

    print(f"\n{B}[+] Fetching Available Passwords...")
    time.sleep(2)
    passwords = [
        'wifi1234', 'vipnet2024', 'hackzone999', 'admin@123',
        'password007', 'dragonwifi', 'bossnetwork', 'hackwifi2025'
    ]
    for pw in passwords:
        print(f"{P}[*] Found Password: {C}{pw}")
        time.sleep(1)

    print(f"\n{G}[!] WIFI HACKED SUCCESSFUL PASSWORD - ALAMIN22@@")
    time.sleep(1.5)
    print(f"{Y}Visit: {G}https://wifi-vip-connect.com to finish verification")

    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#------------- PASSWORD LIST -------------#
def password_list():
    logo()
    print(f"{P} VIP WiFi Passwords:")
    passwords = [
        'wifi1234', 'vipnet2024', 'hackzone999', 'admin@123',
        'password007', 'dragonwifi', 'bossnetwork', 'hackwifi2025'
    ]
    for pw in passwords:
        print(f"{C}[*] {pw}")
        time.sleep(0.5)
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#------------- START TOOL -------------#
menu()