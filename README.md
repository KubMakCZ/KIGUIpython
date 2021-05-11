# Python Dashboard
## jednoduche GUI pro ovládání
Jedná se o jednoduchou aplikaci k představení malého programu na ovladaní některých
činností na Rasbperry Pi (RPi) za pomocí malé dotykové obrazovky.
Program by měl být i CrossPlatform díky Pythonu (v projektu používaný 3.8). 
Aplikace jako taková pro sestavení  by měla být funkční jako widget na OS Windows 
a jako Fullscreen aplikace na Linuxu (RPi používa Rasbperry Pi OS postavený na debianu).



------
## Features:
* počasí
* skenování síte
* vypínaní zapínání
    * PC
    * Senzoru
    * Programu v PC
* cteni hodnot ze senzoru
* monitoring systému
* text editor

## Potřebné knihovny + programy

#### knihovny
bude potřeba stahnout a nainstalovat 
- [NMAP](https://nmap.org/download.html) - [win32stable](https://nmap.org/dist/nmap-7.91-setup.exe) - aplikace spoustejici se s knihovnou python-nmap [Ukazky kodu](https://www.programcreek.com/python/example/92225/nmap.PortScanner)

#### knihovny
* EasyTkinter - TKinter - GUI framework
* OS - volání systémových příkazů
* sys - Specifické parametry a funkce O 
* python-nmap - nmap - (NetworkMAP) skenování sítě (UPOZORNENÍ = nestahovat knihonu "nmap", jedna se o uplne jinou knihovnu (knihovna na numbers map))
* python3-nmap - lepsi nmap pro python3


!!!UPOZORNĚNÍ!!! není potřeba mít všechny balíčky co jsou v obrazku z PyCharm
![Python Intepreter](https://raw.githubusercontent.com/KubMakCZ/KIGUIpython/main/Screenshot_184.png)
!!!UPOZORNĚNÍ!!! není potřeba mít všechny balíčky co jsou v obrazku z PyCharm

------
## Postup:
+ Prezentace - Raspberry pi
+ seznámení v TKinter s postupným prostředím (jednotlive soubory part1.py, part2.py, atd,)
+ Vytvořením dashboardu
  + funkce pro zjištění OS
  + fullscreen a nastavení GRID systemu 
+ vytvoření okna na jednoduche CMD příkazy
+ vytvoření okna pro počasí
+ vytvoření okna pro text editing

------
## files
#### Hlavní soubory pro prezentaci
- part1.py - jednoduche vypsani OS
- part2.py - zakladní dashboard s tlačítky
- part3.py - text editor
- part4.py - nmap sken site v okne (pripraveno na implementovani do dashboardu)

### Testovací soubory
+ tester.py - testovaní MultiWindow
+ tester2.py - testovani Fullscreen části
+ tester3.py - testovani roztažení tlačítek
+ tester4.py - testovani rozlozeni v Grid systemu
+ nmap-scan.py - skenovani protocolu na localhostu
+ tester5.py - skenovani síte
+ tester6.py - vypis do okna 

------
+ Děkuji předem a snaď se vám bude libit můj projekt
+ student 3. ročníku Aplikované Informatiky na KI PřF UJEP
+ Jakub "KubMak" Škrabánek