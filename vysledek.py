import math
import numpy as np
import statistics
import math
import sympy

class Vysledek:
    def __init__(self,hodnoty):
        self._hodnoty = hodnoty
        self._vysledky = {}

    @property
    def hodnoty(self):
        return self._hodnoty
    @hodnoty.setter
    def hodnoty(self, nove_hodnoty):
        self._hodnoty = nove_hodnoty

        
    @property
    def vysledky(self):
        return self._vysledky
    

    def vysledek(self):
        def zaokrouhleni(*cisla):
            return tuple(round(float(v), 2) if v is not None else None for v in cisla)
        

        try:
            self.vysledky['vysledek1'] = (self.hodnoty[0]*self.hodnoty[1]*self.hodnoty[2])/3
            self.vysledky['vysledek2'] = (self.hodnoty[4]*100)/self.hodnoty[3]
            self.vysledky['vysledek3'] = statistics.median(self.hodnoty[5])
            self.vysledky['vysledek4'] = np.dot(self.hodnoty[6], self.hodnoty[7])
            self.vysledky['vysledek5'] = self.hodnoty[10]*self.hodnoty[9]**(self.hodnoty[8]-1)
            x = sympy.symbols("x")
            derivace = sympy.diff(x*x + sympy.sin(2*x), x)
            self.vysledky['vysledek6'] = derivace.evalf(subs={x: self.hodnoty[11]})
            self.vysledky['vysledek7'] = (self.hodnoty[12]-self.hodnoty[13])*(self.hodnoty[12]/self.hodnoty[13])
            self.vysledky['vysledek8'] = statistics.median(self.hodnoty[14])
            self.vysledky['vysledek9'] = np.linalg.det(self.hodnoty[15])
            self.vysledky['vysledek10'] = (self.hodnoty[16]**2)/2
            self.vysledky['vysledek11'] = np.mean(self.hodnoty[17])
            self.vysledky['vysledek12'] = math.pi*self.hodnoty[18]*self.hodnoty[18]
            self.vysledky['vysledek13'] = (self.hodnoty[19]+self.hodnoty[20])-(self.hodnoty[19]*self.hodnoty[20])
            self.vysledky['vysledek14'] = self.hodnoty[21]*1000
            self.vysledky['vysledek15'] = math.pi*self.hodnoty[23]*(self.hodnoty[22]/2)**2
        except Exception as e:
            pass
        
        return zaokrouhleni(*self.vysledky.values())