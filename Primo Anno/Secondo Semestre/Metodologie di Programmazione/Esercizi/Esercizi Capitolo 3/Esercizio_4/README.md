# <p align=center> Capitolo3 Esercizio4 </p>

Creare una classe *Circuit* che gestisca l’illuminazione di un corridoio. <br>

Attributi: tutti e tre private

- *firstSwitch*: può assumere due valori: 1 o 0, che rappresentano
rispettivamente il selezionamento o meno della prima lampada
- *secondSwitch*: come firstSwitch, ma riferita alla seconda
lampada
- *lampState*: rappresenta lo presenza o meno di corrente,
valorizzata con i valori 0 o 1 analogamente agli attributi
precedenti

Metodi:
- *getFirstSwitchState*: ritorna il valore di *firstSwitch*
- *getSecondSwitchState*: ritorna il valore di *secondSwitch*
- *getLampState*: ritorna il valore di *lampState*
- *toggleFirstSwitch*: cambia lo stato di *firstSwitch* e *lampState* da 0 a 1 e viceversa
- *toggleSecondSwitch*: cambia lo stato di secondSwitch e
lampState da 0 a 1 e viceversa

La classe *CircuitTester* dovrà essere costruita accertandosi che
l’esecuzione consecutiva dello stesso *toggleSwitch* riporti lo stato
dello switch corrispondente e della lampada a zero. Per controllare il contenuto dei diversi attributi durante i test, 
stampare il valore ritornato dai metodi *get*.


<details closed>

<summary> Soluzione Personale</summary>

[Circuit.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_4/src/Esercizio4/Circuit.java) <br>
[CircuitTester.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_4/src/Esercizio4/CircuitTester.java)

</details>

<details closed>

<summary> Soluzione Professore</summary>

[Circuit.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_4/src/Esercizio4Prof/Circuit.java) <br>
[CircuitTester.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_4/src/Esercizio4Prof/CircuitTester.java)
</details>
