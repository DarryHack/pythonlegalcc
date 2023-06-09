import os
import webbrowser
import os.path
import subprocess
from termcolor import colored
from pystyle import *
import ctypes
import urllib
import time
import urllib.request


ctypes.windll.kernel32.SetConsoleTitleA("DarryHack")



# Yeni başlık adını belirleyin
yeni_baslik = "DarryHack :)"



url = "https://github.com/DarryHack/pythonlegalcc/pythonlegalcc.py"
filename = "pythonlegalcc.py"

def check_file():
    print("Kodun guncel olup olunmadigi kontrol ediliyor..")
    urllib.request.urlretrieve(url, "temp")
    if not os.path.exists(filename):
        return True
    else:
        with open("temp", "r") as f1, open(filename, "r") as f2:
            if f1.read() == f2.read():
                return False
            else:
                return True
    os.remove("temp")



def update_file():
    print("Kod guncelleniyor..")
    urllib.request.urlretrieve(url, filename)


if check_file():
    update_file()
    print("Kod Guncel")
    time.sleep(3)


def consoleclear():
    os.system('cls')



blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_blue, Col.white, Col.white))
red = Col.light_red
lred = Colors.StaticMIX((Col.light_red, Col.white, Col.white))
green = Col.light_green
lgreen = Colors.StaticMIX((Col.light_green, Col.white, Col.white))

def stage(text: str, symbol: str = '...') -> str:
    if symbol == '...':
      return f""" {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""
    elif symbol == "!":
        return f""" {Col.Symbol(symbol, lred, red)} {red}{text}{Col.reset}"""
    elif symbol == "x":
        return f""" {Col.Symbol(symbol, lgreen, green)} {green}{text}{Col.reset}"""
    else:
      return f""" {Col.Symbol(symbol, blue, lblue)} {blue}{text}{Col.reset}"""

urllist= []
    
while True:
    
    url = ""
    if url in urllist:
        pass
    else:
        consoleclear()
        print(stage(f"1 - Ad Soyad Sorgu", "!"))
        print(stage(f"2 - GSM Sorgu", "!"))
        print(stage(f"3 - TC Sorgu", "!"))
        print(stage(f"4 - Aile Sorgu", "!"))
        print(stage(f"5 - GSM TC Sorgu", "!"))
        print(stage(f"6 - Adres Sorgu", "!"))    
        print(stage(f"7 - E Okul Sorgu", "!"))
        print(stage(f"8 - Discord", "!"))
        print(stage(f"9 - Youtube", "!"))
        secim = input("Seciminiz: ")

    if secim == "1":
        subprocess.run(["python", "adsoyad.py"])
    elif secim == "2":
        subprocess.run(["python", "gsm.py"])
    elif secim == "3":
        subprocess.run(["python", "tc.py"])
    elif secim == "4":
        subprocess.run(["python", "eokul.py"])
    elif secim == "5":
        subprocess.run(["python", "gsmtc.py"])
    elif secim == "7":
        webbrowser.open("https://www.youtube.com/@Darry1453")
    elif secim == "6":
        subprocess.run(["python", "adres.py"])
    elif secim == "8":
        webbrowser.open("https://discord.gg/kYVGc36VzZ")
    else:
        consoleclear()
        print("Hatalı seçim.")
