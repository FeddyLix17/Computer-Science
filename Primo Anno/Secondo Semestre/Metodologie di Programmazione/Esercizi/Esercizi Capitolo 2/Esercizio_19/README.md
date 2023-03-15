# <p align="center"> Capitolo2 Esercizio19 </p>

Creare una finestra che contenga due rettangoli, uno interno dell’altro, e visualizzarla a video. <br>

**Consiglio**: Utilizzare le seguenti classi: <br>

- *java.awt.Color*

- *java.awt.Graphics*

- *java.awt.Graphics2D*

- *java.awt.Rectangle*

- *javax.swing.JComponent*

- *javax.swing.JFrame*

È richiesta la creazione di una finestra con una sua dimensione impostata tramite il metodo *setSize()*, che si chiuda cliccando sulla X (*setDefaultCloseOperation()*). <br>

Successivamente, sarà necessario aggiungere i due oggetti di tipo *Rectangle*. <br>

Per raggiungere questo scopo, occorre creare un oggetto di tipo *Graphics2D* che fungerà da "contenitore" per i nostri *Rectangle*, i quali dovranno essere creati con dei parametri opportunamente scelti in modo tale che il secondo si trovi all’interno del primo. <br>

L’aggiunta dei due rettangoli all’interno del contenitore di tipo
*Graphics2D* avviene grazie al metodo *draw(oggetto Rectangle)*. <br>

Una volta fatto questo, la nostra finestra di tipo *JFrame* dovrà aggiungere questo contenitore tramite il metodo *add(oggetto Graphics2D)*.