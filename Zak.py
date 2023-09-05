from konfigura import config

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
    @jmeno.setter
    def jmeno(self, nove_jmeno):
        self._jmeno = nove_jmeno

    @property
    def prijmeni(self):
        return self._prijmeni
    @prijmeni.setter
    def prijmeni(self, nove_prijmeni):
        self._prijmeni = nove_prijmeni

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
            znamka1 = range(config["znamka1_min"],config["znamka1_max"]+1)
            znamka2 = range(config["znamka2_min"],config["znamka2_max"]+1)
            znamka3 = range(config["znamka3_min"],config["znamka3_max"]+1)
            znamka4 = range(config["znamka4_min"],config["znamka4_max"]+1)
            znamka5 = range(config["znamka5_min"],config["znamka5_max"]+1)
            znamky = {znamka1:1,znamka2:2,znamka3:3,znamka4:4,znamka5:5}
            vybrane_cislo = None
            for znamka_rozsah, cislo in znamky.items():
                if nove_data in znamka_rozsah:
                    vybrane_cislo = cislo
            self._znamka = vybrane_cislo
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
    
    