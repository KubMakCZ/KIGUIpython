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

## Potřebné knihovny
* EasyTkinter - TKinter - GUI framework
* OS - volání systémových příkazů
* python3-nmap - nmap - (NetworkMAP) skenování sítě ()


!!!UPOZORNĚNÍ!!! není potřeba mít všechny balíčky co jsou v obrazku z PyCharm
![Python Intepret](https://raw.githubusercontent.com/KubMakCZ/KIGUIpython/main/Screenshot_184.png)
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

### Testovací soubory
+ tester.py - testovaní MultiWindow
+ tester2.py - testovani Fullscreen části
+ tester3.py - testovani roztažení tlačítek

------
+ Děkuji předem a snaď se vám bude libit můj projekt
+ student 3. ročníku Aplikované Informatiky na KI PřF UJEP
+ Jakub "KubMak" Škrabánek