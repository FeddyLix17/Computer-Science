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


def check_board(board, player, players):
  piecetoeat = 0
  otherpositionvalid = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == ".":
        for k in range(-1, 2):
          for l in range(-1, 2):
            if not check_position(board,i + k, j + l):
              continue
            if board[i + k][j + l] == players[player]:
              piecetoeat += 1
        if piecetoeat > 0:
          otherpositionvalid.append((i, j))
  return otherpositionvalid



def check_position(board, i, j):
  if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
    return False
  return True

def check_winner(board, a, b, c):
  b, w = 0, 0
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == "B":
        b += 1
      elif board[i][j] == "W":
        w += 1
  if b > w:
    a += 1
  elif b < w:
    b += 1
  else:
    c += 1
  return (a, b, c)

def place_disk(board, player, i, j):
  for k in range(-1, 2):
    for l in range(-1, 2):
      if not check_position(board,i + k, j + l):
        continue
      else:
        board[i + k][j + l] = player


def dumbothello_rec(board, player, a, b, c, players):
  if len(check_board(board, player, players)) == 0:
    if len(check_board(board, players[player], players)) == 0:
      return check_winner(board, a, b, c)
  else:
    allcurrentdots = check_board(board, player, players)
    while allcurrentdots:
      x = allcurrentdots.pop()
      print(f"player {player} plays {x}")
      recboard = board.copy()
      place_disk(recboard, player, x[0], x[1])
      dumbothello_rec(recboard, players[player], a, b, c, players)    
  return check_winner(recboard, a, b, c)



def dumbothello(filename : str) -> tuple[int,int,int] :
  filename, board, players = open(filename, "r"), [], {"B": "W", "W": "B"}
  for line in filename:
    board.append(line.split())
  filename.close()
  return (dumbothello_rec(board, "B", 0, 0, 0, players))




if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
