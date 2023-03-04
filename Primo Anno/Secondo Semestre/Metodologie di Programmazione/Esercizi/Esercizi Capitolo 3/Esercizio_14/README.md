# <p align=center> Capitolo3 Esercizio14 </p>

Creare la classe Letter che rappresenta il contenuto di una
lettera.

Attributi:

- *Sender*: privata e di tipo *String*, rappresenta il mittente della
lettera

- *Recipient*: privata e di tipo *String*, rappresenta il destinatario
della lettera

- *Body*: privata e di tipo *String*, rappresenta il corpo della lettera

Costruttore:

- *Letter*: ridefinito per accettare, come parametri, un mittente e un
destinatario al fine di valorizzare i corrispettivi attributi. Il corpo
sarà automaticamente valorizzato con una stringa vuota.

Metodi:

- *addLine*: concatena il contenuto dell’attributo *body* e la stringa
passata come parametro, andando a capo.

- *getText*: ritorna il contenuto della lettera, con il seguente
formato: <br>
*Caro {recipient},* <br>
*{body}* <br> <br>
*Tuo,* <br>
*{mittente}*

**Consiglio**: per il concatenamento di due stringhe, guardare il
metodo *concat()* della classe *String*. <br>

La classe *LetterPrinter* creerà una lettera con un mittente ed un
destinatario, costruendo il corpo tramite l’inserimento di tre
righe a piacere. <br>
Stampare il contenuto della lettera per
verificarne il corretto funzionamento.
