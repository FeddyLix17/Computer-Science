#Vari Valori colori
# con valori tra 0 e 255 compresi (1 byte)
# definiamo qualche colore
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
grey = 128, 128, 128

# Creazione di una immagine/matrice monocolore nel modo sbagliato
import images
def crea_immagine_errata(larghezza, altezza, colore):
    riga = [ colore ] * larghezza
    img = [ riga ] * altezza
    return img
img2 = crea_immagine_errata(30, 40, blue)

img2[5][7] = red # Coloro un solo pixel

images.visd(img2) # e trovo una colonna rossa invece di un solo pixel!!!
## LAVAGNA!

# Creazione di una immagine/matrice monocolore nel modo corretto
# crea_immagine ritorna un immagine monocolore nera
def crea_immagine(larghezza, altezza, colore=black):
    return [ [ colore ] * larghezza for i in range(altezza) ]
# mentre crea_imm crea un'immagine monocolore in base al parametro passatogli
def crea_imm(L,H,C):
    img = []
    for y in range(H):
        riga = []
        for x in range(L):
            riga.append(C) 
        img.append(riga)
    return img
img = crea_imm(30, 40, red)
img5 = crea_immagine(50, 50, black)
#test di prova per salvare immagini
images.save(img5, "sfondoNero.png")
img[5][7] = blue # coloro un pixel
images.visd(img)

# come salvare un file png sul disco
# Pixel = tuple[int,int,int]
# Line = list[Pixel]
# Picture = list[Line]
# images.load(filename : str) -> Picture
img3 = images.load('img1.png')
print(len(img3), len(img3[0])) # altezza e larghezza
img3[40][30:250] = [red]*220 # coloriamo una fila di pixel
# images.save(img : Picture, filename : str) -> None
images.save(img3, 'img1-2.png')
images.visd(img3)


# Disegnare un pixel senza generare errori se le coordinate sono fuori dall'immagine
# --- controllando le posizioni
def draw_pixel(img, x, y, colore):
    # ricavo l'altezza e larghezza dell'immagine
    L,A = len(img[0]), len(img)
    # cambio il pixel solo se dentro l'immagine
    if 0 <= x < L and 0 <= y < A:
        x = int(round(x))
        y = int(round(y))
        img[y][x] = colore
draw_pixel(img3, 100, 150, red)
images.visd(img3)

# usando try-except per catturare l'errore
def draw_pixel(img, x, y, colore): 
    # mi preparo a catturare l'errore (try)
    try:
        # disegno il pixel
        assert x >= 0 and y >= 0
        img[y][x] = colore
        # se c'è errore (except) lo ignoro
    except IndexError:
        pass
    except AssertionError:
        print('sbordato a sinistra o in alto')
        pass
# --- BEWARE of negative indexes!!! (che non producono errori)
# --- BEWARE of generic 'catch-all' except clauses!!!!! (che nascondono TROPPI errori)
draw_pixel(img3, -50, -50, red)
images.visd(img3)

# Rotazione dell'immagine di 90° a sinistra
# X_destinazione = y_sorgente
# Y_destinazione = larghezza_sorgente - 1 - x_sorgente
def ruota_sx(img):
    altezza = len(img)
    larghezza = len(img[0])
    # creo una immagine con altezza e larghezza scambiate
    img2 = crea_immagine(altezza, larghezza)
    # per ogni pixel della immagine originale
    for y, riga in enumerate(img):
        for x, pixel in enumerate(riga):
            # calcolo le coordinate della destinazione
            X = y
            Y = larghezza -1 -x
            # e copio il pixel
            img2[Y][X] = pixel
    # torno l'immagine ruotata
    return img2
img_r = ruota_sx(img3)
images.save(img_r, 'img1-rotatasium.png')
images.visd(img_r)
# --- PER CASA: rotazione destra
def ruota_dx(img):
    altezza = len(img)
    larghezza = len(img[0])
    # creo una immagine con altezza e larghezza scambiate
    img2 = crea_immagine(altezza, larghezza)
    # per ogni pixel della immagine originale
    for y, riga in enumerate(img):
        for x, pixel in enumerate(riga):
            # calcolo le coordinate della destinazione
            X = y
            Y = x 
            # e copio il pixel
            img2[Y][X] = pixel
    # torno l'immagine ruotata
    return img2


img_r = ruota_dx(img3)
images.save(img_r, 'img1-rotatasiumdestra.png')
images.visd(img_r)

# Disegnare una linea orizzontale o verticale
def draw_h_line(img, x, y, x2, colore):
    # scandisco le X da x a x2
    for X in range(x, x2+1):
        # riusiamo la draw_pixel che controlla di non sbordare
        draw_pixel(img, X, y, colore)
# oppure prima intersechiamo la linea con l'immagine e poi la disegnamo senza controlla
def draw_h_line2(img, x, y, x2, colore):
    larghezza = len(img[0])
    altezza = len(img) # se la y è tra 0 e altezza
    if 0 <= y < altezza:
        # la parte da disegnare ha estremi non maggiori di larghezza-1 e non minori di x, x2 = min(x,x2), max(x, x2)
        xmin = max(x, 0)
        xmax = min(x2, larghezza-1)
        # una volta aggiustati gli estremi la si disegna
        for X in range(xmin, xmax+1):
            img[y][X] = colore
img = images.load('img1.png')
draw_h_line2(img, 30, 100, 200, red)
images.visd(img)
# lo stesso per una linea verticale
def draw_v_line(img, x, y, y2, colore):
    larghezza = len(img[0])
    altezza = len(img)
        # la parte da disegnare ha estremi non maggiori di altezza-1 e non minori di 0
        # una volta aggiustati gli estremi la si disegna
    for Y in range(y, y2+1):
        # riusiamo la draw_pixel che controlla di non sbordare
        draw_pixel(img, x, Y, colore)


# --- e diagonale??? come???
# dipende dalla direzione
def draw_slope(img, x1, y1, x2, y2, colore):
    # FIXME: aggiungere i controlli sulle coordinate?
    dx = x2-x1
    dy = y2-y1 # si varia lungo la direzione più lunga
    # se |dx| > |dy| ci calcola la y per ciascuna x in [x1 .. x2]
    # FIXME: e se dx == 0 oppure dy == 0? disegnamo una retta verticale o orizzontale
    if dx == 0:
        draw_v_line(img, x1, y1, y2, colore) 
    elif dy == 0:
        draw_h_line(img, x1, y1, x2, colore) 
    elif abs(dx) >= abs(dy):
        # mi assicuro che x1<x2
        x1, x2 = min(x1, x2), max(x1, x2)
        # calcolo m=dy/dx
        m = dy/dx
        # e per ogni x in [x1 .. x2]
        for x in range(x1, x2+1):
            # calcolo y = mx+c con c=y1
            y = m * x + y1
            # e disegno il pixel (con draw_pixel?)
            draw_pixel(img, x, y, colore)
        # altrimenti per ciascuna y calcoliamo la x
        else:
            # semplicemente scambiando x e y nelle formule precedenti
            # mi assicuro che y1<y2
            y1, y2 = min(y1, y2), max(y1, y2)
            # calcolo m=dx/dy
            m = dx/dy
            # e per ogni x in [x1 .. x2]
            for y in range(y1, y2+1):
                # calcolo y = mx+c con c=y1
                x = m * y + x1
                # e disegno il pixel (con draw_pixel?)
                draw_pixel(img, x, y, colore)
draw_slope(img, 10,20, 100, 20, green)
images.visd(img)


# Disegnare un rettangolo vuoto
def draw_empty_rectangle(img,x1,y1,x2,y2,colore):
    # dobbiamo disegnare le 4 linee
    draw_h_line(img, x1, y1, x2, colore)
    draw_h_line(img, x1, y2, x2, colore)
    draw_v_line(img, x1, y1, y2, colore)
    draw_v_line(img, x2, y1, y2, colore)
def draw_empty_rectangle(img,x1,y1,x2,y2,colore):
    for x in range(x1, x2+1):
        draw_pixel(img, x, y1, colore)
        draw_pixel(img, x, y2, colore)
    # oppure disegnare i pixel orizzontali
    # e poi i verticali
    for y in range(y1, y2+1):
        draw_pixel(img, x1, y, colore)
        draw_pixel(img, x2, y, colore)
draw_empty_rectangle(img, 50, 50, 150, 150, yellow)
images.visd(img)


# Disegnare un rettangolo pieno
# questa è facile
def draw_rectangle(img, x1,y1, x2,y2, colore):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            draw_pixel(img, x,y, colore)
draw_rectangle(img, 30,50, 80, 120, purple)
images.visd(img)


# Disegnare un'ellisse
# disegnamo una ellisse PIENA
# --- con somma delle distanze dai fuochi <= D
from math import sqrt, dist
def draw_ellisse(img, x1, y1, x2, y2, D, colore):
    larghezza = len(img[0])
    altezza = len(img)
    # scandisco tutti i pixel della immagine
    for x in range(larghezza):
        for y in range(altezza):
            # per ciascuno calcolo le due distanze dai fuochi
            D1 = dist((x,y), (x1,y1))
            D2 = dist((x,y), (x2,y2)) # se la somma < D allora il pixel è DENTRO e lo coloro
            if D1+D2 < D:
                img[y][x] = colore
            # altrimenti lo ignoro
            # NOTA: non devo controllare se sono dentro l'immagine
            # perchè scandisco SOLO i pixel della immagine
# NOTA: D deve essere più grande della distanza tra i fuochi
# TODO: si possono scandire meno pixel
draw_ellisse(img, 50, 200, 90, 150, 100, cyan)
images.visd(img)


# Disegnare un'ellisse vuota
def draw_ellisse_vuota(img, x1, y1, x2, y2, D, colore):
    larghezza = len(img[0])
    altezza = len(img)
    # scandisco tutti i pixel della immagine
    for x in range(larghezza):
        for y in range(altezza):
            # per ciascuno calcolo le due distanze dai fuochi
            D1 = dist((x,y), (x1,y1))
            D2 = dist((x,y), (x2,y2)) # se la somma - D è piccola sono sul bordo
            if abs((D1+D2) - D) < 1 :
                img[y][x] = colore
            # altrimenti lo ignoro 
# D deve essere più grande della distanza tra i fuochi
draw_ellisse_vuota(img, 100, 100, 150, 150, 200, green)
images.visd(img)


# Disegnare un cerchio
# cerchio = ellisse con entrambi i fuochi nello stesso punto e somma delle distanze = 2 
# def draw_circle(img, x, y, r, colore): draw_ellisse(img, x, y, x, y, 2*r, colore)
def draw_circle_vuoto(img, x, y, r, colore): draw_ellisse_vuota(img, x, y, x, y, 2*r, colore)
draw_circle_vuoto(img, 150, 50, 30, red)
images.visd(img)