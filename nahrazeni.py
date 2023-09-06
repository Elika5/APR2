import re
import random
import numpy as np
from konfigura import nacti_konfiguraci
config = nacti_konfiguraci()

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
                hodnota1 = random.randint(config["neznama_min"], config["neznama_max"])
                self.hodnoty.append(hodnota1)
                return str(hodnota1)
            elif tag == "neznama2":
                hodnota2 = random.randint(config["neznama2_min"], config["neznama2_max"])
                self.hodnoty.append(hodnota2)
                return str(hodnota2)
            elif tag == "neznama3":
                hodnota3 = random.randint(config["neznama3_min"], config["neznama3_max"])
                self.hodnoty.append(hodnota3)
                return str(hodnota3)
            elif tag == "matice":
                matice = np.random.randint(config["matice_min"], config["matice_max"], size=(config["matice_velikost"], config["matice_velikost"]))
                self.hodnoty.append(matice)
                return str(matice)
            elif tag == "cisla":
                seznam_cisel = [random.randint(config["cisla_min"], config["cisla_max"]) for _ in range(config["cisla_pocet"])]
                self.hodnoty.append(seznam_cisel)
                return str(seznam_cisel)
            elif tag == "vektor":
                seznam_cisel = [random.randint(config["vektor_min"], config["vektor_max"]) for _ in range(config["vektor_pocet"])]
                self.hodnoty.append(seznam_cisel)
                return str(seznam_cisel)
            else:
                return match.group()
            
        vzor = r'\[([^\]]+)\]'
        nahrazeni = [re.sub(vzor, nahradit, uloha) for uloha in self.ulohy]
        return nahrazeni