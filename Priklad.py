
class Priklad:

    def __init__(self,zadani,vysledek):
        self.zadani = zadani
        self._vysledek = vysledek
        self._uspesnost = 0

    @property
    def vysledek(self):
        return self._vysledek
    

    def porovnani(self,vysledek_uzivatele):
        if self._vysledek == vysledek_uzivatele:
           self._uspesnost += 1
           return "Správný výsledek."
        else:
            return "Špatný výsledek"

    def ziskat_uspesnost(self):
        return self._uspesnost
