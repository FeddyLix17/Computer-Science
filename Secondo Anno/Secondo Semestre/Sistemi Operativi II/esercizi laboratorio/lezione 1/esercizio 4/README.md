<div align="center">

# lezione 1 - esercizio 4

</div>

- Trovare un’apposita invocazione di ps che ritorni solo il pid (process
id) della shell.

Seguendo la falsariga dell'esercizio precedente, basterà semplicemente cambiare il campo desiderato da CMD a PID.

```bash
ps -p $$ -opid -h
```
