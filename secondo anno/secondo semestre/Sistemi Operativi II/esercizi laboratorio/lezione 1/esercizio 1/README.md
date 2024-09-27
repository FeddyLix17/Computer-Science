<div align="center">

# lezione 1 - esercizio 1

</div>

- Provare qualche opzione del comando man di Linux.

Il comando *man* in Linux visualizza le pagine del manuale per i comandi, le funzioni di sistema e altri argomenti.

È utilizzato per ottenere informazioni dettagliate sull'uso, le opzioni e la sintassi di comandi e programmi disponibili nel sistema.

Le pagine del manuale sono organizzate in sezioni, ciascuna delle quali copre una categoria specifica come comandi utente, chiamate di sistema, funzioni di libreria e file di configurazione.

Ad esempio il comando

```bash
man ls
```

restituisce la pagina del manuale per il comando *ls* (il quale elenca i file e le directory presenti in una directory specifica).

Alcune opzioni delle quali è possibile fare uso sono

```bash
man -f ls
```

il quale restituirà una breve descrizione di tutte le pagine del manuale che hanno *ls* nel loro nome (equivalente a usare il comando *whatis ls*).

```bash
man -a ls
```

per cui si andranno a visualizzare tutte le pagine del manuale relative al comando *ls* in successione.

```bash
man -k ls
```

dove verrà restituito l'elenco di tutte le pagine del manuale che contengono la parola chiave *ls* nella loro descriizione (equivalente a usare il comando *apropos ls*).

```bash
man -w ls
```

il quale restituirà il percorso del file della pagina del manuale per il comando *ls*.

```bash
man -I ls
```

in modo da cercare il rispettivo comando passato come argomento in tutte le sezioni del manuale, tenendo conto delle maiuscole-minuscole (dunque stavolta i possibili altri argomenti *LS*, *Ls* e *lS*, come logicamente giusto che sia, non verranno considerati equivalenti).
