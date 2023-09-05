import re
import random
import numpy as np

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