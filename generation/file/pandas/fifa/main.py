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
    
    qatar_name = 'Qatar' 
    
    df_qatar_players = df[df['team'] == qatar_name]
    gol_metodo_a = df_qatar_players['goals'].sum()
    
    df_partite_uniche = df.drop_duplicates(subset=['match_id', 'team'])
    df_qatar_matches = df_partite_uniche[df_partite_uniche['team'] == qatar_name]
    gol_metodo_b = df_qatar_matches['goals_team'].sum()

    print(gol_metodo_a)
    print(gol_metodo_b)
    print(gol_metodo_b - gol_metodo_a)
    
#doppio_conteggio(df)


def disciplina(df):
    
    tot_yellow = df['yellow_cards'].sum()
    print(f"Tot. Yellow: {tot_yellow}")
    
    tot_red = df['red_cards'].sum()
    print(f"Tot. Red: {tot_red}")
    
    yellow = df.groupby('team')['yellow_cards'].sum().nlargest(3).reset_index()
    
    print("YELLOW cards")
    for squadra, cards in yellow.values:
        print(f"{squadra}, {cards}")
    
    
    rosso = df.groupby('team')['red_cards'].sum().nlargest(3).reset_index()
    
    print("RED cards")
    for squadra, cards in rosso.values:
        print(f"{squadra}, {cards}")

#disciplina(df)


def produrre_salvare(df):
    classifica = df.groupby(['player_name', 'position', 'team'])['goals'].sum().nlargest(20)
    
    classifica.to_csv('generation/file/pandas/fifa/files/classifica_marcatori.csv', index=True, sep=';')
    
#produrre_salvare(df)


def profilo_medio(df):

    ruoli = df.groupby('position')[['goals', 'assists', 'tackles', 'pass_accuracy', 'distance_covered_km']].mean() # mean() calcola promedio di tutti gli elementi passati
    
    profilo = ruoli.round(2).reset_index()
    
    profilo.to_csv('generation/file/pandas/fifa/files/profilo_ruoli.csv', index=True, sep=';')

#profilo_medio(df)


def giocatore_del_torneo(df):
    migliori_giocatori = df.groupby('player_name')[['goals', 'assists', 'recoveries']].sum()
    top = migliori_giocatori.reset_index()
    
    top_ord = top.sort_values(by='goals', ascending=False)
    print(top_ord.head(15))
    
#giocatore_del_torneo(df)