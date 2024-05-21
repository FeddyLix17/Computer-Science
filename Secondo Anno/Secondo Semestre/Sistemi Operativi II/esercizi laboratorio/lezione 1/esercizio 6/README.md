<div align="center">

# lezione 1 - esercizio 6

</div>

- con utente utente1 eseguire il comando apt-get update
- con utente utente1 eseguire il comando sudo apt-get update
- rendere utente1 sudoer
- riprovare passi 1 e 2

provando a eseguire i comandi
```bash
apt-get update
```
e
```bash
sudo apt-get update
```
con utente utente1 il terminale ci comunicherà che non solo non disoniamo dei permessi necessari, ma che neanche utente1 sia nel file degli utenti *sudoers*.

Dopo aver aggiunto utente uno al gruppo dei sudoers tramite il comando

```bash
sudo adduser utente1 sudo
```

eseguendo nuovamente il comando
```bash
apt-get update
```
che non abbiamo comunque i privilegi abbastanza elevati per poter eseguire l'operazione, mentre invece con il comando sudo all'inizio
```bash
sudo apt-get update
```
verra eseguito normalmente
