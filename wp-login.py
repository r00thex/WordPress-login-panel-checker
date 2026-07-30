# Developer @r00thex
import argparse
import requests
import urllib3
import sys
from colorama import Fore, Back, Style

RED2 = Fore.LIGHTRED_EX
GREEN = Fore.GREEN
BLUE = Fore.BLUE
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def banner():
     print(f"""            
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠤⠤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡴⠟⠉⠀⠀⠀⠀⠀⠀⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⢀⣾⡿⠛⢿⣿⣶⡄⠀⠀⣀⣴⣶⣶⣶⣶⣄⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡽⢸⣇⠀⣰⣿⣿⣿⣆⣼⡏⠉⢹⣿⣿⣿⣿⣷⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣿⡈⢿⣿⣿⣿⢿⣿⣿⣿⣷⣶⣿⣿⡛⣹⣿⣸⣷⡏⠀⠀⠀⠀⠀⠀
⢀⣤⠤⣼⠉⢷⣌⣛⡿⣿⣦⣾⡟⠙⢿⣿⣿⣿⠿⣛⣵⣿⣯⣀⢀⣤⣤⡀⠀⠀
⠘⢧⣄⡀⠀⠀⠈⠻⣭⣉⠉⠁⠀⠀⠀⠉⣛⣛⣿⡿⠟⠁⠀⠉⠋⠉⢸⡇⠀⠀
⠀⢀⡾⠃⠀⠀⠀⢀⣤⠌⠓⠤⠤⠒⠛⠛⠋⠉⠐⣶⢦⡀⠀⠀⠀⠀⠈⠙⢦⡀
⠀⠸⣧⣤⠴⣆⠀⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡂⣿⠂⠀⠀⠀⣴⠶⠞⠃
⠀⠀⠀⠀⠀⠈⠛⢃⡿⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠈⣇⣿⣤⠜⢷⣄⣼⠆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⢈⡿⠉⠉⠛⠛⠛⢲⡒⠀⠈⣷⠀⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⢤⠴⠟⠁⠀⠀⠀⠀⠀⠈⠻⠦⣤⠼⠃⠀⠀⠀⠀⠀⠀⠀

           
{YELLOW}[+] {WHITE}"Not all who wander are lost, some are just scanning WordPress." :)
""")

def update_bar(current, total):
    width = 30
    filled = int(width * current / total)
    arrow = "-" * (filled - 1) + ">" if filled > 0 else ">"
    empty = " " * (width - filled)
    percent = int(current / total * 100)
    
    bar = f"\r{CYAN}[SCANNED] {WHITE}[{GREEN}{arrow}{WHITE}{empty}] {YELLOW}{current}/{total} ({percent}%)"
    sys.stdout.write(bar + " " * 10)
    sys.stdout.flush()

def scan(url, counter, outputfile, total_lines):
    try:
        resp = requests.get(url, timeout=10, verify=False)
        

        sys.stdout.write("\r" + " " * 80 + "\r")
        
        if resp.status_code == 202 or resp.status_code == 200:
            print(f"{GREEN}[+] {WHITE}{url} status {GREEN}{resp.status_code}")
            final_check(url, resp, counter, outputfile)
        else:
            print(f"{RED2}[-] {url} status {resp.status_code}")
        
        counter += 1
        update_bar(counter, total_lines)
        return counter
        
    except requests.exceptions.Timeout:
        counter += 1
        update_bar(counter, total_lines)
        return counter
    except requests.exceptions.ConnectionError:
        counter += 1
        update_bar(counter, total_lines)
        return counter
    except KeyboardInterrupt:
        print(f"\n\n{GREEN}[MISSION COMPLETE] {CYAN}Total Urls Scanned: {counter}")
        print(f"{MAGENTA}You Pressed CTRL + C!")
        exit()
    except Exception as e:
        sys.stdout.write("\r" + " " * 80 + "\r")
        print(f"{RED2}[-] {url} ERROR: {e}")
        counter += 1
        update_bar(counter, total_lines)
        return counter

def final_check(url_200, resp, counter, output):
    try:
        check_list = ["wp-admin", "wp-includes", "wp-pwd", "WordPress"]
        if any(word.lower() in resp.text.lower() for word in check_list):
            print(f"{GREEN}[WP-LOGIN] {CYAN}{url_200}")
            if output:
                with open(output, "a") as file:
                    file.write(url_200 + "\n")
            else:
                with open("valid.txt", "a") as f:
                    f.write(url_200 + "\n")
        else:
            print(f"{RED2}[NO PANEL] {MAGENTA}{url_200}")
        
    except KeyboardInterrupt:
        print(f"\n\n{GREEN}[MISSION COMPLETE] {CYAN}Total Urls Scanned: {counter}")
        print(f"{MAGENTA}You Pressed CTRL + C!")
        exit()

def get_file(file, output):
    try:
        with open(file, 'r') as f:
            total_lines = sum(1 for line in f if line.strip())
        
        print(f"{CYAN}[+] {WHITE}Total URLs to scan: {total_lines}\n")
        
        with open(file, 'r') as f:
            counter = 0
            update_bar(0, total_lines)
            for line in f:
                base_url = line.strip()
                if base_url:
                    full_url = "https://" + base_url + "/wp-login.php"
                    counter = scan(full_url, counter, output, total_lines)
        
        print(f"\n\n{GREEN}[MISSION COMPLETE] {CYAN}Total Urls Scanned: {counter}")
    except FileNotFoundError:
        print("File Not Found !")
    except KeyboardInterrupt:
        print(f"{MAGENTA}You Pressed CTRL + C!")
        exit()

def commands():
    try:
        parser = argparse.ArgumentParser(description='Wordpress Checker')
        parser.add_argument('-f', dest='file', help='Your Combo List')
        parser.add_argument('-o', dest='output', help='The Results Output File Default (Valid.txt)')
        args = parser.parse_args()

        if not args.file:
            print("Usage: python3 wp-login.py -f list.txt")
        elif not args.output:
            print(f"{CYAN}[+] {WHITE}Valid Results Is Saving in (valid.txt)")
            get_file(args.file, args.output)
        elif args.output:
            print(f"{CYAN}[+] {WHITE}Valid Results Is Saving in ({args.output})")
            get_file(args.file, args.output)
        else:
            get_file(args.file, args.output)
    except FileNotFoundError:
        print(f"[-] File Not Found")

banner()
commands()
