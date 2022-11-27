import images
import time
start_img = "./data/input_00.png"
position = [12, 13]
commands = "S W S W W W S W W N N W N N N N N W N"
out_img = "./output/output_end_00.png"


def draw_pixel(img, x, y, colore):
    L, A = len(img[0]), len(img)
    if 0 <= x < L and 0 <= y < A:
        x = int(round(x))
        y = int(round(y))
        img[y][x] = colore


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    img, commands, snakelen, nextmove, all_positions = images.load(start_img), commands.split(), 1, 0, [position]
    moveset = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1)}
    draw_pixel(img, position[0], position[1], (128, 128, 128))
    command = commands[nextmove]
    print(len(commands))
    position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
    nextmove += 1
    all_positions.append(position)
    while nextmove < len(commands) and img[position[1]][position[0]] != (0, 255, 0) and img[position[1]][position[0]] != (255, 0, 0): 
        #time.sleep(0.1)
        #input()
        command = commands[nextmove]
        draw_pixel(img, all_positions[-snakelen - 1][0], all_positions[-snakelen - 1][1], (128, 128, 128))
        draw_pixel(img, position[0], position[1], (0, 255, 0))
        position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
        if position[0] < 0:
            position[0] = len(img[0]) - 1
        elif position[0] >= len(img[0]):
            position[0] = 0
        if position[1] < 0:
            position[1] = len(img) - 1
        elif position[1] >= len(img):
            position[1] = 0
        if img[position[1]][position[0]] == (255, 128, 0):
            snakelen += 1
        all_positions.append(position)
        images.save(img, out_img)
        nextmove += 1
    draw_pixel(img, position[0], position[1], (0, 255, 0))
    images.save(img, out_img)
    print(len(all_positions))
    return snakelen

generate_snake(start_img, position, commands, out_img)