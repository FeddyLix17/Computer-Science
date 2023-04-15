##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Valerio
# Cognome:  Fontana
# Matricola: 2046790
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    buffer: .space 20

.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 20      # Alloca al massimo 20 caratteri
    syscall         # $a0 contiene l'indirizzo base della stringa

##########################################
## INSERIRE IL CODICE QUI
    li $t1, -1                                                  # $t1 = indice della stringa
    li $t2, '0'                                                 # $t2 = valore ascii da sottrarre al carattere corrente per ottenere il suo valore numerico
    li $t3, 0                                                   # $t3 = contatore dei numeri divisibili per 2
    li $t4, 0                                                   # $t4 = contatore dei numeri divisibili per 4
    li $t5, 0                                                   # $t5 = variabile temporanea per l'operazione logica AND che verificherà se il numero corrente è divisibile per 4
    li $t6, 0                                                   # $t6 = variabile temporanea per l'operazione logica AND che verificherà se il numero corrente è divisibile per 2

Solution:
    addi $t1, $t1, 1                                            # incremento l'indice della stringa
    lb $a0, buffer($t1)                                         # carico il carattere corrente in $a0
    sub $a0, $a0, $t2                                           # sottraggo il valore ascii di '0' per ottenere il valore numerico del carattere corrente
    beq $a0, $zero, Solution                                    # se il valore numerico del carattere corrente è 0, allora passo al prossimo carattere, come richiesto dall'esercizio
    bltz $a0, end_program                                       # l'esercizio ci fa presente che ogni stringa termina con \n, avendo '0' con un valore ascii maggiore di quello di \n
                                                                # se il valore numerico del carattere corrente è minore di 0, allora ho raggiunto la fine della stringa

    # un numero binario è divisibile per 2^n se e solo se le sue n cifre meno significative sono uguali a 0
    # ad esempio, 4 in binario è 100, che è divisibile per 2^2, in quanto le sue 2 cifre meno significative sono uguali a 0
    # mentre ad esempio 5 in binario è 101, che non è divisibile per 2^2, in quanto non tutte le sue 2 cifre meno significative sono uguali a 0
    # nel nostro primo caso ad esempio, dobbiamo verificare se il numero è divisibile per 4, quindi dobbiamo verificare se le sue 2 cifre meno significative sono uguali a 0
    # per farlo applichiamo l'operazione logica AND tra il numero corrente e 3, che in binario è uguale a 11. In questo modo tale operazione restituirà 0 se e solo se le 2 cifre meno significative del numero corrente sono uguali a 0
    andi $t5, $a0, 3                                    
    beqz $t5, divisibile_per_4                                  # se $t5 = 0, quindi se l'operazione logica AND ha restituito come risultato 0, allora entro nella funzione 
    
    # nel caso in cui il numero corrente non sia divisibile per 4, proseguo col flusso del codice e verifico se invece è divisibile per 2
    # allo stesso modo, un numero binario è divisibile per 2 se e solo se la sua ultima cifra meno significativa è uguale a 0
    andi $t6, $a0, 1
    beqz $t6, divisible_by_2

    # nel caso in cui il numero corrente non sia neanche divisibile per 2, semplicemente passo al carattere successivo
    j Solution                                                  # passo al carattere successivo

divisible_by_2:
    addi $t3, $t3, 1                                           # essendo il numero corrente divisibile per 2, incremento il contatore dei numeri divisibili per 2
    j Solution                                                 # passo al carattere successivo
divisibile_per_4:
    addi $t3, $t3, 1                                           # essendo il numero corrente divisibile per 4, incremento il contatore dei numeri divisibili per 4
    addi $t4, $t4, 1                                           # e di conseguenza sarà anche divisibile per 2, quindi incremento anche il contatore dei numeri divisibili per 2
    j Solution                                                 # passo al carattere successivo

end_program:
    # stampo il numero di numeri divisibili per 2
    li $v0, 1
    move $a0, $t3
    syscall

    #vado a capo
    li $v0, 11
    li $a0, '\n'
    syscall

    # stampo il numero di numeri divisibili per 4
    li $v0, 1
    move $a0, $t4
    syscall

    # esco dal programma
    li $v0, 10
    syscall