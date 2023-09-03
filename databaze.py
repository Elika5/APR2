import re
import random
import numpy as np
import statistics
import math
import sympy
import sys

class Databaze:
    def __init__(self,soubor,typ_testu):
        self._soubor = soubor
        self._typ_testu = typ_testu
        self.radky = []

    @property
    def soubor(self):
        return self._soubor
    @soubor.setter
    def soubor(self, novy_soubor):
        self._soubor = novy_soubor

    @property
    def typ_testu(self):
        return self._typ_testu
    @typ_testu.setter
    def typ_testu(self, novy_typ_testu):
        self._typ_testu = novy_typ_testu

    def otevreni_souboru(self):
        try:
            with open(self.soubor, "r", encoding="UTF-8") as soubor:
                text = soubor.readlines()
                text2 = [radek.strip() for radek in text]
                return text2
        except FileNotFoundError:
            print(f"Soubor {self.soubor} nebyl nalezen, spusť znovu s jiným názvem souboru.")
            sys.exit()

            

    def vyber_prikladu(self):
        radky = self.otevreni_souboru()
        self.radky.extend(radky[5*self.typ_testu-5:5*self.typ_testu])


class Nahrazeni:
    def __init__(self,ulohy):
        self._ulohy = ulohy
        self.hodnoty = []

    @property
    def ulohy(self):
        return self._ulohy
    @ulohy.setter
    def ulohy(self, nove_ulohy):
        self._ulohy = nove_ulohy

    def hledani_vyrazu(self):
        vzor = r'\[[^\]]+\]'
        hledani = re.findall(vzor, self.ulohy)
        pocet = {match: len(match.split()) for match in hledani}
        return pocet
      
    def nahrazeni(self):
        def nahradit(match):
            tag = match.group(1)
            if tag == "neznama":
                hodnota1 = random.randint(-11, 11)
                self.hodnoty.append(hodnota1)
                return str(hodnota1)
            elif tag == "neznama2":
                hodnota2 = random.randint(0, 300)
                self.hodnoty.append(hodnota2)
                return str(hodnota2)
            elif tag == "neznama3":
                hodnota3 = random.randint(0, 30)
                self.hodnoty.append(hodnota3)
                return str(hodnota3)
            elif tag == "matice":
                matice = np.random.randint(-10, 10, size=(3, 3))
                self.hodnoty.append(matice)
                return str(matice)
            elif tag == "cisla":
                seznam_cisel = [random.randint(-100, 100) for _ in range(7)]
                self.hodnoty.append(seznam_cisel)
                return str(seznam_cisel)
            elif tag == "vektor":
                seznam_cisel = [random.randint(-100, 100) for _ in range(5)]
                self.hodnoty.append(seznam_cisel)
                return str(seznam_cisel)
            else:
                return match.group()
            
        vzor = r'\[([^\]]+)\]'
        nahrazeni = [re.sub(vzor, nahradit, uloha) for uloha in self.ulohy]
        return nahrazeni
     

class Vysledek:
    def __init__(self,hodnoty,typ_testu):
        self._hodnoty = hodnoty
        self._typ_testu = typ_testu

    @property
    def hodnoty(self):
        return self._hodnoty
    @hodnoty.setter
    def hodnoty(self, nove_hodnoty):
        self._hodnoty = nove_hodnoty

    @property
    def typ_testu(self):
        return self._typ_testu
    @typ_testu.setter
    def typ_testu(self, novy_typ_testu):
        self._typ_testu = novy_typ_testu

    def vysledek(self):
        def zaokrouhleni(*cisla):
            return tuple(round(float(v), 2) if v is not None else None for v in cisla)
        
        if self.typ_testu == 1:
            vysledek1 = (self.hodnoty[0]*self.hodnoty[1]*self.hodnoty[2])/3
            vysledek2 = (self.hodnoty[4]*100)/self.hodnoty[3]
            vysledek3 = statistics.median(self.hodnoty[5])
            vysledek4 = np.dot(self.hodnoty[6],self.hodnoty[7])
            vysledek5 = self.hodnoty[10]*self.hodnoty[9]**(self.hodnoty[8]-1)
            return zaokrouhleni(vysledek1, vysledek2, vysledek3, vysledek4, vysledek5)
        elif self.typ_testu == 2:
            x = sympy.symbols("x")
            derivace = sympy.diff(x*x + sympy.sin(2*x),x)
            vysledek1 = derivace.evalf(subs={x: self.hodnoty[0]})
            vysledek2 = (self.hodnoty[1]-self.hodnoty[2])*(self.hodnoty[1]/self.hodnoty[2])
            vysledek3 = statistics.median(self.hodnoty[3])
            vysledek4 = np.linalg.det(self.hodnoty[4])
            vysledek5 = math.sqrt(math.sqrt(self.hodnoty[5]))*math.sqrt(math.sqrt(self.hodnoty[5]))
            return zaokrouhleni(vysledek1, vysledek2, vysledek3, vysledek4, vysledek5)
        elif self.typ_testu == 3:
            vysledek1 = np.mean(self.hodnoty[0])
            vysledek2 = math.pi*self.hodnoty[1]*self.hodnoty[1]
            vysledek3 = (self.hodnoty[2]+self.hodnoty[3])-(self.hodnoty[2]*self.hodnoty[3])
            vysledek4 = self.hodnoty[4]*1000
            vysledek5 = math.pi*self.hodnoty[6]*(self.hodnoty[5]/2)**2
            return zaokrouhleni(vysledek1, vysledek2, vysledek3, vysledek4, vysledek5)
        else:
            pass
        
     