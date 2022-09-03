from rataosuus import Rasti, Kulku

class Kisa():

    def __init__(self, nimi, kisaajat, rataosuudet = []):
        self.nimi = nimi
        self.kisaajat = kisaajat
        self.rataosuudet = rataosuudet
    
    def lisaa_rataosuus(self, rataosuus):
        self.rataosuudet.append(rataosuus)

    def simuloi_kisa(self):
        for rataosuus in self.rataosuudet:
            self.kisaajat.simuloi(rataosuus)
        
