#!/bin/bash

echo "[+]-------------------Start Enum Endpoints-------------------[+]"

echo "[+]-------------------Katana-------------------[+]"
katana -list aliveSubs -d 15 -silent -f qurl -o katana

echo "[+]-------------------Gau-------------------[+]"

cat aliveSubs | gau --blacklist md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico | uro | tee gau

echo "[+]-------------------Gauplus-------------------[+]"

cat aliveSubs | gauplus -b md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico -random-agend | uro | tee gauplus

echo "[+]-------------------Hakrawler-------------------[+]"

cat aliveSubs | hakrawler | uro | tee hakrawler

echo "[+]-------------------Waybackurls-------------------[+]"

cat aliveSubs | waybackurls | uro | tee waybackurls

echo "[+]-------------------ParamSpider-------------------[+]"

xargs -a aliveSubs -I@ bash -c 'python3 /Tools/ParamSpider -d @ --level high -e md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico ' | uro | tee paramspider

echo "[+]-------------------Arjun-------------------[+]"

arjun -i aliveSubs -oT arjun1

arjun -i aliveSubs -m POST -oT arjun2

echo "[+]-------------------Join All-------------------[+]"

cat katana gau gauplus hakrawler waybackurls paramspider arjun1 arjun2 | uro | sort -u | tee allEndpoints

echo "[+]-------------------Validating Endpoints-------------------[+]"

cat allEndpoints | httpx -silent -o endpoints

echo "[+]-------------------Removing Files-------------------[+]"

rm -rf katana gau gauplus hakrawler waybackurls paramspider arjun1 arjun2

echo "[+]-------------------Sending Notification-------------------[+]"

echo "Enum Endpoints Finished" | notify