from scipy.stats import gamma


class Rataosuus():

    def __init__(self, nimi, sarjat = ["punainen"]):
        self.nimi = nimi
        self.sarjat = sarjat


class Kulku(Rataosuus):
    
    # TODO: laske kuljettu aika pituuden, vartion nopeuden, ja reitin hankaluuden avulla, tai kovakoodatuilla arvoilla
    # pituus = 1
    # vaikeus = 1
    

    def __init__(self, nimi, suoritusaika, hajonta, sarjat = ["punainen"]):
        super().__init__(nimi, sarjat)
        self.suoritusaika = suoritusaika
        self.hajonta = hajonta
        self.sarjat = sarjat

    def simuloi(self, vartiolista):
        
        # Kulkuosuudella jokainen vartio käyttää satunnaisen ajan
        for vartio in vartiolista:
            
            # Tallenna vartion suorittamisaika
            kulkuaika = gamma.rvs(self.suoritusaika, self.hajonta)
            vartio.aika += kulkuaika

        return vartiolista

    def __str__(self):
        return f'''Kulku {self.nimi} sarjoille {self.sarjat}
        Suoritusaika: {self.suoritusaika}, hajonnalla {self.hajonta}
        '''
    
    def __repr__(self):
        return str(self)

    

class Rasti(Rataosuus):
    
    def __init__(self, nimi, suoritusaika, hajonta, suorituspaikat, sarjat = ["punainen"]):
        super().__init__(nimi, sarjat)
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
                jono.append(saapumatta.pop(0))
            
            # Täydennä suorituspaikat jonottavilla vartioilla
            while(jono and vapaat_suorituspisteet > 0):

                jono[0].aika = kello + gamma.rvs(self.suoritusaika, self.hajonta)

                suorittamassa.append(jono.pop(0))
                vapaat_suorituspisteet -= 1
            
            # Siirrä valmiit vartiot pois suorituspaikoilta
            suorittamassa.sort()
            while(len(valmiit) < len(vartiolista)-1 and suorittamassa and kello >= suorittamassa[0].aika):
                valmiit.append(suorittamassa.pop(0))
                vapaat_suorituspisteet += 1

            kello += 1

        return valmiit

    def __str__(self):
        return f'''Rasti {self.nimi} sarjoille {self.sarjat}
        Suoritusaika: {self.suoritusaika}, hajonnalla {self.hajonta}
        '''
        
    def __repr__(self):
        return str(self)