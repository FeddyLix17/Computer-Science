##########################################
# INSERIRE I PROPRI DATI QUI
# Nome:         Valerio
# Cognome:      Fontana
# Matricola:    2046790
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
    li $t0, 0              # Contatore
    li $v0, 0              # Numero di coppie di caratteri uguali
    li $v1, 0              # Somma dei valori numerici rappresentati dai caratteri della stringa

Solution:
    addi $t0, $t0, 1        # Incremento contatore
    sub $t1, $t0, 1         # $t1 = $t0 - 1
    lb $t2, buffer($t0)     # $t2 = buffer[$t0]
    lb $t3, buffer($t1)     # $t3 = buffer[$t1] = buffer[$t0 - 1]
    sub $t2, $t2, '0'       # $t2 = valore numerico rappresentato dal carattere contenuto in $t2
    sub $t3, $t3, '0'       # $t3 = valore numerico rappresentato dal carattere contenuto in $t3
    bltz $t2, VerificaUltimoCarattere   # Se $t2 < 0, significa che ho finito di leggere la stringa
    add $v1, $v1, $t3       # $v1 = $v1 + $t2
    beq $t2, $t3, CoppiaCaratteriUguali  # Se $t2 == $t3, incremento il numero delle volte che la stringra pre
    j Solution

CoppiaCaratteriUguali:
    addi $v0, $v0, 1        # $v0 = $v0 + 1
    j Solution

VerificaUltimoCarattere:
    bgtz $t3, SommaUltimoCarattere
    j Fine

SommaUltimoCarattere:
    add $v1, $v1, $t3
    j Fine

Fine:
    # stampo $v0 e $v1 su 2 righe separate
    move $t0, $v0
    move $t1, $v1
    li $v0, 1
    move $a0, $t0
    syscall

    li $v0, 11
    li $a0, '\n'
    syscall
    
    li $v0, 1
    move $a0, $t1
    syscall
    
    li $v0, 10
    syscall