# <p align=center> Capitolo3 Esercizio2 </p>

Estendere l’esercizio precedente aggiungendo un ulteriore campo privato e di tipo intero che rappresenti il valore massimo assumibile dal contatore. <br>
Tale valore è impostabile esclusivamente tramite il metodo *setLimit*, il quale accetta un parametro di tipo intero. <br>
L’introduzione di questo limite modificherà il comportamento del metodo *click*. <br> 
Infatti, non sarà possibile incrementare ulteriormente il contatore oltre il valore massimo. <br>
La classe CounterTester riprenderà il comportamento di quella vista nell’esercizio precedente. <br>
La differenza risiederà nel fatto che il primo metodo chiamato sarà *setLimit*, il quale dovrà
impostare il valore massimo del contatore a tre. <br>
L’efficacia di questo limite dovrà essere accertata chiamando quattro volte di fila il metodo click e accertarsi che il valore attuale del contatore sia pari a tre.
