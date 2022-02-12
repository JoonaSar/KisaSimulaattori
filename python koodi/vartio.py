
from numpy.core.fromnumeric import _ndim_dispatcher
from pandas.core.tools import numeric


class Vartio():
    
    # Vartion aika-parametri kuvaa ajankohtaa milloin kyseinen vartio saapuu simuloitavalle rataosuudelle

    def __init__(self, nimi, numero, sarja, aika):
        self.nimi = nimi
        self.numero = numero 
        self.sarja = sarja
        self.aika = aika
        self.historia = []
    
    
    def __str__(self):
        return f'{self.nimi}, {self.numero}, sarjassa {self.sarja}\n Kulkuhistoria kisan aikana: {repr(self.historia)}\n'

    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.aika < other.aika

    def jonotus_yht(self):
        jonotusta = 0
        jonossa = False
        for tapahtuma in self.historia:
            if jonossa:
                jonotusta += tapahtuma[2] - alkoi
                jonossa = False
            if tapahtuma[1] == "jonotus alkoi":
                jonossa = True
                alkoi = tapahtuma[2]
        return jonotusta
