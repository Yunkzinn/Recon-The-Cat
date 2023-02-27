#!/bin/bash

echo "[+]-------------------Start Takeover-------------------[+]"

echo "[+]-------------------Subjack-------------------[+]"

subjack -w aliveSubs -t 100 -ssl -o subjack

echo "[+]-------------------Takeover-------------------[+]"

python3 ~/Tools/takeover/takeover.py -l aliveSubs -o takeover

echo "[+]-------------------Subzy-------------------[+]"

subzy --targets aliveSubs -hide_fails --verify_ssl -concurrency 20 | sort -u | tee subzy

echo "[+]-------------------Sending Notification-------------------[+]"

echo "Takeover Finished" | notify