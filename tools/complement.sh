#!/bin/bash

# Input domain
echo "Enter the domain to be enumerated:"
read domain

curl -s "https://jldc.me/anubis/subdomains/$domain" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew jldc1;
curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | httpx -title -silent | anew certsh1;
curl -s https://dns.bufferover.run/dns?q=.$domain | jq -r .FDNS_A[] | sed -s 's/,/\n/g' | httpx -silent | anew bufferover;
curl -s "https://jldc.me/anubis/subdomains/$domain" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | httpx -silent -threads 300 | anew | rush -j 10 'jaeles scan -s /jaeles-signatures/ -u {}';

