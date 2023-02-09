import os

aliveJustJS = os.system(f"cat aliveJustJS")
resultJSPASS = f"resultJSPASS"

os.system(f"cat {aliveJustJS} | python3 ~/python-tools/collector.py output ; rush -i output/urls.txt 'python3 ~/python-tools/SecretFinder.py -i {{}} -o cli | sort -u >> output/{resultJSPASS}'")
os.system(f"echo 'USE JSScanner https://github.com/0x240x23elu/JSScanner'")

