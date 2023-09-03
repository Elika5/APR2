
class Priklad:

    def __init__(self,zadani,vysledek):
        self.zadani = zadani
        self._vysledek = vysledek
        self._uspesnost = 0

    @property
    def vysledek(self):
        return self._vysledek
    @vysledek.setter
    def vysledek(self, novy_vysledek):
        self._vysledek = novy_vysledek

    @property
    def uspesnost(self):
        return self._uspesnost
    @uspesnost.setter
    def uspesnost(self, hodnota):
        if not isinstance(hodnota, int):
            raise ValueError("Uspesnost musí být celé číslo")
        self._uspesnost = hodnota

    def porovnani(self,vysledek_uzivatele):
        if self._vysledek == vysledek_uzivatele:
           self._uspesnost += 1
        else:
            print("špatně")

    @classmethod
    def vytvor_priklad(cls, zadani, vysledek):
        return cls(zadani, vysledek)