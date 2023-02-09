import os

httpx200 = os.system(f"cat *_httpx200")
getJS = f"getJS"
katana = f"katanaJS"
gau = f"gauJS"
waybackurls1 = f"waybackurls1"
waybackurls2 = f"waybackurls2"
gospider = f"gospider"
hakrawler1 = f"hakrawler1"
hakrawler2 = f"hakrawler2"
dirsearch = f"dirsearch"
allJS = f"allJS"
justJS = f"justJS"
js200 = f"js200"
aliveJustJS = f"aliveJustJS"


os.system(f"{httpx200} | getJS --complete | anew {getJS}")
os.system(f"{httpx200} | katana -d 10 -silent -em js,jsp,json -o {katana}")
os.system(f"{httpx200} | gau -subs | grep -iE '\.js'| grep -iEv '(\.jsp|\.json)' | tee {gau}")
os.system(f"{httpx200} | waybackurls | grep -E '\.json(?:onp?)?$' | anew {waybackurls1}")
os.system(f"{httpx200} | waybackurls | grep -iE '\.js'| grep -iEv '(\.jsp)' | tee {waybackurls2}")
os.system(f"{httpx200} | gospider --js | grep -E '\.js(?:onp?)?$'' | awk '{{print $4}}' | tr -d '[]' | anew {gospider}")
os.system(f"{httpx200} | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | awk '{{print $3}}' | grep -E '\.js(?:onp?)?$' | anew {hakrawler1}")
os.system(f"{httpx200} | rush -j 100 'hakrawler -js -plain -usewayback -depth 6 -scope subs -url {{}} | unew h {hakrawler2}'")
os.system(f"{httpx200} | xargs -I@ sh -c 'python3 dirsearch.py -r -b -w path -u @ -i 200, 403, 401, 302 -e json,js,jsp' | tee {dirsearch}")
os.system(f"cat {getJS} {katana} {gau} {waybackurls1} {waybackurls2} {gospider} {hakrawler1} {hakrawler2} {dirsearch} | sort -u {allJS}")
os.system(f"cat {getJS} {katana} {gau} {waybackurls1} {waybackurls2} {gospider} {hakrawler1} {hakrawler2} {dirsearch} | grep -E '\.js(?:onp?)?$' | sort -u {justJS}")
os.system(f"cat {allJS} | anti-burl | anew {js200}")
os.system(f"cat {justJS} | anti-burl | anew {aliveJustJS}")
os.system(f"rm -rf {getJS} {katana} {gau} {waybackurls1} {waybackurls2} {gospider} {hakrawler1} {hakrawler2} {dirsearch}")



#Add In Future:
#os.system(f"cat dominios | gau | grep -iE '\.js'| grep -iEv '(\.jsp|\.json)' >> gauJS.txt ; cat dominios | waybackurls | grep -iE '\.js'| grep -iEv '(\.jsp|\.json)' >> waybJS.txt ; gospider -a -S dominios -d 2 | grep -Eo '(http|https)://[^/\"].*\.js+' | sed 's#\] \- #\n#g' >> gospiderJS.txt ; cat gauJS.txt waybJS.txt gospiderJS.txt | sort -u >> saidaJS ; rm -rf *.txt ; cat saidaJS | anti-burl |awk '{{print $4}}' | sort -u >> AliveJs.txt ; xargs -a AliveJs.txt -n 2 -I@ bash -c 'echo -e '\n[URL]: @\n'; python3 linkfinder.py -i @ -o cli' ; cat AliveJs.txt  | python3 collector.py output ; rush -i output/urls.txt 'python3 SecretFinder.py -i {{}} -o cli | sort -u >> output/resultJSPASS'")