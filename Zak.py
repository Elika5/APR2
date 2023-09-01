
class Zak:
    def _init__(self,jmeno,prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.soubor_nazev = f"{jmeno}_{prijmeni}.txt"
        self.znamky = {}

    def prace_se_souborem(self,nove_data):
        try:
            with open(self.soubor_nazev, "a", encoding="UTF-8") as soubor:
                obsah = soubor.read()
                soubor.write(f", {nove_data}:{nove_data}/5")
                self.udaje = self.obsah_na_slovnik(obsah)
        except FileNotFoundError:
            with open(self.soubor_nazev, "w", encoding="UTF-8") as soubor:
                soubor.write(f"{self.jmeno} {self.prijmeni} - znamky a statictiky\n")
                soubor.write(f"{nove_data}:{nove_data}/5")
                self.udaje = {nove_data:f"{nove_data}/5"}
                
    def obsah_na_slovnik(self, obsah):
        slovnik = {}
        radky = obsah.strip().split("\n")
        for radek in radky[1:]: 
            klice_a_hodnoty = radek.split(",")
            for klic_a_hodnota in klice_a_hodnoty:
                klic, hodnota = klic_a_hodnota.split(":")
                slovnik[klic.strip()] = hodnota.strip()
        return slovnik
    