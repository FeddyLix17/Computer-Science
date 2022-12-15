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
  if player == "B":
    other_player = "W"
  else:
    other_player = "B"
  if not any("." in row for row in board):
    if sum(row.count("B") for row in board) > sum(row.count("W") for row in board):
      a += 1
    elif sum(row.count("B") for row in board) < sum(row.count("W") for row in board):
      b += 1
    else:
      c += 1
    return a, b, c
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] == ".":
        if any(board[row][col + 1] == other_player for col in range(col + 1, len(board[0])) if 0 <= col + 1 < len(board[0])):
          for col in range(col + 1, len(board[0])):
            if board[row][col] == other_player:
              board[row][col] = player
            else:
              break
        if any(board[row][col - 1] == other_player for col in range(col - 1, -1, -1) if 0 <= col - 1 < len(board[0])):
          for col in range(col - 1, -1, -1):
            if board[row][col] == other_player:
              board[row][col] = player
            else:
              break
        if any(board[row + 1][col] == other_player for row in range(row + 1, len(board)) if 0 <= row + 1 < len(board)):
          for row in range(row + 1, len(board)):
            if board[row][col] == other_player:
              board[row][col] = player
            else:
              break
        if any(board[row - 1][col] == other_player for row in range(row - 1, -1, -1) if 0 <= row - 1 < len(board)):
          for row in range(row - 1, -1, -1):
            if board[row][col] == other_player:
              board[row][col] = player
            else:
              break
        if any(board[row + 1][col + 1] == other_player for row, col in zip(range(row + 1), range(col + 1, len(board[0]))) if 0 <= row + 1 < len(board) and 0 <= col + 1 < len(board[0])):
          for row, col in zip(range(row + 1), range(col + 1, len(board[0]))):
            if board[row][col] == other_player:
              board[row][col] = player
            else:
              break
def dumbothello(filename : str) -> tuple[int,int,int] :
  with open(filename, "r") as f:
    board = [line.strip().split() for line in f]
  return dumbothello_rec(board, "B", 0, 0, 0)
if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
