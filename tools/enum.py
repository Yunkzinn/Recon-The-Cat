import os

domain = input("Domain to Search: ")
haktrails = f"{domain.split('.')[0]}_haktrails.txt"
assetfinder = f"{domain.split('.')[0]}_assetfinder.txt"
subfinder = f"{domain.split('.')[0]}_subfinder.txt"
amass = f"{domain.split('.')[0]}_amass.txt"
chaos = f"{domain.split('.')[0]}_chaos.txt"
githubHttpx = f"{domain.split('.')[0]}_githubHttpx.txt"
subfile = f"{domain.split('.')[0]}_subs.txt"
httpx = f"{domain.split('.')[0]}_httpx.txt"
httpx200 = f"{domain.split('.')[0]}_200httpx.txt"
awkHttpx = f"{domain.split('.')[0]}_awkhttpx.txt"
apiGitHub = "github_pat_AOMJNII04prEmFWLtL3H_SXWrrdWW0K967THW7IMNBfqse5LDDcPXkJ0zocer5JL2TD6QLRMDVBUQgqu"



os.system(f"echo {domain} | haktrails subdomains >> {haktrails}")
os.system(f"assetfinder -subs-only {domain} >> {assetfinder}")
os.system(f"subfinder -d {domain} -all -o {subfinder}")
os.system(f"amass enum -norecursive -passive -d {domain} -o {amass}")
os.system(f"chaos -d {domain} -silent -o {chaos}")
os.system(f"python3 ~/Tools/github-search/github-subdomains.py -t {apiGitHub} -d {domain} | httpx --title >> {githubHttpx}")
os.system(f"cat {haktrails} {assetfinder} {subfinder} {amass} {chaos} {githubHttpx} | sort -u {subfile} -o {subfile}")
os.system(f"cat {subfile} | httpx -silent -no-color -o {httpx}")
os.system(f"cat {subfile} | httpx -status-code -mc 200 -silent -no-color | tr -d '[]' | anew {httpx200}; cat {httpx200} | awk '{{print $1}}' >> {awkHttpx}; rm -rf {httpx200}; mv {awkHttpx} {httpx200}")
os.system(f"rm -rf {haktrails} {assetfinder} {subfinder} {amass} {chaos} {githubHttpx}")
