# <p align=center> Capitolo3 Esercizio6 </p>

Realizzare un gestore di un conto bancario. <br>
Attributi:

- Balance: di tipo double, privata. Rappresenta il saldo del conto <br>

Costruttore: ridefinire il costruttore di default in modo tale che:
- Un oggetto istanziato senza parametri contenga un saldo pari a
zero
- Un oggetto può essere istanziato con un saldo fornito da input,
valorizzando il corrispettivo attributo <br>

Metodi:

- Deposit: effettua un deposito, incrementando il saldo attuale di
un ammontare pari al valore del parametro passato
- Withdraw: effettua un prelievo, decrementando saldo attuale di
un ammontare pari al valore del parametro passato
- getBalance: restituisce il valore attuale del saldo

La classe BankAccountTester accerterà il corretto funzionamento
della classe depositando inizialmente un valore pari a mille.
Successivamente, dovranno essere fatti due prelievi: uno da 500 e
uno da 400. Stampare quindi il valore del saldo, accertandosi che il
saldo risultante sia pari a 100.

<details closed> 

<summary> Soluzione Personale </summary>

[BankAccount.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_6/src/Esercizio6/BankAccount.java) <br>
[BankAccountTester.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_6/src/Esercizio6/BankAccountTester.java)
</details>

<details closed>

<summary> Soluzione Professore </summary>

[BankAccount.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_6/src/Esercizio6Prof/BankAccount.java) <br>
[BankAccountTester.java](https://github.com/FedVlogger17/Uni-Notes/blob/main/Primo%20Anno/Secondo%20Semestre/Metodologie%20di%20Programmazione/Esercizi/Esercizi%20Capitolo%203/Esercizio_6/src/Esercizio6Prof/BankAccountTester.java)
</details>
