import subprocess

# Obtém o domínio de entrada
domain = input("Insira o domínio a ser enumerado:")

# Utiliza o Sublist3r para encontrar subdomínios
print("Buscando subdomínios com o Sublist3r...")
subprocess.run(["python3", "/path/to/sublist3r.py", "-d", domain, "-o", "sublist3r_output.txt"])

# Utiliza o Amass para encontrar subdomínios adicionais
print("Buscando subdomínios adicionais com o Amass...")
subprocess.run(["amass", "enum", "-d", domain, "-o", "amass_output.txt"])

# Utiliza o knockpy para encontrar subdomínios adicionais
print("Buscando subdomínios adicionais com o knockpy...")
with open("knockpy_output.txt", "w") as f:
    subprocess.run(["knockpy", domain], stdout=f)

# Utiliza o Assetfinder para encontrar subdomínios adicionais
print("Buscando subdomínios adicionais com o Assetfinder...")
subprocess.run(["assetfinder", "--subs-only", domain, ">", "assetfinder_output.txt"])

# Utiliza o Subfinder para encontrar subdomínios adicionais
print("Buscando subdomínios adicionais com o Subfinder...")
subprocess.run(["subfinder", "-d", domain, "-o", "subfinder_output.txt"])

# Junta os resultados de todas as ferramentas em um único arquivo
print("Juntando todos os resultados em um único arquivo...")
subprocess.run(["cat", "sublist3r_output.txt", "amass_output.txt", "knockpy_output.txt", "assetfinder_output.txt", "subfinder_output.txt", "|", "sort", "-u", ">", "subs.txt"])

# Remover duplicatas e salvar em arquivo
with open("subs.txt", "r") as f:
    lines = set(f.readlines())
with open("subs.txt", "w") as f:
    f.writelines(lines)

# Utiliza o httpx para verificar quais subdomínios retornam código de status HTTP 200
print("Verificando quais subdomínios retornam código de status HTTP 200...")
subprocess.run(["httpx", "-status-code", "-threads", "100", "-timeout", "5", "-input-file", "subs.txt", "-o", "200subs.txt"])