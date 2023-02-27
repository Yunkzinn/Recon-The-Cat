#!/bin/bash

echo "[+]-------------------Start Enum Subs-------------------[+]"

mkdir $1
cd $1

# Enum with curl

echo "[+]-------------------Enum Curl-------------------[+]"

curl -s "https://jldc.me/anubis/subdomains/$1" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | tee jldc
curl -s "https://crt.sh/?q=%25.$1&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | tee certsh1
curl -s "https://crt.sh/?q=%25.%25.$1&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | tee certsh2
curl -s "https://crt.sh/?q=%25.%25.%25.$1&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | tee certsh3
curl -s "https://crt.sh/?q=%25.%25.%25.%25.$1&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | tee certsh4
curl -s https://dns.bufferover.run/dns?q=.$1 | jq -r .FDNS_A[] | sed -s 's/,/\n/g' | tee bufferover
curl -s "https://rapiddns.io/subdomain/$1?full=1#result" | grep "<td><a" | cut -d '"' -f 2 | grep http | cut -d '/' -f3 | sed 's/#results//g' | sort -u | tee rapiddns
curl -s "https://riddler.io/search/exportcsv?q=pld:$1" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u | tee riddler
curl -s "https://www.virustotal.com/ui/domains/$1/subdomains?limit=40" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u | tee virustotal
curl -s "http://web.archive.org/cdx/search/cdx?url=*.$1/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | sort -u | tee archive
curl -s https://sonar.omnisint.io/subdomains/$1 | grep -oE "[a-zA-Z0-9._-]+\.$1" | sort -u | tee sonar
curl -s -X POST https://synapsint.com/report.php -d "name=https%3A%2F%2F$1" | grep -oE "[a-zA-Z0-9._-]+\.$1" | sort -u | tee synapsint



# Enum Tools

echo "[+]-------------------Haktrails-------------------[+]"

echo $1 | haktrails subdomains | tee haktrails

echo "[+]-------------------Assetfinder-------------------[+]"

assetfinder -subs-only $1 | tee assetfinder

echo "[+]-------------------Subfinder-------------------[+]"

subfinder -d $1 -all -o subfinder

echo "[+]-------------------Amass Passive-------------------[+]"

amass enum -norecursive -passive -d $1 -o amass1

echo "[+]-------------------Amass Brute-------------------[+]"

amass enum -norecursive -brute -d $1 -o amass2

echo "[+]-------------------Chaos Brute-------------------[+]"

chaos -d $1 -silent -o chaos

echo "[+]-------------------Github Subdomains-------------------[+]"

python3 ~/Tools/github-search/github-subdomains.py -t YOUR_API_KEY_GITHUB -d $1 | tee github

echo "[+]-------------------Findomain-------------------[+]"

findomain -t $1 -q | tee findomain

echo "[+]-------------------Sublist3r-------------------[+]"

python3 ~/Tools/Sublist3r/sublist3r.py -d $1 | tee sublist3r

echo "[+]-------------------Knockpy-------------------[+]"

python3 ~/Tools/knock/knockpy.py $domain | cut -d "," -f1  | tr "]" " "| tr '"' " " | tr "[" " "  | cut -d " " -f6 | sed '1d' >> knock

#Remove Extra Lines
sed -i 1,2d knock; sed -i 1,2d knock; sed -i 1,2d knock; sed -i 1,2d knock; sed -i 1,2d knock; sed -i 1,2d knock; sed -i 1,2d knock; sed -i 1,2d knock; sed -i 1,2d knock

# Join All

echo "[+]-------------------Join All-------------------[+]"

cat jldc certsh1  certsh2 certsh3 certsh4 bufferover rapiddns riddler virustotal archive sonar synapsint haktrails assetfinder subfinder amass1 amass2 chaos github findomain sublist3r knock | anew allSubs

# Check subs

echo "[+]-------------------Httpx Alive Subs-------------------[+]"

cat allSubs | httpx -silent -no-color -p 80,443,81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672 -o aliveSubs

echo "[+]-------------------Httpx 200-------------------[+]"

cat allSubs | httpx -status-code -mc 200 -silent -no-color | tr -d '[]' | tee httpx200; cat httpx200 | awk '{print $1}' >> awkHttpx; rm -rf httpx200; mv awkHttpx httpx200

echo "[+]-------------------Removing Files-------------------[+]"

rm -rf jldc certsh1  certsh2 certsh3 certsh4 bufferover rapiddns riddler virustotal archive sonar synapsint haktrails assetfinder subfinder amass1 amass2 chaos github findomain sublist3r knock

echo "[+]-------------------Dnsgen List-------------------[+]"

# Gen list

cat allSubs | dnsgen - | anew dnsgen

cd ..



# Used Tools and URLS

# - Jldc
# - Certsh
# - Bufferover
# - Riddle
# - VirusTotal
# - Archive
# - Sonar
# - Synapsint
# - Haktrails
# - Assetfinder
# - Subfinder
# - Amass
# - Chaos
# - Github
# - Findomain
# - Sublist3r
# - Knockpy

