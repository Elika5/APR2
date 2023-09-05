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


   
