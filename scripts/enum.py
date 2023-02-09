import os

domain = input("Domain to Search: ")

haktrails = f"{domain.split('.')[0]}_haktrails"
assetfinder = f"{domain.split('.')[0]}_assetfinder"
subfinder = f"{domain.split('.')[0]}_subfinder"
amass = f"{domain.split('.')[0]}_amass"
amass2 = f"{domain.split('.')[0]}_amass2"
chaos = f"{domain.split('.')[0]}_chaos"
githubHttpx = f"{domain.split('.')[0]}_githubHttpx"
subfile = f"{domain.split('.')[0]}_subs"
dnsgen = f"{domain.split('.')[0]}_dnsgen"
allSubs = f"{domain.split('.')[0]}_allSubs"
httpx = f"{domain.split('.')[0]}_httpx"
httpx200 = f"{domain.split('.')[0]}_200httpx"
awkHttpx = f"{domain.split('.')[0]}_awkhttpx"
apiGitHub = "YOUR_API_KEY_GITHUB"
allports = "80,443,81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672"


os.system(f"echo {domain} | haktrails subdomains >> {haktrails}")
os.system(f"assetfinder -subs-only {domain} >> {assetfinder}")
os.system(f"subfinder -d {domain} -all -o {subfinder}")
os.system(f"amass enum -norecursive -passive -d {domain} -o {amass}")
os.system(f"amass enum -norecursive -brute -d {domain} -o {amass2}")
os.system(f"chaos -d {domain} -silent -o {chaos}")
os.system(f"python3 ~/Tools/github-search/github-subdomains.py -t {apiGitHub} -d {domain} | httpx --title >> {githubHttpx}")
os.system(f"cat {haktrails} {assetfinder} {subfinder} {amass} {amass2} {chaos} {githubHttpx} | anew {subfile}")
os.system(f"cat {subfile} | dnsgen - | httpx -silent -no-color -p {allports} -o {dnsgen}")
os.system(f"cat {subfile} {dnsgen} | anew {allSubs}")
os.system(f"cat {allSubs} | httpx -silent -no-color -p {allports} -o {httpx}")
os.system(f"cat {allSubs} | httpx -status-code -mc 200 -silent -no-color | tr -d '[]' | tee {httpx200}; cat {httpx200} | awk '{{print $1}}' >> {awkHttpx}; rm -rf {httpx200}; mv {awkHttpx} {httpx200}")
os.system(f"rm -rf {haktrails} {assetfinder} {subfinder} {amass} {amass2} {chaos} {githubHttpx} {dnsgen} {subfile}")
