

def es30(fname1,fname2,fname3):
    ''' 
    Si implementi la funzione es30(fname1,fname2,fname3) prende in input l'indirizzo di tre file di testo.
    Il primo file di testo contiene un messaggio codificato dove ogni carattere e' stato 
    sostituito da un intero di tre cifre.
    Tutti i caratteri non numerici devono essere trasferiti come sono.
    Nel secondo file  e' possibile ritrovare le corrispondenze numeri-caratteri tra i numeri 
    del testo e il rispettivo carattere. 
    Piu' precisamente questo secondo file e' organizzato in righe,  in ciascuna riga sono 
    presenti un carattere  e un intero  di tre cifre  che gli corrisponde nel file di testo separati da almeno uno spazio.
    Numeri diversi possono far riferimento ad uno stesso carattere e non tutti i numeri che appaiono in fname1
    sono necessariamente presenti nel file di decodifica.
    La funzione es30 deve decodificare il messaggio presente nel primo file grazie 
    alle informazioni contenute nel secondo.
    I numeri non presenti nel secondo file vanno decodificati con il simbolo '?'.
    Il messaggio decodificato va poi salvato nel terzo file.
    La funzione infine restituisce il numero di caratteri decodificati con il valore '?' presenti nel file decodificato.
    Ad esempio se 
    - il file fname1 contiene il testo '991118991991345      103    091027003091103?'
    - il file fname2 contiene il testo 'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 '
    il testo decodificato da registrare in file3 sara': 'tutt? a n?nna?' e la funzione restituisce il numero 2.
    Potete assumere che i caratteri numerici appaiano sempre raggruppati in triplette.
    '''
    # inserisci qui il tuo codice
    result = ""
    counter = 0
    messospazio = False
    with open(fname2) as f:
            testo = f.read()
            testo = testo.split()
            f.close()
    decrypter = {}
    for i in range(0,len(testo),2):
        decrypter[testo[i+1]] = testo[i]
    print(decrypter)
    with open(fname1) as f:
            testo = f.read()
            testo = testo.split(" ")
            f.close()
    print(testo)
    for i in testo:
        if len(i) == 0:
            result += " "
        else:
            messospazio = False
            for j in range(0, len(i), 3):
                if len (i[j:j+3]) == 3:
                    if i[j:j+3] in decrypter.keys():
                        result += decrypter[i[j:j+3]]
                    elif i[j:j+3] != "?":
                        print(f"daje roma daje roma {i[j:j+3]}")
                        result += "?"
                        counter += 1
                else:
                    result += i[j:j+3]
            result += " "
    result = result[:-1]
    with open(fname3,'w') as f:
            f.write(result)
            f.close()
    print(result)
    return counter

print(es30('ftesto2.txt','ftesto2b.txt','risposta2.txt'))