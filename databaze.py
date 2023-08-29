import re
import random
import numpy as np
import statistics
import math
import sympy

class Databaze:
      def __init__(self,soubor,typ_testu):
            self.soubor = soubor
            self.typ_testu = typ_testu
            self.radky = []

      def otevreni_souboru(self):
            with open(self.soubor, "r",encoding="UTF-8") as soubor:
                  text = soubor.readlines()
                  text2 = [radek.strip() for radek in text]
                  return text2
      
      def vyber_prikladu(self):
            radky = self.otevreni_souboru()
            self.radky.extend(radky[5*self.typ_testu-5:5*self.typ_testu])


pokus = Databaze("ulohy.txt",3)
pokus.vyber_prikladu()
#print(pokus.radky)   


class Nahrazeni:
    def __init__(self,ulohy):
        self.ulohy = ulohy
        self.hodnoty = []
            
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
                hodnota2 = random.randint(0, 500)
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



def vysledek(cisla,typ_testu):
      if typ_testu == 1:
          det = cisla[1]*cisla[1]-4*cisla[0]*cisla[2]
          vysledek1 = []
          if det ==0:
               vysledek1 = -cisla[1]/(cisla[0]*cisla[0])
          elif det > 0:
               vysledek1.append(str((-cisla[1]+math.sqrt(det))/(cisla[0]*cisla[0])))
               vysledek1.append(str((-cisla[1]-math.sqrt(det))/(cisla[0]*cisla[0])))
          else:
               vysledek1 = None   
          vysledek2 = (cisla[4]*100)/cisla[3]
          vysledek3 = statistics.mode(cisla[5])
          vysledek4 = np.dot(cisla[6],cisla[7])
          vysledek5 = cisla[10]*cisla[9]**(cisla[8]-1)
          return vysledek1, vysledek2, vysledek3, vysledek4, vysledek5
      elif typ_testu == 2:
          x = sympy.symbols("x")
          derivace = sympy.diff(x*x + sympy.sin(2*x),x)
          vysledek1 = derivace.evalf(subs={x: cisla[0]})
          vysledek2 = (cisla[1]-cisla[2])*(cisla[1]/cisla[2])
          vysledek3 = statistics.median(cisla[3])
          vysledek4 = np.linalg.det(cisla[4])
          vysledek5 = math.sqrt(math.sqrt(cisla[5]))*math.sqrt(math.sqrt(cisla[5]))
          return vysledek1, vysledek2, vysledek3, vysledek4, vysledek5
      elif typ_testu == 3:
          vysledek1 = np.mean(cisla[0])
          vysledek2 = math.pi*cisla[1]*cisla[1]
          vysledek3 = (cisla[2]+cisla[3])-(cisla[2]*cisla[3])
          vysledek4 = cisla[4]*1000
          det = cisla[1]*cisla[1]-4*cisla[0]*cisla[2]
          vysledek5 = []
          if det ==0:
               vysledek5 = -cisla[1]/(cisla[0]*cisla[0])
          elif det > 0:
               vysledek5.append(str((-cisla[1]+math.sqrt(det))/(cisla[0]*cisla[0])))
               vysledek5.append(str((-cisla[1]-math.sqrt(det))/(cisla[0]*cisla[0])))
          else:
               vysledek5 = None
          return vysledek1, vysledek2, vysledek3, vysledek4, vysledek5
      else:
          pass
     


if __name__ == "__main__":
    input_text = pokus.radky
    replacer = Nahrazeni(input_text)
    replaced_text = replacer.nahrazeni() 
    for uloha in replaced_text:
        print(uloha)
    hodnoty = replacer.hodnoty
    print(hodnoty)
    print(vysledek(hodnoty,3))