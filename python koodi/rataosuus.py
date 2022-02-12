from scipy.stats import gamma
from logi import Logi

class Rataosuus():

    def __init__(self, nimi, sarjat = ["punainen"], suoritushistoria = []):
        self.nimi = nimi
        self.sarjat = sarjat
        self.suoritushistoria = suoritushistoria


class Kulku(Rataosuus):
    
    # TODO: laske kuljettu aika pituuden, vartion nopeuden, ja reitin hankaluuden avulla, tai kovakoodatuilla arvoilla
    # pituus = 1
    # vaikeus = 1
    

    def __init__(self, nimi, suoritusaika, hajonta, sarjat = ["punainen"], suoritushistoria = []):
        super().__init__(nimi, sarjat, suoritushistoria)
        self.suoritusaika = suoritusaika
        self.hajonta = hajonta
        self.sarjat = sarjat
        self.suoritushistoria = suoritushistoria

    def simuloi(self, vartiolista):
        
        # Kulkuosuudella jokainen vartio käyttää satunnaisen ajan
        for vartio in vartiolista:
            # Tallenna vartion suorittamisaika
            vartio.historia.append(Logi(saapumatta[0].nimi, self.nimi, vartio.aika, "suorittamaan"))
            self.suoritushistoria.append(Logi(saapumatta[0].nimi, self.nimi, vartio.aika, "suorittamaan"))
            
            # Tallenna vartion suorittamisaika
            kulkuaika = gamma.rvs(self.suoritusaika, self.hajonta)
            vartio.aika += kulkuaika

            # Tallenna vartion poistumisaika
            vartio.historia.append(Logi(saapumatta[0].nimi, self.nimi, vartio.aika, "poistuu"))
            self.suoritushistoria.append(Logi(saapumatta[0].nimi, self.nimi, vartio.aika, "poistuu"))

        return vartiolista

    def __str__(self):
        return f'''Kulku {self.nimi} sarjoille {self.sarjat}
        Suoritusaika: {self.suoritusaika}, hajonnalla {self.hajonta}
        Suoritushistoria: {self.suoritushistoria}'''
    
    def __repr__(self):
        return str(self)

    

class Rasti(Rataosuus):
    

    def __init__(self, nimi, suoritusaika, hajonta, suorituspaikat, sarjat = ["punainen"], suoritushistoria = []):
        super().__init__(nimi, sarjat, suoritushistoria)
        self.suoritusaika = suoritusaika
        self.hajonta = hajonta
        self.suorituspaikat = suorituspaikat

    def simuloi(self, vartiolista):
        # Laske vartioiden saapumisjärjestys
        vartiolista.sort()
        
        # Rastilla jokainen vartio käyttää satunnaisen ajan, mutta suorituspaikkoja on vain rajallisesti
        kello = vartiolista[0].aika
        vapaat_suorituspisteet = self.suorituspaikat
        
        saapumatta = vartiolista.copy()
        jono = []
        suorittamassa = []
        valmiit = []

        
        
        while(len(valmiit) < len(vartiolista) and kello < 5000):

            # Siirrä saapuneet vartiot jonoon
            while(saapumatta and kello >= saapumatta[0].aika):
                # Tallenna tiedot vartion historiaan, sekä rastin historiaan
                logimerkinta = Logi(saapumatta[0].nimi, self.nimi, kello, "jonottamaan")
                saapumatta[0].historia.append(logimerkinta)
                self.suoritushistoria.append(logimerkinta)
                
                jono.append(saapumatta.pop(0))
            
            # Täydennä suorituspaikat jonottavilla vartioilla
            while(jono and vapaat_suorituspisteet > 0):
                logimerkinta = Logi(jono[0].nimi, self.nimi, kello, "suorittamaan")
                jono[0].historia.append(logimerkinta)
                self.suoritushistoria.append(logimerkinta)

                jono[0].aika = kello + gamma.rvs(self.suoritusaika, self.hajonta)

                suorittamassa.append(jono.pop(0))
                vapaat_suorituspisteet -= 1
            
            # Siirrä valmiit vartiot pois suorituspaikoilta
            suorittamassa.sort()
            while(len(valmiit) < len(vartiolista)-1 and suorittamassa and kello >= suorittamassa[0].aika):
                logimerkinta = Logi(suorittamassa[0].nimi, self.nimi, kello, "poistuu")
                suorittamassa[0].historia.append(logimerkinta)
                self.suoritushistoria.append(logimerkinta)
                valmiit.append(suorittamassa.pop(0))
                vapaat_suorituspisteet += 1

            kello += 1

        return valmiit

    def __str__(self):
        return f'''Rasti {self.nimi} sarjoille {self.sarjat}
        Suoritusaika: {self.suoritusaika}, hajonnalla {self.hajonta}
        Suoritushistoria: {self.suoritushistoria}'''
        
    def __repr__(self):
        return str(self)