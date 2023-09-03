
class Zak:
    def __init__(self,jmeno,prijmeni):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._soubor_nazev = f"{jmeno}_{prijmeni}.txt"
        self._znamky = {}
        self._znamka = 0

    @property
    def jmeno(self):
        return self._jmeno

    @property
    def prijmeni(self):
        return self._prijmeni

    @property
    def soubor_nazev(self):
        return self._soubor_nazev
    
    @property
    def znamky(self):
        return self._znamky
    
    @property 
    def znamka(self):
        return self._znamka
    
    def prace_se_souborem(self,nove_data):
        try:
            with open(self._soubor_nazev, "r", encoding="UTF-8") as soubor:
                obsah = soubor.read()
        except FileNotFoundError:
            obsah = ""

        with open(self._soubor_nazev, "w", encoding="UTF-8") as soubor:
            if nove_data == 5:
                self._znamka = 1
            elif nove_data == 4:
                self._znamka = 2
            elif nove_data == 3:
                self._znamka = 3
            elif nove_data == 2:
                self._znamka = 4
            else:
                self._znamka = 5
            if obsah:
                soubor.write(f"{obsah}, {self.znamka}:{nove_data}/5")
            else:
                soubor.write(f"{self._jmeno} {self._prijmeni} - znamky a statistiky\n")
                soubor.write(f"{self._znamka}:{nove_data}/5")
        self.udaje = self.obsah_na_slovnik(obsah)
    
                
    def obsah_na_slovnik(self, obsah):
        slovnik = {}
        radky = obsah.strip().split("\n")
        for radek in radky[1:]: 
            klice_a_hodnoty = radek.split(",")
            for klic_a_hodnota in klice_a_hodnoty:
                klic, hodnota = klic_a_hodnota.split(":")
                slovnik[klic.strip()] = hodnota.strip()
        return slovnik
    
    def ziskat_znamku(self):
        return self._znamka