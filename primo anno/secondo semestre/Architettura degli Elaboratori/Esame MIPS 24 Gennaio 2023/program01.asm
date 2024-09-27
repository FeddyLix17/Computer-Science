##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26
    output: .byte  0,0,0,0,0,0,0,0,0  # Un carattere extra per la fine della stringa

.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    syscall         # $a0 contiene l'indirizzo base della stringa
    la $a2, output
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI
    move $t0, $zero     # $t0 = Indice del Bit del Numero Binario da convertire in Ottale
    move $t1, $zero     # $t1 = Indice bit più a sinistra
    move $t2, $zero     # $t2 = Indice bit centrale
    move $t3, $zero     # $t3 = Indice bit più a destra
    move $t4, $zero     # $t4 = Valore Ottale del numero binario corrente convertito
    move $t5, $zero     # $t5 = Indice Array Output

BinaryToOctal:
    # carico il bit più a sinistra del numero binario
    lb $t1, buffer($t0)
    addi $t0, $t0, 1

    # carico il bit centrale del numero binario
    lb $t2, buffer($t0)
    addi $t0, $t0, 1

    # carico il bit più a destra del numero binario
    lb $t3, buffer($t0)

    # converto ogni bit (preso in input sotto forma di carattere) nel suo corrispettivo valore numerico
    sub $t3, $t3, '0'
    sub $t2, $t2, '0'  
    sub $t1, $t1, '0'  

    # se $t3 < 0, quindi nel caso in cui il bit meno significativo tra i 3 sia un carattere diverso da 0 o 1,
    # quindi o nel caso in cui la sequenza sia terminata o nel caso in cui l'ultima sequenza sia formata da meno di 3 bit,
    # esco dal programma
    bltz $t3, PrepareForPrintOutput

    # se invece sono di fronte ad una sequenza di 3 bit completa,
    # controllo il valore di ogni bit e incremento il risultato ($t4) di conseguenza
    beq $t3, 1, Add1ToResult
    beq $t2, 1, Add2ToResult
    beq $t1, 1, Add4ToResult

    # nel caso in cui la sequenza sia formata da 3 bit uguali a 0,
    # salvo il risultato in output e passo alla sequenza di 3 bit successiva
    sb $t4, output($t5)             # salvo il risultato in output
    move $t4, $zero                 # resetto il registro per poter salvare il risultato della sequenza successiva
    addi $t5, $t5, 1                # incremento l'indice dell'array output
    addi $t0, $t0, 1                # e passo alla sequenza di 3 bit successiva
    addi $v1, $v1, 1                # incrementando il numero di sequenze di 3 bit convertite

    j BinaryToOctal

Add1ToResult:
    addi $t4, $t4, 1    # incremento il risultato di 1
    beq $t2, 1, Add2ToResult
    beq $t1, 1, Add4ToResult
    j SaveResultToArray

Add2ToResult:
    addi $t4, $t4, 2    # incremento il risultato di 2
    beq $t1, 1, Add4ToResult
    j SaveResultToArray

Add4ToResult:
    addi $t4, $t4, 4    # incremento il risultato di 4
    j SaveResultToArray

SaveResultToArray:
    sb $t4, output($t5) # salvo il risultato in output
    addi $t5, $t5, 1    # incremento l'indice dell'array output
    addi $v1, $v1, 1    # incremento il numero di caratteri prodotti in output
    addi $t0, $t0, 1    # passo alla sequenza di 3 bit successiva
    move $t4, $zero     # resetto il risultato
    j BinaryToOctal

PrepareForPrintOutput:
    # preparo il programma per la stampa del numero ottale
    sge $t6, $t1, 0     # se $t1 >= 0, quindi se il bit più a sinistra del numero binario è un 0 o un 1,
    move $t5, $zero     # resetto l'indice dell'array output
    li $v0, 1
    j PrintOutput

# stampo ogni cifra del numero ottale
PrintOutput:
    lb $a0, output($t5)
    beq $t5, $v1, Exit      # se ho stampato tutte le cifre del numero ottale, mi preparo a stampare il contenuto di $v0 e $v1
    syscall
    addi $t5, $t5, 1
    j PrintOutput

StampaNuovaRiga:
    # stampo una nuova riga
    li $v0, 11
    li $a0, '\n'
    syscall
    jr $ra

Exit:
    # dopo aver stampato il numero ottale, stampo su due righe separate il contenuto di $v0 e $v1
    jal StampaNuovaRiga

    # dove il contenuto di $v0 sarà 0 se tutta la stringa di input è stata tradotta, altrimenti 1
    li $v0, 1
    move $a0, $t6
    syscall
    jal StampaNuovaRiga

    # mentre il contenuto di $v1 sarà il numero di sequenze di 3 bit convertite
    li $v0, 1
    move $a0, $v1
    syscall

    # termino il programma
    li $v0, 10
    syscall