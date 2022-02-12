

class Logi():

    def __init__(self, vartionnimi, rataosuusnimi, aika, tapahtuma):
        self.vartionnimi = vartionnimi
        self.rataosuusnimi = rataosuusnimi,
        self.aika = aika
        self.tapahtuma = tapahtuma

    
    def __str__(self):
        return f"""Logimerkintä: Vartio {self.vartionnimi} rataosuudella {self.rataosuusnimi}, {tapahtuma} kellonaikaan {self.aika}"""

    
    def __repr__(self):
        return str(self)