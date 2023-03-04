# <p align=center> Capitolo3 Esercizio12 </p>
Creare la classe Car che rappresenti un’automobile e il suo
consumo di carburante. <br>

Attributi:

- *Gas*: privata e di tipo *double*, rappresenta i litri di carburante
rimanente
- *Efficiency*: privata e d tipo double, rappresenta il numero di km
per litro che la macchina può fare

Costruttore e metodi:

- *Car*: il costruttore dovrà essere ridefinito accettando un
parametro che rappresenti l’efficienza dell’auto in modo tale da
essere assegnato al corrispondente attributo. L’attributo gas
invece dovrà essere valorizzato a 0.

- *addGas*: incrementa l’attributo *gas* di un valore pari a quello del parametro passato al metodo

- *Drive*: simula un viaggio in auto di una distanza pari a quella del
parametro passato alla funzione. In virtù di ciò, il carburante
dovrà essere diminuito in base all’efficienza dell’automobile.

- *getGasInTank*: ritorna l’ammontare di carburante residuo

La classe *CarTester* creerà un’auto con un efficienza di
50km/litro. <br>
Dopodiché, effettuerà un rifornimento di 20 litri di
carburante e guiderà per 100km. <br>
A fine viaggio, dovrà essere stampato il carburante residuo, accertandosi che sia pari a 18 litri.

<details closed>

<summary> Soluzione Personale </summary>

[Car.java]<https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_12/src/Esercizio12/Car.java()> <br>
[CarTester.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_12/src/Esercizio12/CarTester.java)
</details>

<details closed>

<summary> Soluzione Professore </summary>

[Car.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_12/src/Esercizio12Prof/Car.java) <br>
[CarTester.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_12/src/Esercizio12Prof/CarTester.java)

</details>
