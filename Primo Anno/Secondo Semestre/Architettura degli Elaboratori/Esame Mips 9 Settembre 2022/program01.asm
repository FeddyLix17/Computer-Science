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
    lb $a0, buffer($t0)     # $a0 = buffer[$t0]
    lb $a1, buffer($t1)     # $a1 = buffer[$t1] = buffer[$t0 - 1]
    sub $a0, $a0, '0'       # $a0 = valore numerico rappresentato dal carattere contenuto in $a0
    sub $a1, $a1, '0'       # $a1 = valore numerico rappresentato dal carattere contenuto in $a1
    bltz $a0, VerificaUltimoCarattere   # Se $a0 < 0, significa che ho finito di leggere la stringa
    add $v1, $v1, $a1       # $v1 = $v1 + $a0
    beq $a0, $a1, CoppiaCaratteriUguali  # Se $a0 == $a1, incremento il numero delle volte che la stringra pre
    j Solution

CoppiaCaratteriUguali:
    addi $v0, $v0, 1        # $v0 = $v0 + 1
    j Solution

VerificaUltimoCarattere:
    bgtz $a1, SommaUltimoCarattere
    j Fine

SommaUltimoCarattere:
    add $v1, $v1, $a1
    j Fine
Fine:
    # stampo $v0 e $v1 su 2 righe separate
    move $a2, $v0
    move $a3, $v1
    li $v0, 1
    move $a0, $a2
    syscall

    li $v0, 11
    li $a0, '\n'
    syscall
    
    li $v0, 1
    move $a0, $a3
    syscall
    
    li $v0, 10
    syscall