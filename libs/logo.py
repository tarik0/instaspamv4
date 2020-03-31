# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
     ____  ____   _____ ______   ____  _____ ____   ____  ___ ___ 
    |    ||    \ / ___/|      | /    |/ ___/|    \ /    ||   |   |
     |  | |  _  (   \_ |      ||  o  (   \_ |  o  )  o  || _   _ |
     |  | |  |  |\__  ||_|  |_||     |\__  ||   _/|     ||  \_/  |
     |  | |  |  |/  \ |  |  |  |  _  |/  \ ||  |  |  _  ||   |   |
     |  | |  |  |\    |  |  |  |  |  |\    ||  |  |  |  ||   |   |
    |____||__|__| \___|  |__|  |__|__| \___||__|  |__|__||___|___|v4"""

youtube_urls = [
    "Süpriz - https://www.youtube.com/watch?v=G0STVKbQEaQ",
    "Babaların İnfazı - https://www.youtube.com/watch?v=DmkoBPxyyeo",
    "Polat Ve Testere Türk Ruleti - https://www.youtube.com/watch?v=GPa85nu0-ho",
    "Biat Edin - https://www.youtube.com/watch?v=GFCczMrKa28",
    "Kötü Köpek Sürüye Kurt Getirdi - https://www.youtube.com/watch?v=tNYF-g1u5_Q",
    "Sadece Ölüler Görür - https://www.youtube.com/watch?v=N_1l_au1nJA",
    "Seyfo Dayı, Çakır ve Polat'a Alemi Anlatıyor - https://www.youtube.com/watch?v=0YarjcwVyqs",
    "Memati Cerrahpaşalıların mekanında - https://www.youtube.com/watch?v=6TdIQ6gO1fM",
    "Laz Ziya Testere Necmi'nin Mekanını Basıyor - https://www.youtube.com/watch?v=qeP8ZxXW8tc",
    "Laz Ziya'dan Baron'a Racon - https://www.youtube.com/watch?v=qZiydYE4dUo",
    "Süleyman Çakır ''Erkek adam küpe takmaz'' - https://www.youtube.com/watch?v=Q7WpI6Ekx84",
    "Polat ve Çakır Tombalacıya Posta Koyuyor - https://www.youtube.com/watch?v=UxXEkXvgFb0",
    "Tombalacının İnfazı - https://www.youtube.com/watch?v=VmIDGYLsucU",
    "Abuzer Kömürcü Tüm Sahneler - https://www.youtube.com/watch?v=xTJav-ar6IQ",
    "Seyfo Dayı - https://www.youtube.com/watch?v=8JJa4gXkD-Y"
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Yapımcı: Hichigo THT"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Telegramdan fikri veren ve aynı zamanda söven arkadaşa teşekkür ediyorum.")
    print ("\n", "-> Gaz maskesiyle gül koklamayanalara özel:\n    " + choice(youtube_urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
