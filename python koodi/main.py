

#%%
from kisaajat import Kisaajat
from vartio import Vartio
from rataosuus import Kulku, Rasti
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
def main():
    sarjakohtaiset_maarat = {"punainen": 50, "keltainen": 50}

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
    kisaajat.plot_ajat()

if __name__ == "__main__":
    main()

# %%
