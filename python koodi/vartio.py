
from numpy.core.fromnumeric import _ndim_dispatcher
from pandas.core.tools import numeric


class Vartio():
    
    # Vartion aika-parametri kuvaa ajankohtaa milloin kyseinen vartio saapuu simuloitavalle rataosuudelle

    def __init__(self, nimi, numero, sarja, aika):
        self.nimi = nimi
        self.numero = numero 
        self.sarja = sarja
        self.aika = aika
    
    
    def __str__(self):
        return f'{self.nimi}, {self.numero}, sarjassa {self.sarja}\n'

    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.aika < other.aika

    # TODO: Jonotuslista
    
