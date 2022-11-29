import images
import time
start_img = "./data/input_04.png"
position = [19, 35]
commands = "S S S S W W W W N N N N N N E E E E E E E N E S S S E E E E S E S E S E S E S E N N N N N N N E N E E N E N N E N E N E N E N E N N W N W N W N W W W N W N W N W N W W W N N N N E N N E N E E E E NE NE NE NE S NW SW NE NE S SE S E W S W N E NW SE S NW NW NE SE NE S S E SW W NE NE S W NW SE S S SE NE N SW SW NW NW S S N SE SW E SE SW NW NW SW SW NE W W N SE SW S S SW S SW S S S W S E N NW NW SW S NE S SW SE NE S NW W NE W N S S SW NE SW NE SW SW NE W SW SE E W N SW W NE SE SE S W SE NW NW N E NE SW NW SW W NE NW NW NE S N E NE NE N N E E S NW SW NW E NW NE S E SW N W NE S NW NE N N N N NW SW S SW NW SW SW W NW SW SW E SE W W W NE SE SE S E S SE E W NW SE NE S SW E NW NW S SE S N W NE NW SW S E S E S NW SW S E S NW N SW N W W NE E E N N E E S W NE SE NW E SW S SW N W S S NE NW SW NE NE N W S SE SE S SE S W N S N N NW NW NW S SE S S S SW E W NE NE NW SW W N NW W NW W S N N NE NE S S W SW S N E S NW SW N"
out_img = "./output/output_end_04.png"


def check_diagonal_cross(all_positions, position, nextmove, command, moveset, img):
    diagonals = {'NE': (-1, 1), 'NW': (-1, -1), 'SE': (-1, 1), 'SW': (-1, -1)}
    print(f"current command: {command}")
    if img[all_positions[-1][1] + diagonals[command][0]][all_positions[-1][0]] == (0, 255, 0) and img[all_positions[-1][1]][all_positions[-1][0] + diagonals[command][1]] == (0, 255, 0):
        img[position[1]][position[0]] = (0, 255, 0)
        return False
    return True


def check_bordeless(position, img):
    checked = 0
    if position[0] < 0:
        position[0] = len(img[0]) - 1
        checked = 1
    elif position[0] >= len(img[0]):
        position[0] = 0
        checked = 1
    if position[1] < 0:
        position[1] = len(img) - 1
        checked = 1
    elif position[1] >= len(img):
        position[1] = 0
        checked = 1
    return position, checked


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    img, commands, snakelen, nextmove, all_positions, supercheck = images.load(start_img), commands.split(), 1, 0, [position], 0
    moveset = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1)}
    diagonals = {'NE': (-1, 1), 'NW': (-1, -1), 'SE': (-1, 1), 'SW': (-1, -1)}
    img[position[1]][position[0]] = (128, 128, 128)
    command = commands[nextmove]
    position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
    nextmove += 1
    all_positions.append(position)
    while nextmove < len(commands) and img[position[1]][position[0]] != (0, 255, 0) and img[position[1]][position[0]] != (255, 0, 0):  
        #time.sleep(0.2)
        input()
        command = commands[nextmove]
        if command in diagonals.keys() and supercheck == 0:
            if not check_diagonal_cross(all_positions, position, nextmove, command, moveset, img): break
        img[all_positions[-snakelen - 1][1]][all_positions[-snakelen - 1][0]] = (128, 128, 128)
        img[position[1]][position[0]] = (0, 255, 0)
        position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
        position, supercheck = check_bordeless(position, img)
        if img[position[1]][position[0]] == (255, 128, 0): snakelen += 1
        all_positions.append(position)
        images.save(img, out_img)
        nextmove += 1
    if img[position[1]][position[0]] == (0, 0, 0):
        #    img[all_positions[-snakelen - 1][1]][all_positions[-snakelen - 1][0]] = (128, 128, 128)
        img[position[1]][position[0]] = (0, 255, 0)
        img[all_positions[-snakelen - 1][1] ][all_positions[-snakelen - 1][0]] = (128, 128, 128)
    images.save(img, out_img)
    return snakelen

print(generate_snake(start_img, position, commands, out_img))