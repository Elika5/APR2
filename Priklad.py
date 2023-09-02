
class Priklad:

    def __init__(self,zadani,vysledek):
        self.zadani = zadani
        self.vysledek = vysledek
        self.uspesnost = 0

    def porovnani(self,vysledek_uzivatele):
        if self.vysledek == vysledek_uzivatele:
            self.uspesnost += 1
        else:
            pass