<div align="center">

# lezione 3 - esercizio 3

</div>

- Dal *man* di *ps* cercare di capire perché

```bash
ps –p $$ –ocmd –h
```

- Restituisce bash come output

analizzando le pagine del manuale di *ps* si può notare che:

1. l'opzione *-p* permette di specificare il PID del processo di cui si vogliono visualizzare le informazioni.

2. i due dollari ($$) sono una variabile speciale che in linux rappresentano l'ID del processo della shell corrente.

> [!NOTE]  
> è possibile unire le varie opzioni di un comando in un'unica stringa, come nel caso di *-ocmd*, tuttavia le rispettive opzioni vanno analizzate singolarmente

3. l'opzione *-o* permette di specificare i campi da visualizzare, in questo caso *cmd* che rappresenta il comando eseguito dal processo (gli altri campi tra cui poter scegliere sono PID, TTY e TIME). Sintatticamente sarebbe possibile anche scrivere *-o cmd*.

4. l'opzione *-h*, messa alla fine del comando permette di omettere l'intestazione del campo selezionato, lasciando infine solo il valore del campo selezionato (bash).
