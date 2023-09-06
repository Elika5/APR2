import sys
from konfigura import nacti_konfiguraci
config = nacti_konfiguraci()

class Databaze:
    def __init__(self,soubor):
        self._soubor = soubor
        self.radky = []

    @property
    def soubor(self):
        return self._soubor
    @soubor.setter
    def soubor(self, novy_soubor):
        self._soubor = novy_soubor

    def otevreni_souboru(self):
        try:
            with open(self.soubor, "r", encoding="UTF-8") as soubor:
                text = soubor.readlines()
                vysledne_zadani = [radek.strip() for radek in text]
                return vysledne_zadani
        except FileNotFoundError:
            print(f"Soubor {self.soubor} nebyl nalezen, byl zadán špatný soubor.")
            sys.exit()

            

    def vyber_prikladu(self):
        radky = self.otevreni_souboru()
        self.radky.extend(radky[0:config["pocet_uloh"]])


   
