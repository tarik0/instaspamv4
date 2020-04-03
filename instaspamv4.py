# coding=utf-8
#!/usr/bin/env python3
from libs.check_modules import check_modules
from sys import exit
from os import _exit
check_modules()
from os import path
from libs.logo import print_logo
from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack

from multiprocessing import Process
from colorama import Fore, Back, Style

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

def video_attack(proxies):
    video_url = ask_question("Şikayet etmek istediğiniz videonun bağlantısını girniz")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". İşlem Açıldı!")
            if (k == 5): print()
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Video şikayeti saldırısı başlatılıyor!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". İşlem Açıldı!")
        if (k == 5): print()
        i = i + 1

def profile_attack(proxies):
    username = ask_question("Şikayet etmek istediğiniz kişinin kullanıcı adını giriniz")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". İşlem Açıldı!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Profil şikayeti saldırısı başlatılıyor!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process, args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". İşlem Açıldı!")
        if (k == 5): print()
        i = i + 1

def main():
    print_success("Modüller yüklendi!\n")

    ret = ask_question("Proxy kullanmak ister misiniz? [E/H]")

    proxies = []

    if (ret == "E" or ret == "e"):
        ret = ask_question("Proxylerinizi internetten toplamak ister misiniz? [E/H]")

        if (ret == "E" or ret == "e"):
            print_status("Internetten proxy toplanıyor! Bu biraz uzun sürebilir.\n")
            proxies = find_proxies()
        elif (ret == "H" or ret == "h"):
            print_status("Lütfen bir dosyada maksimum 50 proxy bulunsun!")
            file_path = ask_question("Proxy listenizin yolunu giriniz")
            proxies = parse_proxy_file(file_path)
        else:
            print_error("Cevap anlaşılamadı, çıkılıyor!")
            exit()

        print_success(str(len(proxies)) + " Adet proxy bulundu!\n")
    elif (ret == "H" or ret == "h"):
        pass
    else:
        print_error("Cevap anlaşılamadı, çıkılıyor!")
        exit()

    

    print("")
    print_status("1 - Profili şikayet et.")
    print_status("2 - Bir videoyu şikayet et.")
    report_choice = ask_question("Lütfen şikayet yöntemini seçin")
    print("")

    if (report_choice.isdigit() == False):
        print_error("Cevap anlaşılmadı.")
        exit(0)
    
    if (int(report_choice) > 2 or int(report_choice) == 0):
        print_error("Cevap anlaşılmadı.")
        exit(0)

    if (int(report_choice) == 1):
        profile_attack(proxies)
    elif (int(report_choice) == 2):
        video_attack(proxies)

if __name__ == "__main__":
    print_logo()
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[ * ] Program kapatılıyor!")
        print(Style.RESET_ALL)
        _exit(0)
