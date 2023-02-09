import os

subjack = f"subjack"
takeover = f"takeover"
subzy = f"subzy"

os.system(f"subjack -w *_httpx -t 100 -ssl -o {subjack}")
os.system(f"python3 takeover.py -l *_httpx -o {takeover}")
os.system(f"subzy --targets *_httpx -hide_fails --verify_ssl -concurrency 20 | sort -u | tee {subzy}")
os.system(f"mkdir Takeover && mv {subjack} {takeover} {subzy} takeover")