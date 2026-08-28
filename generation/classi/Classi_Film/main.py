import pandas as pd

df = pd.read_csv('generation/classi/Classi_film/film.csv')

print(df.head())

class Film():
    
    def __init__(self, titolo, anno, genere, durata, voto):
        self.titolo = titolo
        self.anno = anno
        self.genere = genere
        self.durata = int(durata)
        self.voto = float(voto)
        
    def stampa(self):
       print(f"{self.titolo} ({self.durata}) - {self.genere} - voto {self.voto}") 
        
    def e_lungo(self):
        if self.durata > 150:
            return True
        else:
            return False
    
class Catalogo():
    
    def __init__(self):
        self.tutti_film = []
        
    def aggiungi_film(self, film):
        self.tutti_film.append(film)
        
    def stampa_tutti(self):
        print("===== TUTTI I FILM =====")
        for film in self.tutti_film:
            film.stampa()
            
    def stampa_per_genere(self, genere):
        print("====== PER GENERE =====")
        for film in self.tutti_film:
            if genere == film.genere:
                film.stampa()
                
    def migliore(self):
        print("===== MIGLIORE =====")
        voto_alto = 0
        film_vincitore = None
        
        for film in self.tutti_film:
            if film.voto > voto_alto:
                voto_alto = film.voto
                film_vincitore = film

        film_vincitore.stampa()
        
    def durata_media(self):
        print("===== MEDIA =====")
        lunghezza = len(self.tutti_film)
        somma = sum(film.durata for film in self.tutti_film)
        media = somma / lunghezza
        
        print(media)
         
lista_film = []

for index, row in df.iterrows():
    # Per ogni riga prendiamo i dati e si passano alla classe.
    nuovo_film = Film(
        titolo=row['titolo'],   
        anno=row['anno'],
        genere=row['genere'],
        durata=row['durata'],
        voto=row['voto']
    )
    # Aggiunta della classe creata nella lista
    lista_film.append(nuovo_film) 

# catalogo é l'oggetto, mentre Catalogo() é l'idea/proggetto
catalogo = Catalogo()

for film in lista_film:
    catalogo.aggiungi_film(film)

catalogo.stampa_tutti()
catalogo.stampa_per_genere("Drammatico")
catalogo.migliore()
catalogo.durata_media()