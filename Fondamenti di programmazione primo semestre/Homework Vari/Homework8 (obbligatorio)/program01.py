#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Othello, o Reversi (https://en.wikipedia.org/wiki/Reversi), è un gioco da tavolo
giocato da due giocatori su una scacchiera 8x8. Pur avendo regole
relativamente semplici, Othello è un gioco di notevole profondità strategica.
In questo esercizio bisognerà simulare una versione semplificata di othello,
chiamata Dumbothello, in cui un giocatore cattura le pedine dell'avversario in
prossimità della propria pedina appena giocata.
Ecco le regole di Dumbothello:
- ogni giocatore ha un colore associato: bianco, nero;
- il giocatore con il nero è sempre il primo a giocare;
- a turno, ogni giocatore deve mettere una pedina del suo colore in modo tale
  da catturare una o più pedine avversarie;
- catturare una o più pedine avversarie vuol dire che la pedina giocata dal
  giocatore trasforma nel colore del giocatore tutte le pedine avversarie
  direttamente adiacenti, in una qualunque direzione orizzontale, verticale o diagonale;
- dopo aver giocato la propria pedina, le pedine avversarie catturate cambiano
  tutte colore e diventano dello stesso colore del giocatore che ha appena giocato;
- quando il giocatore di turno non può aggiungere ulteriori pedine in gioco,
  la partita termina. Vince il giocatore che ha più pedine sulla scacchiera
  oppure avviene un pareggio se il numero di pedine dei due giocatori è uguale;
- il giocatore di turno non può aggiungere ulteriori pedine se non ha modo di
  catturare nessuna pedina avversaria con nessuna mossa, oppure non ci sono
  più caselle libere sulla scacchiera.

Si deve scrivere una funzione dumbothello(filename) che legga da un file di testo
indicato dalla stringa filename una configurazione della scacchiera e,
seguendo le regole di Dumbothello, generi ricorsivamente l'albero di gioco completo
delle possibili evoluzioni della partita, in modo tale che ogni foglia dell'albero
sia una configurazione da cui non sia più possibile effettuare alcuna mossa.

La configurazione inziale della scacchiera nel file è rappresentata riga per
riga nel file. Una lettera "B" identifica una pedina del nero, una "W" una
pedina del bianco e il carattere "." una casella vuota. Le lettere sono
separate da uno o più caratteri di spaziatura.

In particolare, la funzione dumbothello restituirà una tripla (a, b, c), in cui:
- a è il numero totale di evoluzioni che terminano con una vittoria del nero;
- b è il numero totale di evoluzioni che terminano con una vittoria del bianco;
- c è il numero totale di evoluzioni che terminano con un pari.

Ad esempio, dato in input un file di testo contenente la scacchiera:
. . W W
. . B B
W W W B
W B B W

La funzione ritornerà la tripla:
(2, 16, 0)

ATTENZIONE: la funzione dumbothello o qualche altra 
funzione usata per la soluzione deve essere ricorsiva.

'''

def dumbothello_rec(board, player, a, b, c):
  # la funzione deve essere ricorsiva
  if player == "B":
    other = "W"
  else:
    other = "B"
  if not any("." in row for row in board):
    return a, b, c
  else:
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == ".":
          if i > 0 and board[i - 1][j] == other:
            for k in range(i - 1, -1, -1):
              if board[k][j] == player:
                board[i][j] = player
                board[k][j] = player
                a, b, c = dumbothello_rec(board, other, a, b, c)
                board[i][j] = "."
                board[k][j] = other
                break
              elif board[k][j] == ".":
                break
          if i < len(board) - 1 and board[i + 1][j] == other:
            for k in range(i + 1, len(board)):
              if board[k][j] == player:
                board[i][j] = player
                board[k][j] = player
                a, b, c = dumbothello_rec(board, other, a, b, c)
                board[i][j] = "."
                board[k][j] = other
                break
              elif board[k][j] == ".":
                break
          if j > 0 and board[i][j - 1] == other:
            for k in range(j - 1, -1, -1):
              if board[i][k] == player:
                board[i][j] = player
                board[i][k] = player
                a, b, c = dumbothello_rec(board, other, a, b, c)
                board[i][j] = "."
                board[i][k] = other
                break
              elif board[i][k] == ".":
                break
          if j < len(board[i]) - 1 and board[i][j + 1] == other:
            for k in range(j + 1, len(board[i])):
              if board[i][k] == player:
                board[i][j] = player
                board[i][k] = player
                a, b, c = dumbothello_rec(board, other, a, b, c)
                board[i][j] = "."
                board[i][k] = other
                break
              elif board[i][k] == ".":
                break
def dumbothello(filename : str) -> tuple[int,int,int] :
  with open(filename, "r") as f:
    board = [line.strip().split() for line in f]
  return dumbothello_rec(board, "B", 0, 0, 0)
if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
