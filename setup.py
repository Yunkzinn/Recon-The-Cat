import os

ascii = ('''
     _____                        _______ _             _____      _   
    |  __ \                      |__   __| |           / ____|    | |  
    | |__) |___  ___ ___  _ __      | |  | |__   ___  | |     __ _| |_ 
    |  _  // _ \/ __/ _ \| '_ \     | |  | '_ \ / _ \ | |    / _` | __|
    | | \ \  __/ (_| (_) | | | |    | |  | | | |  __/ | |___| (_| | |_ 
    |_|  \_\___|\___\___/|_| |_|    |_|  |_| |_|\___|  \_____\__,_|\__|
''')                                                                    

print(ascii)                                                                    

github = ('''
    Made by https://github.com/Yunkzinn with ❤️
''')

print(github)

message =  ('''
    Choose a Module :
    1) Subdomains Enum
    2) Complement Subs Enum
    3) Endpoints Enum
    4) Subs Takeover
''')

def getOption(option):

    if option == 1:
        return os.system(f"python3 scripts/enum.py")

    elif option == 2:
        return os.system(f"bash scripts/complement.sh")

    elif option == 3:
        return os.system(f"python3 scripts/endpoints.py")

    elif option == 4:
        return os.system(f"python3 scripts/takeover.py")

try:
    option = int(input(message)) 
    if not 0 < option < 5:
        raise ValueError    
    print(getOption(option))

except:
    print("    Choose a Valid Option")

#Future Updates:    
#All in one archive