# <p align=center> Capitolo3 Esercizio16 </p>

Creare una classe *Moth* che simuli il movimento di una libellula.

*Attributi:*

- *Position*: privata e di tipo *double*, rappresenta la posizione della
libellula

*Costruttore:*

- *Moth*: ridefinito per accettare come parametro la posizione
iniziale della libellula, assegnandola al corrispettiva parametro.

Metodi:

- *moveToLight*: muove la libellula verso la posizione della lfonte
di luce, fornita come parametro. <br> La nuova posizione della
libellula coinciderà con la metà della distanza tra la posizione
attuale e quella della fonte di luce.

- *getPosition*: ritorna la posizione attuale della libellula

La classe *MothTester* creerà una libellula la cui posizione
iniziale è pari a 10. <br>
Successivamente, effettuerà 3 movimenti:

- Il primo verso una fonte di luce in posizione 0

- Il secondo verso una fonte di luce in posizione 10

- Il terzo verso una fonte di luce in posizione 0

Ai fini del corretto funzionamento, la sequenza delle posizioni
della libellula dovrà essere la seguente: <br>
5, 7.5, 3.75