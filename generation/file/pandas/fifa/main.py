import pandas as pd # Importazione pandas 

file = 'generation/file/pandas/fifa/files/fifa.csv' # Path del nostro file (dove si trova)
df = pd.read_csv(file) # Dicchiara il DataFrame (lettura del file csv)


def leggere_csv(df):
    print(df)   # Vediamo il DataFrame
    
#leggere_csv(df)


def conto_dati(df):
    titoli_columna = df.columns # Prendiamo i titoli delle columne
    
    conto_righe = len(df) # Conta le righe della DataFrame
    
    conto_player = df['player_id'].nunique() # Dal DataFrame conta I UNICI della columna player_id
    
    conto_match = df['match_id'].nunique() # Dal DataFrame conta I UNICI della columna match_id 
    
    # Per fare print di ogni titolo
    for titolo in titoli_columna:
        print(titolo, end=' - ')
    print("\n")
    
    print(f"Record: {conto_righe} - player_id: {conto_player} - match_id: {conto_match}")
    
#conto_dati(df)


def conto_goals(df, giocatore_id):
    # Se il player_id è uguale al id che passiamo noi e i goals sono diversi di 0, prendiamo la columna goals con le file che hanno valore != 0
    goals_giocatore = df.loc[(df['player_id'] == giocatore_id) & (df['goals'] != 0), 'goals']
    
    tot_goles = goals_giocatore.sum() # Si sumano i valori della columna presa prima
    print(f"Totale goles: {tot_goles}")

    dati_tournament = df.loc[(df['player_id']== giocatore_id) & (df['total_goals_tournament'] != 0), 'total_goals_tournament']
    tot_tournament = dati_tournament.sum()
    print(f"Total goals tournament: {tot_tournament}")
    
#conto_goals(df, 'P00070')

def giocatore_per_ruolo(df):
    giocatori = dict() # Si crea un diccionario vuoto
    
    giocatori_unici = df[['player_id', 'player_name', 'position']] # Prendiamo i dati che ci interessano
    giocatori_unici = giocatori_unici.drop_duplicates() # Togliamo i ripetuti
    
    # Definiamo player_id come index del diccionario  
    giocatori = giocatori_unici.set_index('player_id').to_dict(orient='index') # Definiamo che gli altri dati sono un diccionario dentro le chiavi player_id
    
    # diccionaro_esempio = {
    #                     'P00055': {
    #                       'player_name': 'Rodri Fati', 
    #                       'position': 'Goalkeeper'
    #                     }
    
    # Definiamo a 0 variabili che ci servirano per il conteggio
    conto_defender = 0
    conto_midfielder = 0
    conto_forward = 0
    conto_goalkeeper = 0
    
    for iden, info in giocatori.items(): # Si percorre il diccionario
        #print(f"{iden} -> {info['player_name']} ({info['position']})")
        
        if info['position'] == 'Defender':
            conto_defender += 1
        elif info['position'] == 'Midfielder':
            conto_midfielder += 1
        elif info['position'] == 'Forward':
            conto_forward += 1
        elif info['position'] == 'Goalkeeper':
            conto_goalkeeper += 1
            
    print(f"Defender = {conto_defender} | Midfielder = {conto_forward} | Goalkeeper = {conto_goalkeeper} | Totale = {conto_defender + conto_midfielder + conto_forward + conto_goalkeeper}")
    
#giocatore_per_ruolo(df)


def squadre_nazioni(df):
    conto_team = df['team'].nunique() # .nunique() CONTA i unici
    conto_nazione = df['nationality'].nunique()
    
    print(f"Team = {conto_team} | Nazione = {conto_nazione}")
    
#squadre_nazioni(df)


def fasi_torneo(df):
    tournament_stage_list = [] # Lista vuota
    
    tournament_stage = df['tournament_stage'].drop_duplicates() # Togliamo i duplicati
    tournament_stage_list = tournament_stage.to_list() # Si inseriscono i valore di tournament_stage a la lista che abbiamo creato
    
    for elem in tournament_stage_list:
        print(elem, end=' - ') # Vediamo i elementi della lista
    
#fasi_torneo(df)


def classifiche(df):
    goals_per_giocatore = dict()
    
    goals_giocatore = df.loc[(df['goals'] != 0), ['player_id', 'player_name', 'team' ,'goals']] # Se goal != 0 prendiamo tutti i dati
    
    # Groupby prende i dati che gli passiamo e gli sistema in un grupo, con la condizione scelta da noi
    # Non funziona come .drop_duplicates()! 
    # Noi stiamo aggrupando tutti i giocatori con i stessi dati in uno solo e facendo una somma di quello che ci serve (i goals)
    goals_group = goals_giocatore.groupby(['player_id', 'player_name', 'team'])['goals'].sum().reset_index() # reset_index() serve per ridare indici e non lasciare come indice i valori agrupatti prima
    
    goals_per_giocatore = goals_group.set_index('player_id').to_dict(orient='index') # Si salva tutto in un dict()
    
    id_max_goals = goals_group['goals'].idxmax() # Prende l'indice con piu goals
    max_goals = goals_group.loc[id_max_goals, ['player_name', 'goals']] # Si prende il giocatore con piu goal
    
    top_cinque = goals_group.nlargest(5, 'goals')[['player_name', 'goals']] # Imagina nlargest come for i in range(5):

    print(max_goals)
    print("---")
    print(top_cinque)
    
    
classifiche(df)