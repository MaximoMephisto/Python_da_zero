import csv

file = 'generation/file/csv/calcio.csv'

# with open(file, 'r', encoding='utf-8') as f:
#     next(f) # Salto riga
#     lettore_csv = csv.reader(f, delimiter=';')
#     for linea in lettore_csv:
#         print(linea)


# with open(file, 'r', encoding='utf-8') as f:
#     next(f) # Salto riga
#     lettore_csv = csv.reader(f, delimiter=';')

#     cont = 0
#     for linea in lettore_csv:
#         if linea[3] == 'Inghilterra':
#             cont += 1
    
#     print(cont)    
    

# with open(file, 'r', encoding='utf-8') as f:
#     lettore_csv = csv.DictReader(f, delimiter=';')
#     for linea in lettore_csv:
#         print(linea)



# with open(file, 'r', encoding='utf-8') as f:
#     lettore_csv = csv.DictReader(f, delimiter=';')
#     cont = 0
#     for linea in lettore_csv:
#         if linea['nazionalita'] == 'Inghilterra':
#             cont += 1
            
#     print(cont)
with open(file, 'r', encoding='utf-8') as f:
    lettore_csv = csv.DictReader(f, delimiter=';')
    for dicc in lettore_csv:
        rapporto = round(float(dicc['gol']) / float(dicc['presenze']), 2) 
        dicc['score'] = [rapporto]
        print(dicc)


with open(file, 'r', encoding='utf-8') as f:
    lettore_csv = csv.DictReader(f, delimiter=';')
    
    lista_punti = []
    
    for dicc in lettore_csv:
        
        nome = dicc['nome']
        rapporto = round(float(dicc['gol']) / float(dicc['presenze']), 2) 
        
        lista_punti.append([nome, rapporto])
          
    print(sorted(lista_punti, key=lambda x:x[1], reverse=True))
    

with open(file, 'r', encoding='utf-8') as f:
    lettore_csv = csv.DictReader(f, delimiter=';')
    
    lista_punti = []
    
    for dicc in lettore_csv:
        
        nome = dicc['nome']
        rapporto = round(float(dicc['gol']) / float(dicc['presenze']), 2) 
        
        lista_punti.append((nome, rapporto))
        
    print(lista_punti)

 

with open(file, 'r', encoding='utf-8') as f:
    lettore_csv = csv.DictReader(f, delimiter=';')
    
    lista_punti = []
    
    for dicc in lettore_csv:
        
        punti = dict()
        
        nome = dicc['nome']
        rapporto = round(float(dicc['gol']) / float(dicc['presenze']), 2) 
        
        punti[nome] = rapporto
        lista_punti.append(punti)
    
    print(lista_punti)
    
print("==============")
print("==============")
print("==============")

with open(file, 'r', encoding='utf-8') as f:
    next(f)
    lettore_csv = csv.reader(f, delimiter=';')
    
    lista = []
    
    for riga in lettore_csv:
        lista.append((riga[0], riga[1], int(riga[4]), int(riga[5]), int(riga[6]), int(riga[7])))

    lista_sort = sorted(lista, key=lambda x:(x[2], x[5]), reverse=True)
    
    for elem in lista_sort:
        print(elem)