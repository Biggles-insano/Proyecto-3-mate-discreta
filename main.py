import math
from itertools import permutations, combinations
from collections import Counter

# ---------------------------------------------------------------------------
#                           PERMUTACIONES
# ---------------------------------------------------------------------------

def permutaciones_objetos_diferentes(objetos):
    """
    Calcula las permutaciones de objetos diferentes.
    """
    print("## 1. Permutaciones de Objetos Diferentes ##")
    n = len(objetos)
    total_permutaciones = math.factorial(n)
    lista_permutaciones = list(permutations(objetos))

    print(f"Objetos de entrada: {objetos}")
    print(f"Total de permutaciones (n!): {total_permutaciones}")
    print("Lista de permutaciones:")
    for p in lista_permutaciones:
        print(f"  {p}")
    print("-" * 40)

def permutaciones_objetos_iguales(objetos):
    """
    Calcula las permutaciones de objetos con repeticiones.
    """
    print("## 2. Permutaciones de Objetos Iguales ##")
    n = len(objetos)
    conteo = Counter(objetos)
    
    denominador = 1
    for cantidad in conteo.values():
        denominador *= math.factorial(cantidad)
        
    total_permutaciones_unicas = math.factorial(n) // denominador
    lista_permutaciones_unicas = sorted(list(set(permutations(objetos))))
    
    print(f"Objetos de entrada: {objetos}")
    print(f"Total de permutaciones únicas: {total_permutaciones_unicas}")
    print("Lista de permutaciones únicas:")
    for p in lista_permutaciones_unicas:
        print(f"  {p}")
    print("-" * 40)

# ---------------------------------------------------------------------------
#                           COMBINACIONES
# ---------------------------------------------------------------------------

def combinaciones_objetos_diferentes(objetos, r):
    """
    Calcula las combinaciones de 'r' objetos tomados de un grupo de objetos diferentes.
    """
    print(f"## 3. Combinaciones de Objetos Diferentes ##")
    n = len(objetos)
    
    # Manejo de error por si se piden más objetos de los que hay
    if r > n:
        print(f"Error: No se puede seleccionar {r} objetos de un grupo de {n}.") 
        print("-" * 40)
        return

    lista_combinaciones = list(combinations(objetos, r))
    total_combinaciones = len(lista_combinaciones)

    print(f"Objetos de entrada: {objetos}, seleccionando {r}.")
    print(f"Total de combinaciones: {total_combinaciones}")
    print("Lista de combinaciones:")
    for c in lista_combinaciones:
        print(f"  {c}")
    print("-" * 40)

def combinaciones_objetos_iguales(objetos, r):
    """
    Calcula las combinaciones únicas de 'r' objetos cuando hay elementos repetidos.
    """
    print(f"## 4. Combinaciones de Objetos Iguales ##")
    n = len(objetos) 

    if r > n: 
        print(f"Error: No se puede seleccionar {r} objetos de un grupo de {n}.")
        print("-" * 40) 
        return
        
    # El truco es usar set() para eliminar los duplicados que genera combinations()
    lista_combinaciones_unicas = sorted(list(set(combinations(objetos, r))))
    total_combinaciones_unicas = len(lista_combinaciones_unicas)

    print(f"Objetos de entrada: {objetos}, seleccionando {r}.")
    print(f"Total de combinaciones únicas: {total_combinaciones_unicas}")
    print("Lista de combinaciones únicas:")
    for c in lista_combinaciones_unicas:
        print(f"  {c}")
    print("-" * 40)

# ---------------------------------------------------------------------------
#                           ZONA DE EJECUCIÓN
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print(" Calculadora de Combinatoria para Mate Discreta \n")
    
    # Ejemplo 1: Permutaciones de objetos diferentes
    permutaciones_objetos_diferentes(['a', 'b', 'c', 'd'])
    
    # Ejemplo 2: Permutaciones de objetos iguales
    permutaciones_objetos_iguales(['a', 'a', 'b', 'c'])
    
    # Ejemplo 3: Combinaciones de objetos diferentes
    combinaciones_objetos_diferentes(['a', 'b', 'c', 'd'], 2) 
    
    # Ejemplo 4: Combinaciones de objetos iguales
    combinaciones_objetos_iguales(['a', 'a', 'b', 'c'], 2) 