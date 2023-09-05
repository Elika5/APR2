import math
import numpy as np
import statistics
import math
import sympy

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