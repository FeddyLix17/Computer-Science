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
