def leggere_txt(file):
    dati = []
    
    with open(file, 'r', encoding='utf-8') as f:
        for riga in f:
            if ':' not in riga:
                continue
            else:
                dati.append(riga)
        
    persone = []
    
    for elem in dati:
        persona = []
        
        elem = elem.split(':')
        persone.append(elem[1].strip())
    
    persone_sistemate = []
    
    while len(persone) >= 3:
        persona = [persone[0], persone[1], persone[2]]
        persone_sistemate.append(persona)
        del persone[:3]
        
    return persone_sistemate
        
        
def trova_artista_per_lettera(lista_artisti, lettera):
    artisti_con_lettera = []
    
    for artista in lista_artisti:
        nome_artista = artista[0]
        cognome = artista[1]
        
        if lettera == nome_artista[0].lower():
            nome = f"{nome_artista} {cognome}"
            artisti_con_lettera.append(nome)
    
    return artisti_con_lettera


def trova_artista_per_anno(lista_artisti, anno):
    artista_anno = []
    verifica = False
    
    for artista in lista_artisti:
        cognome = artista[1]
        data = artista[2]
        data = data.split('-')
        anno_artista = int(data[0])
        
        if anno_artista > anno:
            dati_artista_anno = f"{cognome} -> {anno_artista}"
            artista_anno.append(dati_artista_anno)
            verifica = True
        
    if not verifica:
        vrf = "Anno di artista fuori range."
        return vrf
    else:      
        return artista_anno