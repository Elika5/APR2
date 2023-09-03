import re
import random
import numpy as np
import statistics
import math
import sympy
import sys
from databaze import Databaze, Nahrazeni, Vysledek
from priklad import Priklad
from zak import Zak

def main():
    zadani = input("Zadej název souboru se zadáním (př. ulohy.txt):")
    while True:
        try:
            druh_testu = int(input("Zadej typ testu (1,2,3):"))
            if 0 < druh_testu < 4:
                break
            else:
                print("Tento typ není, zkus jinak.")
                continue
        except ValueError:
            print("Zadali jste neplatný vstup, zkus znovu.")
    data = Databaze(zadani,druh_testu)
    data.vyber_prikladu()
    jmeno = input("Zadej své jméno:")
    prijmeni = input("Zadej své přijmení:")
    radky = data.radky
    text = Nahrazeni(radky)
    nahrazene = text.nahrazeni()
    vysledky = Vysledek(text.hodnoty,druh_testu)
    vysledky = vysledky.vysledek()
    student = Zak(jmeno,prijmeni)
    cisilko = 0
    uspech = 0
    print(vysledky)
    for priklad in nahrazene:
        print(priklad)
        while True: 
            try:
                vysledek_studenta = float(input("Zadej svůj výsledek na tento příklad:"))
                break  
            except ValueError:
                print("Chyba: Zadali jste neplatný vstup, musí to být nějaké číslo. Zkuste to znovu.")
        priklad2 = Priklad(nahrazene[cisilko],vysledky[cisilko])
        print(priklad2.porovnani(vysledek_studenta))
        cisilko += 1
        uspech += priklad2.ziskat_uspesnost()
    student.prace_se_souborem(uspech)
    print(f"Získal jsi {student.ziskat_znamku()} a měl jsi {uspech}/5 bodů.")

if __name__ == "__main__":
    main()