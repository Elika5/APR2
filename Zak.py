
class Zak:
    def _init__(self,jmeno,prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.soubor_nazev = f"{jmeno}_{prijmeni}.txt"
        self.znamky = {}

    def hodnoceni(self,znamka):
        self.znamky.append(znamka)

    def prace_se_souborem(self):
        try:
            with open(self.soubor_nazev, "r", encoding="UTF-8") as soubor:
                obsah = soubor.read()
                print(f"Obsah souboru {self.soubor_nazev}:")
                print(obsah)
                self.udaje = self.obsah_na_slovnik(obsah)
        except FileNotFoundError:
            print(f"Soubor {self.soubor_nazev} nebyl nalezen. Vytvářím nový soubor...")
            with open(self.soubor_nazev, "w", encoding="UTF-8") as soubor:
                soubor.write(f"{self.jmeno} {self.prijmeni} - znamky a statictiky\n")
                print(f"Nový soubor {self.soubor_nazev} byl vytvořen.")

    def obsah_na_slovnik(self, obsah):
        slovnik = {}
        radky = obsah.strip().split("\n")
        for radek in radky[1:]: 
            klice_a_hodnoty = radek.split(",")
            for klic_a_hodnota in klice_a_hodnoty:
                klic, hodnota = klic_a_hodnota.split(":")
                slovnik[klic.strip()] = hodnota.strip()
        return slovnik
    