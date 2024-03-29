##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:         Valerio
# Cognome:      Fontana
# Matricola:    
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
    li $t0, -1                          # $t0 = indice sequenza di caratteri
    li $v0, 0                           # $v0 = numero di zeri presenti nella sequenza di caratteri
    li $v1, 0                           # $v1 = numero di uni presenti nella sequenza di caratteri
    jal contaOccorrenze                 # salto a contaOccorrenze
    
    # una volta calcolati il numero di zeri e uni presenti nella sequenza di caratteri,
    # come richiesto dalla traccia, li stampo in 2 righe separate

    # stampo il numero di zeri (contenuto in $v0)
    move $a0, $v0
    li $v0, 1
    syscall
    
    # vado a capo
    li $v0, 11
    li $a0, '\n'
    syscall
    
    # e infine stampo il numero di uni (contenuto in $v1)
    li $v0, 1
    move $a0, $v1
    syscall

    # termino il programma
    li $v0, 10
    syscall

contaOccorrenze:
    addi $t0, $t0, 1                    # $t0 = $t0 + 1
    lb $a0 buffer($t0)                  # $a0 = buffer[$t0]

    sub $a0, $a0, '0'                   # $a0 = equivalente valore numerico del carattere contenuto in $a0/buffer[$t0] (in questo caso o 0 o 1)
    beqz $a0, NumeroUgualeAZero         # se $a0 == 0, incremento il numero di zeri presenti (quindi il registro $v0) di 1
    beq $a0, 1, NumeroUgualeAUno        # se invece $a0 == 1, incrementa il numero di uni presenti (quindi il registro $v1) di 1
    bltz $a0, EndLoop                   # una volta raggiunta la fine della sequenza di caratteri, salto a EndLoop
    j contaOccorrenze

NumeroUgualeAZero:
    addi $v0, $v0, 1                    # $v0 = $v0 + 1
    j contaOccorrenze

NumeroUgualeAUno:
    addi $v1, $v1, 1                    # $v1 = $v1 + 1
    j contaOccorrenze

EndLoop:
    jr $ra                              # ritorno all'istruzione successiva a jal contaOccorrenze