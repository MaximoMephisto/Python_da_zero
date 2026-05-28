# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las 
# letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def anagrama(p_1, p_2):
    
    if p_1 == p_2:
        return False
    
    return sorted(p_1) == sorted(p_2)

print(anagrama("assai", "iassa"))


