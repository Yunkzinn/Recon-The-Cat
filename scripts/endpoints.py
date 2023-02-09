import os

httpx200 = os.system(f"cat *_httpx200")
katana = f"katanaEndpoints"
gau = f"gauEndpoints"
gauplus = f"gauplus"
hakrawler = f"hakrawler"
waybackurls = f"waybackurls"
gospider = f"gospider"
endpoints = f"endpoints"
endpoints200 = f"endpoints200"
blacklist = "md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico"

os.system(f"katana -list *_httpx200 -d 15 -silent -f qurl -o {katana}")
os.system(f"{httpx200} | gau --blacklist {blacklist} -o {gau}")
os.system(f"{httpx200} | gauplus uro | tee {gauplus}")
os.system(f"{httpx200} | hakrawler | uro | tee {hakrawler}")
os.system(f"{httpx200} | waybackurls | uro| tee {waybackurls}")
os.system(f"{httpx200} | xargs -P100 -I@ gospider -c 30 -t 15 -d 4 -a -H 'x-forwarded-for: 127.0.0.1' -H 'User-Agent: Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1' -s @ -o {gospider}")
os.system(f"cat {katana} {gau} {gauplus} {hakrawler} {waybackurls} {gospider} | uro | sort -u {endpoints}")
os.system(f"cat {endpoints} | httpx -silent -no-color -o {endpoints200}")
os.system(f"rm -rf {katana} {gau} {gauplus} {hakrawler} {waybackurls} {gospider}")

#Next improvement add Paramspider