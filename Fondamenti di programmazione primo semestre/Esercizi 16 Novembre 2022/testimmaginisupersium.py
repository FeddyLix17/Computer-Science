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


import images
def crea_immagine_errata(larghezza, altezza, colore):
    riga = [ colore ] * larghezza
    img = [ riga ] * altezza
    return img
img2 = crea_immagine_errata(30, 40, blue)
img2[5][7] = red # Coloro un solo pixel
images.visd(img2) # e trovo una colonna rossa!!!
## LAVAGNA!


def crea_immagine(larghezza, altezza, colore=black):
    return [ [ colore ]*larghezza
    for i in range(altezza)
    ]
def crea_imm(L,H,C):
    img = []
    for y in range(H):
        riga = []
        for x in range(L):
            riga.append(C) 
        img.append(riga)
    return img
img = crea_imm(30, 40, red)
img5 = crea_immagine(50, 50)
#images.save(img5, "sfondoNero.png")
img[5][7] = blue # coloro un pixel
images.visd(img)


# Pixel = tuple[int,int,int]
# Line = list[Pixel]
# Picture = list[Line]
# images.load(filename : str) -> Picture
img3 = images.load('sfondoNero.png')
print(len(img3), len(img3[0])) # altezza e larghezza
img3[40][30:250] = [red]*220 # coloriamo una fila di pixel
# images.save(img : Picture, filename : str) -> None
images.save(img3, 'img1-2.png')
images.visd(img3)


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


# --- usando try-except per catturare l'errore
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
images.visd(img_r)
# --- PER CASA: rotazione destra


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
img = images.load('3cime.png')
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