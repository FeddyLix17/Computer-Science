# <p align=center> Capitolo3 Esercizio9 </p>

Creare una classe chiamata *CashRegister* che rappresenti il
funzionamento di un registratore di cassa. <br>

Attributi:

- *Purchase*: privato e di tipo *double*, contiene l’importo totale dei
prodotti che si vogliono acquistare
- *Payment*: privato e di tipo *double*, contiene l’importo ricevuto
dall’acquirente per il pagamento dei prodotti
- *History*: private e di tipo *String*, rappresenta lo scontrino con al suo interno i prezzi dei prodotti acquistati

Metodi:

- *recordPurchase*: registra la vendita di un prodotto, ricevendo in
input un parametro che indichi il prezzo del prodotto che
acquistato. Tale funzione dovrà aggiornare l’importo totale dei
prodotti acquistati, aggiornando lo scontrino con l’aggiunta di
una nuova riga che contiene il prezzo del prodotto appena
scelto
- *receivePayment*: simula il passaggio di denaro tra acquirente e
venditore, aggiornando l’attributo relativo agli importi ricevuti
- *giveChange*: simula il calcolo del resto, ossia la differenza tra i soldi forniti dall’acquirente per il pagamento e l’importo totale.
Una volta calcolato il resto, il contenuto dello scontrino e i due
totali dovranno essere azzerati. Il resto dovrà essere ritornato
dalla funzione come output.
- *printReceipt*: stampa il contenuto dello scontrino e,
successivamente, il totale dei prodotti acquistati.

La classe *CashRegisterTest* dovrà simulare un normale
acquisto, aggiungendo l’importo di diversi prodotti tramite la
*recordPurchase* e poi fornendo i soldi per il pagamento tramite
la *receivePayment*. <br>
Prima di chiamare la *giveChange* per dare il
resto, l’esecuzione del programma dovrà stampare il contenuto
dello scontrino tramite la *printReceipt*.

<details closed>

<summary> Soluzione Personale </summary>


</details>

<details closed>

<summary> Soluzione Professore </summary>

</details>
