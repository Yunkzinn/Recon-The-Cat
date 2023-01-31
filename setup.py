import os

message =  ('''
Choose a Module :
1) Subdomains Enum
2) Complement Subs Enum
''')

def getOption(option):

    if option == 1:
        return os.system(f"python tools/enum.py")

    elif option == 2:
        return os.system(f"bash tools/complement.sh")
try:
    option = int(input(message)) 
    if not 0 < option < 3:
        raise ValueError
    print(getOption(option))

except:
    print("Choose a Valid Option")
