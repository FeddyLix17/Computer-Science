<div align="center">

# lezione 1 - esercizio 5

</div>

- Studiare la sinossi del comando adduser
- creare 2 nuovi utenti (utente1 e utente2)
- con utente principale (sudoer) eseguire il comando apt-get update
- con utente principale eseguire il comando sudo apt-get update

Per creare i 2 nuovi utenti verranno eseguiti i comandi

```bash
sudo adduser utente1
sudo adduser utente2
```

eseguendo il comando
```bash
apt-get update
```
con l'utente principle il terminale ci comunicherà che non abbiamo i privilegi abbastanza elevati per poter eseguire l'operazione.

Eseguendolo invece con il comando sudo all'inizio
```bash
sudo apt-get update
```
verra eseguito normalmente
