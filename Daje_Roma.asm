.globl dajeroma

.data
    CarattereDelSium: .byte 'A'
    NumeroInteroDelSium: .word 42
    SecondoNumeroInteroDelSium: .word 36
    NnamoAcapoDajeh: .byte '\n'
    NumeroFloatDelSium: .float 1.23
    NumeroDoubleDelSium: .double 4.56
    SecondoNumeroDoubleDelSium: .double 7.89

.text
    dajeroma:
        #stampo un carattere
        li $v0, 11
        lb $a0, CarattereDelSium
        syscall
        
        #vado a capo
        jal toccaAnnaAcapo

        #stampo un intero
        li $v0, 1
        lw $a0, NumeroInteroDelSium
        syscall
        
        #vado a capo
        jal toccaAnnaAcapo
        
        # stampo un float
        li $v0, 2
        lwc1 $f12, NumeroFloatDelSium
        syscall

        #vado a capo
        jal toccaAnnaAcapo

        # stampo un double
        li $v0, 3
        ldc1 $f12, NumeroDoubleDelSium
        syscall
        
        #vado a capo
        jal toccaAnnaAcapo

        #addizziono i 2 double
        ldc1 $f0, NumeroDoubleDelSium
        ldc1 $f2, SecondoNumeroDoubleDelSium
        add.d $f12, $f0, $f2
        #stampo il risultato
        li $v0, 3
        syscall

        #vado a capo
        jal toccaAnnaAcapo

        # addizziono i 2 interi
        lw $t1, NumeroInteroDelSium
        lw $t2, SecondoNumeroInteroDelSium
        add $t3, $t1, $t2

        #stampo il risultato
        li $v0, 1
        move $a0, $t3
        syscall

        #vado a capo
        jal toccaAnnaAcapo

        # sottraggo i 2 interi
        sub $t3, $t1, $t2

        #stampo il risultato
        li $v0, 1
        move $a0, $t3
        syscall

        #vado a capo
        jal toccaAnnaAcapo

        #esco dal programma
        li $v0, 10
        li $a0, 0
        syscall

    toccaAnnaAcapo:
        li $v0, 11
        lb $a0, NnamoAcapoDajeh
        syscall
        jr $ra