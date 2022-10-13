from re import I
from typing import Any, Callable, List
from unittest import result


# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')


################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return f"Ciao {name} Buona giornata!"


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    return " ".join(string.split())


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    result = []
    start = 0
    for x in range(len(string)):
        if string[x-3:x] == characters:
            result.append(string[start: x-3])
            start = x + 1
    if not result:
        result.append(string)
    return result


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    result = ""
    x = 0
    while x < len(string):
        if string[x: x + len(find)] == find:
            result += replace
            x += len(replace) - 1
        else:
            result += string[x]
            x += 1
    return result


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    result = ""
    if decrypt == True:
        for x in range(len(string)):
            if offset > 25:
                result += chr((ord(string[x])+offset) % 25)
            else:
                result += chr(ord(string[x])+offset)
        return result
    else:
        for x in range(len(string)):
            if offset > -25:
                result += chr((ord(string[x])-offset) % 25)
        return result



# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.


def check_pwd(pwd: str) -> bool:
    if pwd >= 0 and pwd <= 9:
        return pwd


# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 17, False)
print_test(caesar_cypher, 'tzrf gzggf', 17, True)
print_test(check_pwd, "a")
print_test(check_pwd, "000000000000000000")
print_test(check_pwd, "almeno6")
print_test(check_pwd, "Aa@09asng2/")
print_test(check_pwd, "Aa@09asng2")

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    result = 0
    for x in elements:
        result+= x**2
    return result


# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    return max(elements)


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    return set(elements)


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    return elements[::-1]


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e ritorna una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    result = []
    x = 0
    while x < len(elements):
        if isinstance(elements[x], list):
            [result.append(elements[x][y]) for y in range(len(elements[x]))]
            x+=len(elements[x])
        else:
            result.append(elements[x])
            x += 1
    return result


# Test funzioni
print_test(sum_squares, [1, 2, 3])
print_test(max_element, [1, 2, 3, -1, -2])
print_test(remove_duplicates, [1, 2, 3, 2, 3])
print_test(reverse_list, [1, 2, 3])
print_test(flatten_list, [1, [2, 3]])