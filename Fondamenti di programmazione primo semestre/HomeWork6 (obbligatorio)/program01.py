#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Siete stati appena ingaggiati in una software house di videogiochi e
dovete renderizzare su immagine il giochino dello snake salvando
l'immagine finale del percorso dello snake e restituendo la lunghezza
dello snake.
Si implementi la funzione generate_snake che prende in ingresso un
percorso di un file immagine, che e' l'immagine di partenza
"start_img" che puo' contenere pixel di background neri, pixel di
ostacolo per lo snake di colore rosso e infine del cibo di colore
arancione. Lo snake deve essere disegnato di verde. Inoltre bisogna
disegnare in grigio la scia che lo snake lascia sul proprio
cammino. La funzione inoltre prende in ingresso una posizione iniziale
dello snake, "position" come una lista di due interi X e Y. I comandi
del giocatore su come muovere lo snake nel videogioco sono disponibili
in una stringa "commands".  La funzione deve salvare l'immagine finale
del cammino dello snake al percorso "out_img", che e' passato come
ultimo argomento di ingresso alla funzione. Inoltre la funzione deve
restituire la lunghezza dello snake al termine del gioco.

Ciascun comando in "commands" corrisponde ad un segno cardinale ed e
seguito da uno spazio. I segni cardinali possibli sono:

| NW | N | NE |
| W  |   | E  |
| SW | S | SE |

che corrispondono a movimenti dello snake di un pixel come:

| alto-sinistra  | alto  | alto-destra  |
| sinistra       |       | destra       |
| basso-sinistra | basso | basso-destra |

Lo snake si muove in base ai comandi passati e nel caso in cui
mangia del cibo si allunga di un pixel.

Lo snake puo' passare da parte a parte dell'immagine sia in
orizzontale che in verticale. Il gioco termina quando sono finiti i
comandi oppure lo snake muore. Lo snake muore quando:
- colpisce un ostacolo
- colpisce se stesso quindi non puo' passare sopra se stesso
- si incrocia in diagonale in qualsiasi modo. Ad esempio, un percorso
  1->2->3-4 come quello sotto a sinistra non e' lecito mentre quello a
  destra sotto va bene.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

Ad esempio considerando il caso di test data/input_00.json
lo snake parte da "position": [12, 13] e riceve i comandi
 "commands": "S W S W W W S W W N N W N N N N N W N" 
genera l'immagine in visibile in data/expected_end_00.png
e restituisce 5 in quanto lo snake e' lungo 5 pixels alla
fine del gioco.

NOTA: analizzate le immagini per avere i valori esatti dei colore da usare.

NOTA: non importate o usate altre librerie
'''


import images


def draw_pixel(img, x, y, colore):
    L, A = len(img[0]), len(img)
    if 0 <= x < L and 0 <= y < A:
        x = int(round(x))
        y = int(round(y))
        img[y][x] = colore


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    img, commands, snakelen, nextmove = images.load(start_img), commands.split(), 1, 0
    all_positions = [position]
    moveset = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0), 'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1)}
    #draw_pixel(img, position[0], position[1], (128, 128, 128))
    #command = commands[nextmove]
    #position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
    #all_positions.append(position)
    #nextmove += 1
    while nextmove < len(commands) and img[position[1]][position[0]] != (255, 0, 0):
        #nextmove += 1
        command = commands[nextmove]
        #input('Press enter to continue')
        #images.save(img, out_img)
        #position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
        if img[position[1]][position[0]] == (255, 128, 0): snakelen += 1
        draw_pixel(img, position[0], position[1], (128, 128, 128))
        all_positions.append(position)
        position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
        nextmove += 1
    nextmove = len(all_positions) - snakelen
    while nextmove < len(all_positions):
        draw_pixel(img, all_positions[nextmove][0], all_positions[nextmove][1], (0, 255, 0))
        nextmove += 1
    images.save(img, out_img)
    return snakelen
