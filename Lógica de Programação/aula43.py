"""  
Iterável -> str, range, list, tuple, set, dict, etc (__iter__())
Iterador -> objeto que tem o método __next__()
next() -> chama o método __next__()
iter() -> chama o método __iter__()
"""

# for letra in texto

texto = 'Python' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break