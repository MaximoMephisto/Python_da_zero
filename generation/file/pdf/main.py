from pypdf import PdfReader
from tqdm import tqdm

import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

parola_escluse = set(stopwords.words('english'))
tokenizador = RegexpTokenizer(r'\w+')

reader = PdfReader("generation/file/pdf/hp.pdf")
print(len(reader.pages))          


lista_parola = {}

for pagina in tqdm(reader.pages):
    s = pagina.extract_text()
    
    parole = tokenizador.tokenize(s)

    for parola in parole:
        if parola.istitle() and len(parola) > 2:
            if parola.lower() not in parola_escluse:
                if parola not in lista_parola:
                    lista_parola[parola] = 1
                else:
                    lista_parola[parola] += 1

ordinato = dict(sorted(lista_parola.items(), key=lambda x: x[1], reverse=True)[:30])

print(ordinato)