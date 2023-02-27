#!/bin/bash

echo "[+]-------------------Start Enum JS-------------------[+]"

cat httpx200 | getJS --complete | anew getJS
cat httpx200 | katana -d 15 -silent -em js,jsp,json -o katana
cat httpx200 | gau -subs | grep -iE '\.js'| grep -iEv '(\.jsp|\.json)' | tee gau
cat httpx200 | waybackurls | grep -E '\.json(?:onp?)?$' | anew waybackurls1
cat httpx200 | waybackurls | grep -iE '\.js'| grep -iEv '(\.jsp)' | tee waybackurls2
cat httpx200 | gospider --js | grep -E '\.js(?:onp?)?$' | awk '{print $4}' | tr -d '[]' | anew gospider
cat httpx200 | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | awk '{{print $3}}' | grep -E '\.js(?:onp?)?$' | anew hakrawler1
cat httpx200 | rush -j 100 'hakrawler -js -plain -usewayback -depth 6 -scope subs -url {} | unew hakrawler2'
cat httpx200 | xargs -I@ sh -c 'pyth3 dirsearch.py -r -b -w path -u @ -i 200, 403, 401, 302 -e json,js,jsp' | tee dirsearch

echo "[+]-------------------Join All-------------------[+]"

echo "[+]-------------------JS JSON & JSP-------------------[+]"

cat getJS katana gau waybackurls1 waybackurls2 gospider hakrawler1 hakrawler2 dirsearch | sort -u | tee allJS

echo "[+]-------------------Just JS-------------------[+]"

cat getJS katana gau waybackurls1 waybackurls2 gospider hakrawler1 hakrawler2 dirsearch | grep -E '\.js(?:onp?)?$' | sort -u | tee justJS

echo "[+]-------------------Validating JS-------------------[+]"

cat allJS | anti-burl | anew js200

cat justJS | anti-burl | anew aliveJustJS

echo "[+]-------------------Removing Files-------------------[+]"

rm -rf getJS katana gau waybackurls1 waybackurls2 gospider hakrawler1 hakrawler2 dirsearch

echo "[+]-------------------Sending Notification-------------------[+]"

echo "JS Enum Finished" | notify

