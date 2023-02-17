import os

httpx200 = os.system(f"cat *_httpx200")
katana = f"katanaEndpoints"
gau = f"gauEndpoints"
gauplus = f"gauplus"
hakrawler = f"hakrawler"
waybackurls = f"waybackurls"
#gospider = f"gospider"
paramspider = f"paramspider"
arjun1 = f"arjun1"
arjun2 = f"arjun2"
endpoints = f"endpoints"
endpoints200 = f"endpoints200"
blacklist = "md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico"

os.system(f"katana -list *_httpx200 -d 15 -silent -f qurl -o {katana}")
os.system(f"{httpx200} | gau --blacklist {blacklist} --o {gau}")
os.system(f"{httpx200} | gauplus -b {blacklist} -random-agent | uro | tee {gauplus}")
os.system(f"{httpx200} | hakrawler | uro | tee {hakrawler}")
os.system(f"{httpx200} | waybackurls | uro | tee {waybackurls}")
#os.system(f"{httpx200} | xargs -P100 -I@ gospider -c 30 -t 15 -d 4 -a -H 'x-forwarded-for: 127.0.0.1' -H 'User-Agent: Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1' -s @ | tr ' ' '\n' | grep -v '.js' | grep 'https://' | grep '=' | tee {gospider}")
os.system(f"xargs -a *_httpx200 -I@ bash -c 'python3 /Tools/ParamSpider -d @ --level high -e {blacklist}' | uro | tee {paramspider}")
os.system(f"arjun -i *_httpx200 -oT {arjun1}; arjun -i *_httpx200 -m POST -oT {arjun2} ")
os.system(f"cat {katana} {gau} {gauplus} {hakrawler} {waybackurls} {paramspider} {arjun1} {arjun2} | uro | sort -u | tee {endpoints}")
os.system(f"cat {endpoints} | httpx -silent -no-color -o {endpoints200}")
os.system(f"rm -rf {katana} {gau} {gauplus} {hakrawler} {waybackurls} {paramspider} {arjun1} {arjun2}")
os.system(f"echo 'Endpoints Module Finished' | notify ")

#Gospider in tests
#Waybackurls returns garbage | Need Improvements