import images
import time
start_img = "./data/input_08.png"
position = [2, 18]
commands = "S S E E S E S E S S E E E E E E E N W W W W N W N W N N E E E E N W N N E N E N N N E E S E S E E E E E N W N E E E E E E N N W N W W W N N E E E N W N E E E E S S S S E S S S S S S W W W S S E S S S E N N N N E E N N N N N N N N E E S S W S S S S S S E E E E N N N N E N N E E N E E E S S S S E E S W S S E E E N N E S S S W S S E S S E S S S S S S W W W S W W N W W N W S S S S S S S E E S S S E S S S S S S S S W S S W N N W S S S S S S S S S W W W W W S S S S W S S E E E E S S W W S W S W S W S W S W S W S S S E S S S S S E S S S W S S E E N E N N E S S S S S W S W S W W S W S S S S E S W S E E S S S S E E E S S S W W W W W W W W W W N N N E N N N N N N N N N N N N W W W W W W S S S W W N N N N N N E S E E N N N N N N N W W N E E E E E N N N W W N W N W N W N W N N N N N W NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NE NE NE NE N N N N N N N N N N N NW NW NW NW NW NW NW NW W W W S W S W SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW SW W W N N E E N N E N N E N N N N E S E N N E N N E SE N SW N N E N N N N E S E N N E N N E SE N SW"
out_img = "./output/output_end_08.png"


def check_diagonal_cross(all_positions, command, img, snakelen):
    diagonals = {'NE': (-1, 1), 'NW': (-1, -1), 'SE': (-1, 1), 'SW': (-1, -1)}
    if img[all_positions[-1][1] + diagonals[command][0]][all_positions[-1][0]] == (0, 255, 0) and img[all_positions[-1][1]][all_positions[-1][0] + diagonals[command][1]] == (0, 255, 0):
        #img[all_positions[-snakelen - 1][1]][all_positions[-snakelen - 1][0]] = (0, 255, 0)
        #img[all_positions[-1][1]][all_positions[-1][0]] = (0, 0, 0)
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
    img, commands, snakelen, nextmove, all_positions, supercheck = images.load(
        start_img), commands.split(), 1, 0, [position], 0
    moveset = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),
               'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1)}
    diagonals = {'NE': (-1, 1), 'NW': (-1, -1), 'SE': (-1, 1), 'SW': (-1, -1)}
    img[position[1]][position[0]] = (128, 128, 128)
    command = commands[nextmove]
    position = [position[0] + moveset[command]
                [0], position[1] + moveset[command][1]]
    nextmove += 1
    all_positions.append(position)
    while nextmove < len(commands) and img[position[1]][position[0]] != (0, 255, 0) and img[position[1]][position[0]] != (255, 0, 0):
        time.sleep(0.05)
        input()
        
        if img[all_positions[-1][1]][all_positions[-1][0]] == (255, 128, 0):
            img[all_positions[-snakelen - 1][1]
                ][all_positions[-snakelen - 1][0]] = (0, 255, 0)
            img[all_positions[-1][1]][all_positions[-1][0]] = (0, 255, 0)
            snakelen += 1
        else:
            img[all_positions[-snakelen - 1][1]
                ][all_positions[-snakelen - 1][0]] = (128, 128, 128)
            img[all_positions[-1][1]][all_positions[-1][0]] = (0, 255, 0)
        command = commands[nextmove]
        position = [position[0] + moveset[command]
                    [0], position[1] + moveset[command][1]]
        position, supercheck = check_bordeless(position, img)
        if command in diagonals.keys() and supercheck == 0:
            if not check_diagonal_cross(all_positions, command, img, snakelen):
                break
        all_positions.append(position)
        print(commands[nextmove:])
        images.save(img, out_img)
        nextmove += 1
    if img[all_positions[-1][1]][all_positions[-1][0]] == (255, 128, 0):
        snakelen += 1
    if nextmove == len(commands):
        img[all_positions[-snakelen - 1][1]
            ][all_positions[-snakelen - 1][0]] = (128, 128, 128)
        img[all_positions[-1][1]][all_positions[-1][0]] = (0, 255, 0)
    else:
        print(command)
    images.save(img, out_img)
    return snakelen


print(generate_snake(start_img, position, commands, out_img))