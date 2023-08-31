
class Zak:
    def _init__(self,jmeno,prijmeni,znamky):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.znamky = znamky
        self.soubor_nazev = f"{jmeno}_{prijmeni}.txt"

    def hodnoceni(self,znamka):
        self.znamky.append(znamka)

    def otevri_nebo_vytvor_soubor(self):
        try:
            with open(self.soubor_nazev, "r", encoding="UTF-8") as soubor:
                obsah = soubor.read()
                print(f"Obsah souboru {self.soubor_nazev}:")
                print(obsah)
        except FileNotFoundError:
            print(f"Soubor {self.soubor_nazev} nebyl nalezen. Vytvářím nový soubor...")
            with open(self.soubor_nazev, "w", encoding="UTF-8") as soubor:
                print(f"Nový soubor {self.soubor_nazev} byl vytvořen.")
    