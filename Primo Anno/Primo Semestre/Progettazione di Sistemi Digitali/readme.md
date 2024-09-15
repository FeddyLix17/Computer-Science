<div align="center">

<img src="https://antmicro.com/blog/images/systemverilog.svg" width=60% >

# Progettazione di Sistemi Digitali

</div>

## About 🔎

Il corso di *Progettazione di Sistemi Digitali* fornisce

- una panoramica completa sul sistema numerico binario

- un'introduzione ai circuiti logici, sia combinatori che sequenziali, e la costruzione di blocchi costruttivi digitali tramite questi ultimi

- un'approfondimento sul linguaggio descrittivo dell'hardware *SystemVeriLog*, per poter codificare e sintetizzare i relativi circuiti digitali

## Testi consigliati dal docente📚

[Digital Design and Computer Architecture, 2nd edition, 2012](https://moodle.tktk.ee/pluginfile.php/270005/mod_resource/content/1/Harris%20D.%20M.%2C%20Harris%20S.%20L.%20-%20Digital%20Design%20and%20Computer%20Architecture%2C%202nd%20Edition%20-%202012.pdf)

## Lezioni 👨‍🏫

È possibile accedere a tutte le risorse usate durante le lezioni nel rispettivo [classroom](https://classroom.google.com/c/MTczNjk2NDI1MjI5?cjc=blb53dw)

## Esercizi 📝

È possibile consultare esercizi e tracce di esami precedenti nella rispettiva [repository](https://github.com/sapienzastudentsnetwork/progettazione-di-sistemi-digitali) di [SapienzaStudentNetwork](https://github.com/sapienzastudentsnetwork/)

<table align="center">
    <tr>
        <td colspan="4" align="center">
            <h3>Implementazioni di compomenti <br> digitali in Systemverilog</h3>
        </td>
    </tr>
    <tr>
        <td>
            <table>
                <tr>
                    <td align="center">Latch</td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Latch/SR latch.sv"> SR latch </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Latch/D latch.sv"> D latch </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Latch/JK latch.sv"> JK latch </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Latch/T latch.sv"> T latch </a> </td>
                </tr>
            </table>
        </td>
        <td>
            <table>
                <tr>
                    <td align="center">Flip-Flop</td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Flip Flop/SR flip-flop.sv"> SR flip-flop </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Flip Flop/D flip-flop.sv"> D flip-flop </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Flip Flop/JK flip-flop.sv"> JK flip-flop </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Flip Flop/T flip-flop.sv"> T flip-flop </a> </td>
                </tr>
            </table>
        </td>
    <td>
      <table>
        <tr>
          <td align="center">Finite State Machine</td>
        </tr>
        <tr>
          <td align="center"> <a href="./Systemverilog/Macchine a Stati Finiti (FSM)/Mealy FSM.sv"> Mealy </a>, <a href="https://images.app.goo.gl/vjEfJL1uaThxQXBB6"> esempio </a> </td>
        </tr>
        <tr>
          <td align="center"> <a href="./Systemverilog/Macchine a Stati Finiti (FSM)/Moore FSM.sv"> Moore </a>, <a href="https://images.app.goo.gl/h74KNVzLzM1qNs9W8"> esempio </a> </td>
        </tr>
        <tr>
          <td align="center"> ... </td>
        </tr>
        <tr>
          <td align="center"> ... </td>
        </tr>
      </table>
    </td>
    <td>
            <table>
                <tr>
                    <td align="center"> Blocchi Digitali </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Blocchi Digitali/Adders.sv"> sommatori </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Blocchi Digitali/Shifters.sv"> shifter </a> </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Blocchi Digitali/Multipliers.sv"> moltiplicatori </td>
                </tr>
                <tr>
                    <td align="center"> <a href="./Systemverilog/Blocchi Digitali/Aritmetic Logic Unit.sv"> ALU </a> </td>
                </tr>
            </table>
        </td>
  </tr>
</table>

- <details closed>
      
    <summary> TestBench </summary>

  - [TestBench a 3 input](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Primo%20Semestre/Progettazione%20di%20Sistemi%20Digitali/Sysverilog/TestBench/test%20circuito%20a%203%20input.sv)

  </details>

## Other 🔗

- [DigitalJS](https://digitaljs.tilk.eu) per sintetizzare i circuiti descritti in *SystemVeriLog*

- [EdaPlayground](https://www.edaplayground.com/) per compilare codice *SystemVeriLog*

- [Boolean Algebra](https://www.boolean-algebra.com/) per semplificare espressioni booleane

- [IEEE 754 Calculator](https://weitz.de/ieee/) per verificare i calcoli eseguiti con il medesimo standard

<div align="center">

[***Torna alla Home***](../../../)

</div>
