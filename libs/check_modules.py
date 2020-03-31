# coding=utf-8
#!/usr/bin/env python3

import sys

def check_modules():
    try:
        import requests
    except:
        print("[-] 'requests' paketi yüklü değil!")
        print("[*] Yüklemek için 'pip install requests[socks]' yazın!")
        sys.exit(0)

    try:
        import colorama
    except:
        print("[-] 'colorama' paketi yüklü değil!")
        print("[*] Yüklemek için 'pip install colorama' yazın!")
        sys.exit(0)

    try:
        import asyncio
    except:
        print("[-] 'asyncio' paketi yüklü değil!")
        print("[*] Yüklemek için 'pip install asyncio' yazın!")
        sys.exit(0)

    try:
        import proxybroker
    except:
        print("[-] 'proxybroker' paketi yüklü değil!")
        print("[*] Yüklemek için 'pip install proxybroker' yazın!")
        sys.exit(0)

    try:
        import warnings
    except:
        print("[-] 'warnings' paketi yüklü değil!")
        print("[*] Yüklemek için 'pip install warnings' yazın!")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()