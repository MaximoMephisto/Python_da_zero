import csv

file = 'generation/file/pandas/olimpiadi/olimpiadi.csv'

with open(file, 'r', encoding='utf-8') as f:
    lettore_csv = csv.reader(f)

    for elem in lettore_csv:
        print(elem)
        break


### Es. 0.2 — Una riga ≠ un atleta
import pandas as pd
#DataFrame / Module
df = pd.read_csv(file, encoding='utf-8')

atleti_non_ripetuti = df['ID'].nunique()

print(atleti_non_ripetuti)

###########################################
### Es. 0.3 — Mappare i dati mancanti
eta_vuota = df['Age'].isnull().sum()
height_vuota = df['Height'].isnull().sum()
weight_vuota = df['Weight'].isnull().sum()

senza_medal = df['Medal'].isnull().sum()

print(f"{eta_vuota} campo vuoti di età.")
print(f"{height_vuota} campo vuoti di height.")
print(f"{weight_vuota} campo vuoti di weight.")

print(f"{senza_medal} atleti senza medaglie.")

### Es. 1.1 — Distribuzione per sesso
maschi = df['Sex'].value_counts()

print(maschi)


### Es. 1.2 — Arco temporale e stagioni
anno_min = df['Year'].min()
anno_max = df['Year'].max()

state = (df['Season'] == "Summer").sum()
inverno = (df['Season'] == "Winter").sum()

print(f"{int(anno_min)} - {int(anno_max)}; Summer {state}, Winter {inverno}")


### Es. 1.3 — Quanti sport, eventi, nazione
sport = df['Sport'].nunique()
evento = df['Event'].nunique()
noc = df['NOC'].nunique()

print(f"Sport {sport}, eventi {evento}, NOC {noc}")


### Parte 2 — Conversioni e dati mancanti (qui si ragiona)
### Es. 2.1 — Età media, gestendo i vuoti
df = pd.read_csv(file, encoding='utf-8', na_values=['', ' '])

media = df['Age'].astype('Int64').mean()

print(f"Età media = {round(media, 2)}")

### Es. 2.2 — Quanto ci possiamo fidare di Height/Weight?
height_conto = df['Height'].count()
height_vuoto = df['Height'].isnull().sum()

tot_height = height_conto + height_vuoto

print(f"Height mancante = {height_vuoto / tot_height * 100}%")

weight_conto = df['Weight'].count()
weight_vuoto = df['Weight'].isnull().sum()

tot_weight = weight_conto + weight_vuoto

print(f"Weight mancante = {weight_vuoto / tot_weight * 100}%")


### Es. 2.3 — Il medagliato più giovane e più anziano
### .iloc() sirve para seleccionar filas y columnas basándose exclusivamente en su posición numérica (índice entero), empezando siempre desde el 0
atleta = df[['Name', 'Age', 'Medal']]
atleti_vincenti = df.loc[df['Medal'].notnull(), ['Name', 'Age']]

min_atleta = atleti_vincenti.iloc[:,1].min()

nome_atleta = atleti_vincenti.loc[(atleti_vincenti['Age'] == min_atleta), 'Name']

uguales_min = atleti_vincenti.loc[(atleti_vincenti['Age'] == min_atleta)]
uguales_ordinati = uguales_min.sort_values(by='Name')

print(f"Nome: {uguales_ordinati.iloc[0, 0]} -> Età: {int(uguales_ordinati.iloc[0, 1])}")

max_atleta = atleti_vincenti.iloc[:,1].max()
nome_atleta_max = atleti_vincenti.loc[(atleti_vincenti['Age'] == max_atleta) & (atleti_vincenti['Name'].notnull()) , ['Name', 'Age']]

print(f"Nome: {nome_atleta_max.iloc[0, 0]} -> Età: {int(nome_atleta_max.iloc[0, 1])}")


### Parte 3 — Aggregazioni con dizionari / Counter
### Es. 3.1 — Il medagliere per nazione (NOC)
conteggio_medaglie = df.loc[df['Medal'].notnull()].groupby('NOC').size()

### El razonamiento pensado: .size() cuenta absolutamente todas las filas de cada grupo (país). Al aplicarlo después de filtrar los nulos con .notnull(), obtienes el total exacto de medallas por delegación.

medaglie_ordinate = conteggio_medaglie.sort_values(ascending=False)

for paese, medaglia in medaglie_ordinate.items():
    print(f"{paese} -> {medaglia}")


### Es. 3.2 — Medaglie per sesso
medaglie_sesso = df.loc[df['Medal'].notnull()].groupby('Sex').size()

for sesso, qta in medaglie_sesso.items():
    print(f"{sesso} -> {qta}")


### Es. 3.3 — L'atleta più medagliato
cont_atletas = df.loc[df['Medal'].notnull(), ['ID', 'Name']].groupby(['ID', 'Name']).size()

atletas_ord = cont_atletas.sort_values(ascending=False)

print(f"Nome: {atletas_ord.index[0]} -> {atletas_ord.iloc[0]}")


### Es. 3.4 — Distribuzione oro/argento/bronzo
oro = (df['Medal'] == "Gold").sum()
print(f"Oro -> {oro}")

bronze = (df['Medal'] == "Bronze").sum()
print(f"Bronze -> {bronze}")

silver = (df['Medal'] == "Silver").sum()
print(f"Silver -> {silver}")


# Parte 4 — Cosa stiamo *davvero* contando? (ragionamento avanzato)
### Es. 4.2 — Perché `NOC` e non `Team`

righe_medaglia = df['Medal'].count() # Conta tutte le righe del dataset che contengono una medaglia (escludendo le righe dove non c'è medaglia, se presenti).

keys = ['Year', 'Season', 'Event', 'Medal', 'NOC']
# Il metodo dropna() serve per eliminare (cancellare) dal DataFrame tutte le righe che contengono valori mancanti o vuoti
df_pulito = df.dropna(subset=keys) # Pulisce il dataset rimuovendo righe che hanno valori mancanti nelle colonne chiave (evitando errori nel calcolo successivo).

# Il metodo drop_duplicates() serve per eliminare i doppioni (le righe ripetute)
conteggio = df_pulito.drop_duplicates(subset=keys).shape[0]

differenza = int(righe_medaglia) - int(conteggio)

print(f"Righe medaglia -> {righe_medaglia}")
print(f"Conteggio: {conteggio}")
print(f"Differenza: {differenza}")

### Es. 4.3 — Il medagliere "corretto" per evento
cont_team = df['Team'].nunique()
cont_noc = df['NOC'].nunique()

print(f"Team: {cont_team}")
print(f"NOC: {cont_noc}")

## Parte 5 — Scrittura dei risultati
medagliati = df.loc[df['Medal'].notnull(), ['Name']]

medagliati.to_csv('generation/file/pandas/olimpiadi/medagliati.csv', index=False)

### Es. 5.2 — Salvare il medagliere dettagliato (`csv.DictWriter`)
medagliere = df[['Medal', 'NOC']].dropna()

oro = medagliere[medagliere['Medal'] == 'Gold']
dati_oro = oro.groupby('NOC').size().sort_values(ascending=False)

silver = medagliere[medagliere['Medal'] == 'Silver']
dati_silver = silver.groupby('NOC').size().sort_values(ascending=False)

bronze = medagliere[medagliere['Medal'] == 'Bronze']
dati_bronze = bronze.groupby('NOC').size().sort_values(ascending=False)

medagliere_senza_duplicati = medagliere['NOC'].unique()

dict_medagliere = dict()
for elem in medagliere_senza_duplicati:
  dict_medagliere[elem] = []


for elem in dati_oro.index:
  dict_medagliere[elem] = [int(dati_oro[elem])]
  
  
for elem in dati_silver.index:
  dict_medagliere[elem].append(int(dati_silver[elem]))
  
  
for elem in dati_bronze.index:
  dict_medagliere[elem].append(int(dati_bronze[elem]))
  

for noc, medaglie in dict_medagliere.items():
  tot = 0
  for elem in medaglie:
    tot += int(elem)
  dict_medagliere[noc].append(tot)


for noc, medaglie in dict_medagliere.items():
    print(f"{noc} -> {medaglie}")


df_medagliere = pd.DataFrame.from_dict(dict_medagliere, orient='index')

df_medagliere.columns = ['Gold', 'Silver', 'Bronze', 'Totale']

df_medagliere.index.name = 'NOC'

df_medagliere = df_medagliere.sort_values(by=['Totale'], ascending=False)

df_medagliere.to_csv('generation/file/pandas/olimpiadi/noc_medagliati.csv', index=True)

"""### Es. 5.3 — Esportare una nazione (a scelta)
**Obiettivo:** scrivere `italia.csv` con le sole righe dove `NOC == "ITA"` (provate poi col vostro paese).
**Ragionamento:** stesso schema del 5.1 ma filtrando su una colonna diversa.

> **Atteso:** 1 header + `4176` righe per `ITA`.
"""
df_paese_uno = df.loc[df['NOC'] == 'ITA', ['NOC']]
df_paese_uno = df_paese_uno.drop_duplicates()
paese = f"NOC == {df_paese_uno.values[0, 0]}"

import csv

with open('generation/file/pandas/olimpiadi/italia.csv', 'w', encoding='utf-8') as f:
  scrittura_csv = csv.writer(f)
  
  scrittura_csv.writerow([paese])
  
  
### Es. 5.4 — Pipeline: il medagliere per evento, su file
df_medaglie = df.dropna(subset=['Medal'])

colonne_evento = ['Year', 'Sport', 'Event', 'Medal', 'NOC']
df_eventi_unici = df_medaglie[colonne_evento].drop_duplicates()

medagliere_serie = df_eventi_unici.groupby('NOC').size()

df_medagliere_eventi = medagliere_serie.to_frame(name='Medaglie')
df_medagliere_eventi.index.name = 'NOC'
df_medagliere_ordinato = df_medagliere_eventi.sort_values(by='Medaglie', ascending=False)
df_medagliere_ordinato.to_csv('generation/file/pandas/olimpiadi/medagliere_eventi.csv', index=True, sep=';')