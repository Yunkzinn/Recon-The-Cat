#!/bin/bash

# Domínio de entrada
echo "Insira o domínio a ser enumerado:"
read domain

# Utiliza o Sublist3r para encontrar subdomínios
echo "Buscando subdomínios com o Sublist3r..."
python3 /path/to/sublist3r.py -d $domain -o sublist3r_output.txt

# Utiliza o Amass para encontrar subdomínios adicionais
echo "Buscando subdomínios adicionais com o Amass..."
amass enum -d $domain -o amass_output.txt

# Utiliza o knockpy para encontrar subdomínios adicionais
echo "Buscando subdomínios adicionais com o knockpy..."
knockpy $domain > knockpy_output.txt

# Utiliza o Assetfinder para encontrar subdomínios adicionais
echo "Buscando subdomínios adicionais com o Assetfinder..."
assetfinder --subs-only $domain > assetfinder_output.txt

# Utiliza o Subfinder para encontrar subdomínios adicionais
echo "Buscando subdomínios adicionais com o Subfinder..."
subfinder -d $domain -o subfinder_output.txt

# Junta os resultados de todas as ferramentas em um único arquivo
echo "Juntando todos os resultados em um único arquivo..."
cat sublist3r_output.txt amass_output.txt knockpy_output.txt assetfinder_output.txt subfinder_output.txt | sort -u > subs.txt

# Remover duplicados e salva em arquivo
sort -u subs.txt -o subs.txt

# Utiliza o httpx para verificar quais subdomínios retornam código de status HTTP 200
echo "Verificando quais subdomínios retornam código de status HTTP 200..."
httpx -status-code -threads 100 -timeout 5 -input-file subs.txt -o 200subs.txt
