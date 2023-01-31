import os

message =  ('''
Choose a Module :
1) Subdomains Enum
2) Complement Subs Enum
3) Endpoints Enum
4) Ips Enum
''')

def getOption(option):

    if option == 1:
        return os.system(f"python3 scripts/enum.py")

    elif option == 2:
        return os.system(f"bash scripts/complement.sh")

    elif option == 3:
        return os.system(f"python3 scripts/endpoints.py")

    elif option == 4:
        return os.system(f"python3 scripts/ips.py")

try:
    option = int(input(message)) 
    if not 0 < option < 5:
        raise ValueError
    print(getOption(option))

except:
    print("Choose a Valid Option")
