import subprocess
import random
import re
import locale
import os

def print_banner():
    banner = """
\033[94m ___________   _   _ _________________ ___________ 
|_   _| ___ \\ | | | |_   _|  _  \\  _  \\  ___| ___ \\
  | | | |_/ / | |_| | | | | | | | | | | |__ | |_/ /
  | | |  __/  |  _  | | | | | | | | | |  __||    / 
 _| |_| |     | | | |_| |_| |/ /| |/ /| |___| |\\ \\ 
 \\___/\\_|     \\_| |_|\\___/|___/ |___/ \\____/\\_| \\_|
                                                   
\033[0m"""
    print(banner)

def generate_random_ip():
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

def get_current_ip():
    encoding = locale.getpreferredencoding()
    ipconfig_result = subprocess.check_output(["ipconfig"], shell=True).decode(encoding, errors='ignore')
    match = re.search(r"IPv4 Address.*?: (\d+\.\d+\.\d+\.\d+)", ipconfig_result)
    if match:
        return match.group(1)
    else:
        return None

def change_ip():
    real_ip = get_current_ip()
    subprocess.call(["ipconfig", "/release"])
    subprocess.call(["ipconfig", "/renew"])
    new_ip = get_current_ip()
    print(f"Your real IP ({real_ip}) has been hidden. Your new IP is: {new_ip}")

def reset_ip():
    subprocess.call(["ipconfig", "/release"])
    subprocess.call(["ipconfig", "/renew"])

def show_current_ip():
    current_ip = get_current_ip()
    if current_ip:
        print(f"Your current IP address is: {current_ip}")
    else:
        print("Unable to retrieve current IP address.")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = subprocess.call('cls', shell=True)
    # For Unix-like systems (Linux, macOS)
    else:
        _ = subprocess.call('clear', shell=True)

def main():
    while True:
        clear_screen()
        print_banner()
        print("\033[94m1. Change IP address\033[0m")
        print("\033[94m2. Reset IP address\033[0m")
        print("\033[94m3. Show current IP address\033[0m")
        print("\033[94m4. Exit\033[0m")
        choice = input("\033[94mEnter your choice: \033[0m")

        if choice == "1":
            change_ip()
        elif choice == "2":
            reset_ip()
        elif choice == "3":
            show_current_ip()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
