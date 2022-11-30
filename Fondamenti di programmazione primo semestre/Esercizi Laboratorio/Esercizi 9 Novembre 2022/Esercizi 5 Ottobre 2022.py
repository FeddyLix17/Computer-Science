import math

#calcoli
#1
print(f"secondi presenti in 42minuti e 42 secondi: {(42*60)+42} secondi")

#2
print(f"numero di miglia che ci sono in 10 chilometri: {10*0.621371} miglia")

#3
print("Corridore che corre una gara di 10 chilometri in 42 minuti e 42 secondi")
print(f"tempo per miglio in minuti e secondi: {int((((42*60)+42) / (10*0.621371) / 60))} minuti e {int((((42*60)+42) /  (10*0.621371)%60))} secondi")

#4
print(f"volume di una sfera di raggio 5: {(4/3) * math.pi * (5**3)}")

#5
print(f"costo totale di 60 copie: {((((24.95 / 100) * 60) + 0.75) * 59) + (((24.95 / 100) * 60) + 3)}")

#6
# calcolare ora in cui torniamo a casa in base al ritmo (?)

#stringhe
#1
stringa5caratteri = input("inserisci la tua stringa da 5 caratteri: ")
sommanumeristringa = 0
for numero in stringa5caratteri: sommanumeristringa+=int(numero)
print(f"la somma dei numeri presenti nella stringa {stringa5caratteri} è {sommanumeristringa}")

#2
stringa5caratteri = input("inserisci la tua stringa da 5 caratteri rappresentante un numero binario: ")
print(f"la rappresentazione finale di {stringa5caratteri} in decimale è {int(int(stringa5caratteri, 2))}")

#3
stringa5caratteri = input("inserisci la tua stringa da 5 caratteri rappresentante un numero decimale: ")
print(f"la rappresentazione finale di {stringa5caratteri} in decimale (con la virgola) è {float(stringa5caratteri)}")


#funzioni
#1
def cubo_numero_virgola_mobile() -> int:
    numeroo = float(input("inserisci un numero in virgola mobile: "))
    return numeroo**3
#2
def first_equation() -> int:
    a, b, c = input("inserisci 3 numeri separati da uno spazio: ").split()
    x1 = -b + math.sqrt( b**2 - 4*a*c) / 2*a
    x2 = -b - math.sqrt( b**2 - 4*a*c) / 2*a
    return max(x1, x2) # return x1,x2 

#3
def second_equation() -> int:
    a, b, c = input("inserisci 3 numeri separati da uno spazio: ").split()
    x1 = -b + math.sqrt(b**2 - 4*a*c) / 2*a
    x2 = -b - math.sqrt(b**2 - 4*a*c) / 2*a
    return x1, x2

#4
def sum_even_minus_diff_odd() ->int:
    nums = []
    result = 0
    for x in range(5):
        nums+=input(f"inserisci il numero {x + 1}: ")
    for x in nums:
        if x % 2 == 0:
            result+=x
        else:
            result-=x

#5
def sum_value_if_valid() -> int:
    a, b, c = input("inserisci 3 numeri separati da uno spazio: ").split()
    if (a >= 0 and a <= 30) and (b >= 0 and b <= 30) and (c >= 0 and c <= 30):
        return a+b+c
    else:
        return -1


#6
def check_date() -> bool:
    d, m, y = input("inserisci giorno mese e anno separati da uno spazio: ").split()
    if (d >= 0 and d <= 31) and (m >= 1 and m <= 12) and (y >= 0 and y <= 2022):
        return True
    else:
        return False


#7
def fn_str_strip(string: str) -> str:
    return " ".join(string.split())

#8
def saluto(name: str) -> str:
    return f"Ciao {name} Buona giornata!"