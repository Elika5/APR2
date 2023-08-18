class Databaze:
      def __init__(self,soubor,typ_testu):
            self.soubor = soubor
            self.typ_testu = typ_testu

      def otevreni_souboru(self):
            with open(self.soubor, "r") as soubor:
                  radky = soubor.readlines()
                  return radky
      
      def vyber_prikladu(self):
            radky = self.otevreni_souboru()
            return radky[5*self.typ_testu-5:5*self.typ_testu]

pokus = Databaze("ulohy.txt",1)
print(pokus)
            
      