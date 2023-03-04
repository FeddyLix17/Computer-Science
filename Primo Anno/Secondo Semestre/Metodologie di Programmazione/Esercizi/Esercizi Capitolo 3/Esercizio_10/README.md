# <p align=center> Capitolo3 Esercizio10

Estendere la classe *CashRegister* dell’esercizio precedente
inserendo due nuovi attributi:

- *salesTotal*: privata e di tipo *double*, memorizza il totale di tutte
le vendite avvenute

- *salesCount*: privata e di tipo *int*, memorizza il numero totale di vendite avvenute

Il costruttore e i metodi invece dovranno essere modificati nel
seguente modo:

- Costruttore: dovrà assegnare il valore 0 ai due nuovi attributi
- *recordPurchase*: l’importo dell’oggetto venduto dovrà essere aggiunto al valore attuale di *salesTotal*
- *giveChange*: poiché questo metodo conclude un acquisto, l’attributo *salesCount* dovrà essere incrementato di una unità

Dovranno essere aggiunti invece i seguenti metodi:

- *getSalesTotal*: ritornerà il valore attuale di *salesTotal*
- *getSalesCount*: ritornerà il valore attuale di *salesCount*
- *Reset*: reimposterà a 0 i valori di *salesTotal* e *salesCount*

La classe *CashRegisterTester* in questo caso dovrà accertarsi che, a
fronte vari acquisti, la *getSalesCount* e la *getSalesTotal* ritornino
rispettivamente il totale ed il numero delle vendite avvenute fino al
momento delle due chiamate.

<details closed>
<summary> Soluzioni Personali </summary>

[CashRegister.java]() <br>
[CashRegisterTester.java]()
</details>
<details closed>
<summary> Soluzioni professore </summary>

[CashRegister.java]() <br>
[CashRegisterTester.java]()
</details>
