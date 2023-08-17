import databaze
import random
import numpy as np

def generujPriklad(databaze):
    typPrikladu = random.randint(1,3)
    if typPrikladu==1:
        A=random.randint
        B=random.randint
        C=random.randint

    elif typPrikladu==2:
        pocet_cisel=random.randint(4,10)
        cislaPriklad=[]
        for i in range(pocet_cisel):
            cislaPriklad.append(random.randint)

    else:
        nahodna_matice = np.random.rand(3, 3)



