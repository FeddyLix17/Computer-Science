import os
import os.path


def minemass(path, dizionariodelsium, aoao = 0):
    for x in os.scandir(path):
        if not x.name.startswith("."):
            if x.is_file():
                if x.name.split(".")[1] in dizionariodelsium:
                    dizionariodelsium[x.name.split(".")[1]].append(aoao) 
                else:
                    dizionariodelsium[x.name.split(".")[1]] = [aoao]
            else:
                minemass(x, dizionariodelsium, aoao+1)

def es67(path):
    """
    ATTENZIONE: e' VIETATO usare la funzione os.walk o altre funzioni di libreria che 
    permettono di cercare tutti i file presenti in una directory. 
    (la directory la dovete esplorare voi)

    Si definisca la funzione ricorsiva (o che fa uso di vostre funzioni ricorsive) es67 che:
    - riceve come argomento un path del filesystem
    - esplora ricorsivamente la directory corrispondente e torna un dizionario.

    NOTA: tutti i file e directory che iniziano con '.' vanno ignorati.

    Il dizionario ha come chiave le estensioni dei file trovati nella directory 
    (ovvero gli ultimi 3 caratteri del nome dei file, es: 'txt', 'pdf', 'png').
    Il valore associato a ciascuna chiave K e' la distanza (differenza delle profondita')
    tra il piu' profondo file che ha quella estensione e il meno profondo.
    Assumete che i file contenuti nella directory path siano a profondita' 0.
    Esempio:
    se nella directory con path='A1' sono presenti i soli due file di tipo 'txt'
        A1/a/b/c/d/e/f/g/h/pippo.txt    a profondita' 8    (contando A1 = 0)
        A1/d/f/pappo.txt                a profondita' 2
        risultato contiene la coppia chiave: valore
        'txt' : 6
    """
    # inserite qui il vostro codice
    dizionariodelsium = {}
    minemass(path, dizionariodelsium)
    for x in dizionariodelsium:
        dizionariodelsium[x] = max(dizionariodelsium[x]) - min(dizionariodelsium[x])
    return dizionariodelsium
    dizionario = {}
    minemass(path, dizionario)
    for k, v in dizionario.items():
        dizionario[k] = max(v) - min(v)
        return dizionario
print(es67("A1"))