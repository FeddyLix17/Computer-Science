# <p align=center>Capitolo3 Esercizio 1 </p>
Creare una classe *Counter* che rappresenti il funzionamento di un contatore. <br>
Al suo interno sarà presente un campo privato, di tipo intero, che memorizzi il suo valore attuale. <br> 
Dal punto di vista delle funzionalità, la classe conterrà:
- Un metodo *getValue* che ritorni il valore attuale del contatore
- Un metodo *click* che permetta l’incremento del campo di un’unità
- Un metodo *reset* che reimposti il valore del campo a 0
- Un metodo *undo* che annulli l’ultima esecuzione di click, evitando che il valore del campo non scenda sotto allo zero. 

La classe *CounterTester* dovrà:
- Creare un oggetto di tipo *Counter*
- Incrementare il contatore di tre unità
- Stampare il suo valore
- Decrementare il contatore di un’unità
- Stampare il suo valore, controllando che sia pari a due
- Decrementare il contatore di tre unità
- Stampare il suo valore, controllando che sia pari a zero

Consiglio: la classe *Math* offre il metodo *max()* che può essere utilizzato nella definizione di
undo per evitare che il decremento porti ad avere un numero negativo

<details closed>
<summary> Soluzioni Personali </summary>
</details>
<details closed>
<summary> Soluzioni professore </summary>
