import os

subjack = f"subjack"
takeover = f"takeover"

os.system(f"subjack -w *_httpx -t 100 -timeout 30 -o {subjack} -ssl")
os.system(f"python3 takeover.py -l *_httpx -o {takeover}")
os.system(f"mkdir Takeover && mv {subjack} {takeover} takeover")