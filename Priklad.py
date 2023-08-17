import databaze
import random
import numpy as np

def generujPriklad(databaze):
    typPrikladu = random.randint(1,3)
    if typPrikladu==1:
         nezname = {
    "[neznama1]": random.randint,
    "[neznama2]": random.randint,
    "[neznama3]": random.randint,
}

    text="Vypočítejte rovnici [neznama1]x² + [neznama2]x + [neznama3] = 0"
    for neznama, nezname in nezname.items():
        zkouškaNovehoTextu = text.replace("[" + neznama + "]",nezname)

    elif typPrikladu==2:
        pocet_cisel=random.randint(4,12)
        cislaPriklad=[]
        for i in range(pocet_cisel):
            cislaPriklad.append(random.randint(1,3))

    else:
        nahodna_matice = np.random.rand(3, 3)



