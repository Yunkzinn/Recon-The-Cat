#!/bin/bash

echo " _____ _____ _____ _____ _____ _____ "
echo "|     |     |     |     |     |     |"
echo "|  S  |  u  |  b  |  z  |  Y  |  k  |"
echo "|_____|_____|_____|_____|_____|_____|"

# Input domain
echo "Enter the domain to be enumerated:"
read domain

# Use Sublist3r to find subdomains
echo "Searching for subdomains with Sublist3r..."
python3 /path/to/sublist3r.py -d $domain -o sublist3r_output.txt

# Use Amass to find additional subdomains
echo "Searching for additional subdomains with Amass..."
amass enum -d $domain -o amass_output.txt

# Use knockpy to find additional subdomains
echo "Searching for additional subdomains with knockpy..."
knockpy $domain > knockpy_output.txt

# Use Assetfinder to find additional subdomains
echo "Searching for additional subdomains with Assetfinder..."
assetfinder --subs-only $domain > assetfinder_output.txt

# Use Subfinder to find additional subdomains
echo "Searching for additional subdomains with Subfinder..."
subfinder -d $domain -o subfinder_output.txt

# Join results from all tools into a single file
echo "Joining all results into a single file..."
cat sublist3r_output.txt amass_output.txt knockpy_output.txt assetfinder_output.txt subfinder_output.txt | sort -u > subs.txt

# Remove duplicates and save to file
sort -u subs.txt -o subs.txt

# Use httpx to check which subdomains return HTTP 200 status code
echo "Checking which subdomains return HTTP 200 status code..."
httpx -status-code -threads 100 -timeout 5 -input-file subs.txt -o 200subs.txt

# Display the number of live subdomains
echo "Number of subdomains live:"
wc -l 200subs.txt

# Crawl and Enum Katana
echo "Searching for files with Katana"
katana -list 200subs.txt -d 15 -silent -ef md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico -em js,jsp,json,php,aspx,asp -o katanafiles.txt

# Extract JS with Gauplus
echo "Extracting JS with Gauplus"
echo $domain | gauplus | grep -iE '\.js' | anew gauplus_js.txt

# Extract JS with Jsubfinder
echo "Extracting JS with Jsubfinder"
echo $domain | jsubfinder search | subfinder -all -silent > jsubfinder_js.txt

# Join results from all tools into a single file
echo "Joining all results into a single file..."
cat katanafiles.txt gauplus_js.txt jsubfinder_js.txt | sort -u > files.txt

# Remove duplicates and save to file
sort -u files.txt -o files.txt