my_set = tuple()
print(my_set)

my_set = list(my_set)
print(my_set)

my_set.append('Dante')
my_set.append('Sorondo')
my_set.append('2')
print(my_set)

my_set = tuple(my_set)
print(my_set)

nuovo_dict = {}
id = "7"

nuovo_dict[id] = {my_set}

for nome, cognome, eta in nuovo_dict[id]:
    print(f"{nome} {cognome} {eta}")
    