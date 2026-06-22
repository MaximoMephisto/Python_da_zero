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
    
#classifiche(df)


def assists(df):
    assists_per_giocatore = dict()
    
    assists_giocatore = df.loc[(df['assists'] != 0), ['player_id', 'player_name', 'team' ,'goals', 'nationality', 'assists']]
    
    assists_group = assists_giocatore.groupby(['player_id', 'player_name', 'team', 'nationality'])['assists'].sum().reset_index()
    assists_per_giocatore = assists_group.set_index('player_id').to_dict(orient='index')
    id_max_assists = assists_group['assists'].idxmax()
    max_assists = assists_group.loc[id_max_assists, ['player_name', 'nationality', 'assists']]
    top_cinque = assists_group.nlargest(5, 'assists')[['player_name', 'nationality', 'assists']]
    
    print(max_assists)
    print("---")
    print(top_cinque)
    
#assists(df)


def goal_ruolo(df):
    
    tot_goalkeeper = df.loc[(df['goals'] != 0) & (df['position'] == 'Goalkeeper')]
    tot_midfielder = df.loc[(df['goals'] != 0) & (df['position'] == 'Midfielder')]
    tot_defender = df.loc[(df['goals'] != 0) & (df['position'] == 'Defender')]
    tot_forward = df.loc[(df['goals'] != 0) & (df['position'] == 'Forward')]
    
    dati_goalkeeper = tot_goalkeeper.groupby('position')['goals'].sum().reset_index()
    dati_midfielder = tot_midfielder.groupby('position')['goals'].sum().reset_index()
    dati_defender = tot_defender.groupby('position')['goals'].sum().reset_index()
    dati_forward = tot_forward.groupby('position')['goals'].sum().reset_index()
    
    if dati_goalkeeper.empty:
        print("Goalkeeper -> 0")
        
    for elem in dati_defender.values:
        print(f"{elem[0]} -> {elem[1]}")
        
    for elem in dati_midfielder.values:
        print(f"{elem[0]} -> {elem[1]}")
        
    for elem in dati_forward.values:
        print(f"{elem[0]} -> {elem[1]}")

#goal_ruolo(df)


def squadra_profilica(df):
                # Si fa un grupo per TEAM e prendiamo i goal
    squadra = df.groupby('team')['goals'].sum().nlargest(5) # Si sommano i goals e si prendono i dati in una larghezza di 5 indici

    print(squadra)

#squadra_profilica(df)


def gol_reali(df):
    
    goals = df.groupby('player_name')['goals'].sum()
    expected_goals = df.groupby('player_name')['expected_goals_xg'].sum()
    
    real_goals = goals - expected_goals
    
    real_goals_top = real_goals.nlargest(5)
    
    print(real_goals_top)

#gol_reali(df)


def passagi_precisi(df):
    # con groupby possiamo anche ottenere la somma totale di due valori SENZA unirli. Es: somma_totale di total_passe e somma_totale di successful_passes
    passagi = df.groupby(['player_name', 'nationality'])[['total_passes', 'successful_passes']].sum().reset_index()
    
    # Prendiamo i valori salvati nella variabile passagi SOLTANTO se total_passes >= 2000
    sum_passagi = passagi[passagi['total_passes'] >= 2000]
    
    # I valori di sum_passagi sono i stessi che abbiamo scelto noi quando abbiamo fatto il groupby nella variabile passagi
    for elem in sum_passagi.values:
        print(f"{elem[0]} ({elem[1]}) = {round(100 * elem[3] / elem[2], 2)}%")
    
#passagi_precisi(df)


def portieri(df):
    clean_sheet = df.loc[(df['position'] == 'Goalkeeper'), ['clean_sheet', 'position']]
    tot_clean_sheet = clean_sheet.groupby('position')['clean_sheet'].sum().reset_index()
    
    penalty_saves = df.loc[(df['position'] == 'Goalkeeper'), ['penalty_saves', 'position']]
    
    tot_rigori_pari = penalty_saves.groupby('position')['penalty_saves'].sum().reset_index()
    
    
    for elem in tot_clean_sheet.values:
        print(f"{elem[0]} -> {elem[1]}")
        
    for elem in tot_rigori_pari.values:
        print(f"{elem[0]} -> {elem[1]}")
        
#portieri(df)


def piu_veloce(df):
    # Prendiamo il ID dell' top_speed_kmh maggiore
    id_max = df['top_speed_kmh'].idxmax()
    
    veloce = df.loc[id_max, ['player_name', 'nationality', 'top_speed_kmh']]
    # Prendiamo i elementi salvati in veloce
    nome, nazione, velocita = veloce.values
    
    print(f"{nome} ({nazione}), {velocita}km/h.")
        
#piu_veloce(df)


def doppio_conteggio(df):
#     Obiettivo: calcolare i gol totali del Qatar in due modi e confrontarli: (a) sommando i goals dei suoi giocatori; 
# (b) usando il punteggio di partita goals_team, ma una sola volta per partita (deduplicando su (match_id, team)). 
# Ragionamento (chiave): goals_team è il risultato della squadra in quella partita ed è ripetuto su ogni riga-giocatore di quella partita. 
# Sommarlo su tutte le righe lo moltiplica per il numero di giocatori! Per usarlo correttamente bisogna prima ridurre a una riga per partita.

# Atteso: i due metodi danno numeri diversi (per il Qatar ≈ 95 con il metodo (a) e ≈ 103 con il metodo (b)): differiscono per autogol, 
# gol di giocatori non a referto, ecc. Capire perché è più importante del numero esatto.
    pass
doppio_conteggio(df)


def disciplina(df):
    # Obiettivo: cartellini yellow_cards e red_cards totali del torneo, e le 3 squadre con più gialli. Ragionamento: semplici somme per chiave; 
    # utile come ulteriore esercizio di aggregazione.

    # Atteso: gialli totali 5346, rossi totali 306; più gialli: Saudi Arabia 162, Qatar 160, Jamaica 154.
    pass
disciplina(df)


def produrre_salvare(df):
    # Es. 5.1 — Esportare la classifica marcatori (csv.writer)
    # Obiettivo: salvare classifica_marcatori.csv con i top 20 cannonieri, colonne player_name,team,position,goals, ordinati per gol decrescenti. 
    # Ragionamento: riusate l'aggregazione del 2.1, ordinate con sorted(..., key=..., reverse=True), prendete i primi 20 e scrivete con header.

    # Atteso: 1 header + 20 righe; prima riga Memphis Zerrouki,Netherlands,Forward,24.
    pass
produrre_salvare(df)


def profilo_medio(df):
    # Obiettivo: creare profilo_ruoli.csv con una riga per position e le medie (su tutte le righe del ruolo) di: goals, assists, tackles, pass_accuracy, 
    # distance_covered_km. Arrotondate a 2 decimali. Ragionamento: aggregazione "somma e conteggio per chiave" poi divisione. È il classico identikit statistico: 
    # cosa distingue un difensore da un attaccante nei numeri?

    # Suggerimento: un dizionario {ruolo: {"somma_goals":.., "n":.., ...}} e alla fine dividete.
    pass
profilo_medio(df)


def giocatore_del_torneo(df):
#     Obiettivo: progettate voi un punteggio composito per nominare il miglior giocatore, poi salvate top_giocatori.csv con i primi 15 e il loro punteggio. 
# Ragionamento (open-ended): dovete prendere decisioni e motivarle. Esempi di scelte:

    # quali metriche combinare (gol, assist, key_passes, contrasti, recuperi...)?
    # come renderle confrontabili (normalizzare? pesare gol più degli assist?);
    # come gestire i ruoli (un portiere non va valutato come un attaccante)? Non esiste una risposta "giusta": l'esercizio è costruire e giustificare un criterio, 
    # poi ordinare e salvare. Commentate nel notebook le scelte fatte.
    pass
giocatore_del_torneo(df)