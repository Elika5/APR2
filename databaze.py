class Databaze:
      def __init__(self,soubor):
            self.soubor = soubor

      def otevreni_souboru(self):
            with open(self.soubor, "r") as soubor:
                  radky = soubor.readlines()
                  return radky
      