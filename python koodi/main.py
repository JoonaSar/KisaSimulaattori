from kisaajat import Kisaajat
from vartio import Vartio
from rataosuus import Kulku, Rasti
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    """sarjakohtaiset_maarat = {"punainen": 50, "keltainen": 50}

    kisaajat = Kisaajat(sarjakohtaiset_maarat, 0)
    
    rasti1 = Rasti("Rasti 1", 90, 1, 100)
    kulku1 = Kulku("Kulku 1", 120, 2, 100)
    rasti2 = Rasti("Rasti 2", 30, 1, 33)
    
    kisaajat.plot_ajat()
    kisaajat.simuloi_rataosuus(rasti1)
    kisaajat.plot_ajat()
    kisaajat.simuloi_rataosuus(kulku1)
    kisaajat.plot_ajat()
    kisaajat.simuloi_rataosuus(rasti2)
    kisaajat.plot_ajat()"""

if __name__ == "__main__":
    main()


def luo_kisa(kisan_nimi):
    p = Path("./saves")
    tallennetut_kisat = [f.name for f in p.iterdir() if f.is_file]
    if kisan_nimi in tallennetut_kisat:
        raise FileExistsError
    else:
        p = Path(f"./saves/{kisan_nimi}")
        p.touch()
        return 



