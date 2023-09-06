from databaze import Databaze
from nahrazeni import Nahrazeni
from vysledek import Vysledek
from priklad import Priklad
from zak import Zak
from konfigura import nacti_konfiguraci
config = nacti_konfiguraci()

def main():    
    data = Databaze(config["soubor_zadani"])
    data.vyber_prikladu()
    jmeno = input("Zadej své jméno:")
    prijmeni = input("Zadej své přijmení:")
    radky = data.radky
    text = Nahrazeni(radky)
    nahrazene = text.nahrazeni()
    vysledky = Vysledek(text.hodnoty)
    vysledky = vysledky.vysledek()
    student = Zak(jmeno,prijmeni)
    postup = 0
    uspech = 0
    print(vysledky)
    print("Výsledky zadávej se zaokrouhlením na dvě desetinná místa.")
    for priklad in nahrazene:
        print(f"{postup}. {priklad}")
        while True: 
            try:
                vysledek_studenta = float(input("Zadej svůj výsledek na tento příklad:"))
                break  
            except ValueError:
                print("Chyba: Zadali jste neplatný vstup, musí to být nějaké číslo. Zkuste to znovu.")
        priklad2 = Priklad(nahrazene[postup],vysledky[postup])
        print(priklad2.porovnani(vysledek_studenta))
        postup += 1
        uspech += priklad2.ziskat_uspesnost()
    student.prace_se_souborem(uspech)
    pocet = config["pocet_uloh"]
    print(f"Získal jsi {student.ziskat_znamku()} a měl jsi {uspech}/{pocet} bodů.")

if __name__ == "__main__":
    main()