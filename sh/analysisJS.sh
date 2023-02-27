echo "[+]-------------------Start JS Analysis-------------------[+]"

echo "[+]-------------------Collector and Secret Finder-------------------[+]"

cat aliveJustJS | python3 ~/Tools/python-tools/collector.py output ; rush -i output/urls.txt 'python3 ~/Tools/SecretFinder.py -i {} -o cli | sort -u >> output/resultJSPASS'

echo 'USE JSSCANER https://github.com/0x240x23elu/JSScanner'

echo "[+]-------------------Sending Notification-------------------[+]"

echo "JS Analysis Finished" | notify