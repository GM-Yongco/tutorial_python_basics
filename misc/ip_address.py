# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code to get your ip address
# HEADERS ================================================================

import socket
import requests

# ========================================================================
# MAIN 
# ========================================================================

ip_local:str = ":DDD"
ip_public:str = ":DDD"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
finally:
        s.close()

print(f"Local\tIP address: {ip_local}")

try:
        ip_public = requests.get("https://api.ipify.org").text
except Exception as e:
        ip_public = e

print(f"Public\tIP address: {ip_public}")
