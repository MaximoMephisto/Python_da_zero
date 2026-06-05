import copy

base = {'tagli': ['filetto', 'costata'],
        'salse': ['senape']}

copia = copy.deepcopy(dict(base))
copia['tagli'].append('lombata')

print(base)
print(copia)