import math
from itertools import permutations, combinations
from collections import Counter

def permutaciones_objetos_diferentes(objetos):
    
    #_________________________________________
    # Permutaciones de objetos diferentes
    #_________________________________________
    print("Permutaciones de objetos diferentes:")
    
    n = len(objetos)
    #cuantos elementos hay en la lista
    
    total_permutaciones = math.factorial(n)
    
    lista_permutaciones = list(permutations(objetos))

    print(f"Total de permutaciones: {n}!: {total_permutaciones}")
    print("Lista de permutaciones:")
    for p in lista_permutaciones:
        print(f"{p}")
        
    
def permutaciones_objetos_iguales(objetos):
    
    #_________________________________________
    # Permutaciones de objetos iguales
    #_________________________________________
    print("\nPermutaciones de objetos iguales:")
    
    n = len(objetos)
    #cuantos elementos hay en la lista
    
    conteo=Counter(objetos)
    
    denominador=1
    for cantidad in conteo.values():
        denominador *= math.factorial(cantidad)
        
    total_permutaciones = math.factorial(n) // denominador
    lista_permutaciones = sorted(list(set(permutations(objetos))))
    

    
    

    print(f"Total de permutaciones: {n}!: {total_permutaciones}")
    print("Lista de permutaciones:")
    for p in lista_permutaciones:
        print(f"{p}")        
    
        
if __name__ == "__main__":
    permutaciones_objetos_diferentes(['A', 'B', 'C'])
    permutaciones_objetos_iguales(['A', 'A', 'B'])