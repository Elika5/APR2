import re
import random

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


pokus = Databaze("ulohy.txt",2)
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
                 if tag.startswith("neznama"):
                       return str(random.randint(1, 100))
                 elif tag.startswith("neznama2"):
                        return str(random.randint(100, 200))
                 else:
                        return match.group()
            
            vzor = r'\[([^\]]+)\]'
            nahrazeni = re.sub(vzor,nahradit,self.ulohy)
            return nahradit


if __name__ == "__main__":
    input_text = pokus.radky
    replacer = Nahrazeni(input_text)
    replaced_text = replacer.nahrazeni()
    print(replaced_text)