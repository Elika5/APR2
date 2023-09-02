
class Zak:
    def __init__(self,jmeno,prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.soubor_nazev = f"{jmeno}_{prijmeni}.txt"
        self.znamky = {}

    def prace_se_souborem(self,nove_data):
        try:
            with open(self.soubor_nazev, "r", encoding="UTF-8") as soubor:
                obsah = soubor.read()
        except FileNotFoundError:
            obsah = ""

        with open(self.soubor_nazev, "w", encoding="UTF-8") as soubor:
            if obsah:
                soubor.write(f"{obsah}, {nove_data}:{nove_data}/5")
            else:
                soubor.write(f"{self.jmeno} {self.prijmeni} - znamky a statistiky\n")
                soubor.write(f"{nove_data}:{nove_data}/5")
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
    