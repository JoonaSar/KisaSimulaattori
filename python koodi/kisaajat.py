
from vartio import Vartio
import matplotlib.pyplot as plt

class Kisaajat():
    
    def __init__(self, sarjakohtaiset_maarat, lahtoaika):
        self.vartiolista = list()
        vartiolkm = 0
        for sarja in sarjakohtaiset_maarat.keys():
            self.vartiolista.extend([Vartio(f'Vartio {vartiolkm}', vartiolkm, sarja, lahtoaika) for x in range(sarjakohtaiset_maarat[sarja])])
        
    def simuloi_rataosuus(self, rataosuus):
        self.vartiolista = rataosuus.simuloi(self.vartiolista)
    
    def plot_jonotusajat(self):
        fig, ax = plt.subplots(figsize=(10, 7), constrained_layout = True)
        ax.hist([vartio.jonotus_yht() for vartio in self.vartiolista], bins = 15)
        ax.set_xlabel("Jonotusaika yhteensä (min)")
        ax.set_ylabel("Vartiot")

    def plot_ajat(self):
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.hist([vartio.aika for vartio in self.vartiolista], bins = 15)
        ax.set_xlabel("Lähtemisaika rastilta (min)")
        ax.set_ylabel("Vartiot")
        ax.set_title("Vartioiden lähtemisaikojen jakauma")
