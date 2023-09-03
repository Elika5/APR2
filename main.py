import re
import random
import numpy as np
import statistics
import math
import sympy
from databaze import Databaze, Nahrazeni, Vysledek
from priklad import Priklad
from zak import Zak

def main():
    zadani = input("Zadej název souboru se zadáním (př. ulohy.txt):")
    druh_testu = int(input("Zadej typ testu (1,2,3):"))
    jmeno = input("Zadej své jméno:")
    prijmeni = input("Zadej své přijmení:")
    data = Databaze(zadani,druh_testu)
    data.vyber_prikladu()
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
        vysledek_studenta = float(input("Zadej svůj výsledek na tento příklad:"))
        priklad2 = Priklad(nahrazene[cisilko],vysledky[cisilko])
        print(priklad2.porovnani(vysledek_studenta))
        cisilko+=1
        uspech += priklad2.uspesnost
    student.prace_se_souborem(uspech)
    print(f"Získal jsi {student.ziskat_znamku()} a měl jsi {uspech}/5 bodů.")

if __name__ == "__main__":
    main()