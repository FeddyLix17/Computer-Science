#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_board(board, player, players):
  piecetoeat = 0
  allvalidposition = []
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
          allvalidposition.append((i, j))
          piecetoeat = 0
  return allvalidposition


def check_position(board, i, j):
  if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
    return False
  return True

def check_winner(board, wins):
  b, w = 0, 0
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == "B":
        b += 1
      if board[i][j] == "W":
        w += 1
  if b > w:
    wins[0] += 1
  if b < w:
    wins[1] += 1
  if b == w:
    wins[2] += 1

def place_disk(board, player, i, j, players, depth):
  for k in range(-1, 2):
    for l in range(-1, 2):
      if not check_position(board,i + k, j + l): continue
      elif board[i + k][j + l] == players[player]:
        board[i + k][j + l] = player
  board[i][j] = player


def dumbothello_rec(board, player, wins, players, allposiblemove, depth = 0):
  depth += 1
  if len(allposiblemove) == 0:
    check_winner(board, wins)
  else:
    for i in range(len(allposiblemove)):
      tempboard = []
      for j in board:
        tempboard.append(j.copy())
      place_disk(tempboard, player, allposiblemove[i][0], allposiblemove[i][1], players, depth)
      dumbothello_rec(tempboard, players[player], wins, players, check_board(tempboard, players[player], players), depth)

def dumbothello(filename : str) -> tuple[int,int,int] :
  textinsidethefile, players, board, depth = open(filename, "r"), {"B": "W", "W": "B"}, [], 0
  for line in textinsidethefile: board.append(line.split())
  textinsidethefile.close()
  allposiblemove = check_board(board, "B", players)
  wins = [0, 0, 0]
  dumbothello_rec(board, "B", wins, players, allposiblemove, depth,)
  return tuple(wins)
