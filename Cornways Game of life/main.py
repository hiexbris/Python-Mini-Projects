import time
import pygame
import numpy as np
import math

"""Basically the game works on the principle that alive cells can have a value of 42
   or 66, as 7, 11 signifies resurrection and one signifies death by underpop while other for overpop
   also the calculation of neighbours is done by adding the value of neighbours, so for that we use a convert value 
   which changes value like 42, 66 to 1, for proper addition"""


# Choosing colors
hexagon_coords = {}
COLOR_BG = '#183D3D'
COLOR_GRID = '#93B1A6'
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = '#5C8374'

pygame.init()
pygame.display.set_caption("Conway's game of life")


def convert_array(array):
    converted_array = [[1 if value in (1, 42, 66) else 0 for value in row] for row in array]
    return np.array(converted_array)


def is_point_inside_hexagon(point, vertices):
    x, y = point
    n = len(vertices)
    inside = False

    for i in range(n):  # basically using an algorithm to check if two coordinates are within the vertices of hexagon
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        if y1 < y <= y2 or y2 < y <= y1:
            if x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
                inside = not inside

    return inside  # true or false value based on if the mouse is inside the hexagon or not


def check_neighbours(convert, row, col):
    global alive_1
    if row % 2 != 0:
        alive_1 = np.sum(convert[row - 1:row + 2, col:col + 2]) - convert[row, col] + convert[row, col - 1]  # formula to check neighbours (can show calc on paper)
    if row % 2 == 0:  # due to hexagon not being uniform we make a change for odd rows
        if col == 47:  # out of index problems
            alive_1 = np.sum(convert[row - 1:row + 2, col - 1:col + 1]) - convert[row, col]
        elif col != 48:
            alive_1 = np.sum(convert[row - 1:row + 2, col - 1:col + 1]) - convert[row, col] + convert[row, col + 1]

    return alive_1


def random_gen(cells):
    if ticks % 4 == 0:
        index = []
        for row, col in np.ndindex(cells.shape):
            if cells[row, col] not in (1, 42, 66):
                index.append((row, col))
        rows, cols = zip(*index)
        random_idx = np.random.choice(len(rows))
        random_row, random_col = rows[random_idx], cols[random_idx]
        cells[random_row, random_col] = 1


def hexagon(col, row, size):
    global hexagon_coords  # figures out the vertices of all hexagon (can show the calc on paper)
    if row % 2 == 0:
        x_cor = col*size*math.sin(math.radians(60))  # use the column of hexagon to find the xcor
    elif row % 2 != 0:
        x_cor = (size*math.sin(math.radians(60))/2) + col*size*math.sin(math.radians(60))  # due to hexagon not being uniform we make a change for odd rows
    y_cor = row*3*(size/4)  # uses row number to calc coordinates ( can show calc on paper)
    hexagon_vertices = [(x_cor, y_cor+(size/4)), (x_cor+((size/2)*math.sin(math.radians(60))), y_cor+(size/2)), (x_cor+(size*math.sin(math.radians(60))), y_cor+(size/4)), (x_cor+(size*math.sin(math.radians(60))), y_cor-(size/4)), (x_cor+((size/2)*math.sin(math.radians(60))), y_cor-(size/2)), (x_cor, y_cor-(size/4))]
    hexagon_coords[(row, col)] = hexagon_vertices
    return hexagon_vertices


def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))  # make updated_cells an array same size of cells, basically representing cells, but updating once all the changes are done, so the result of changes doesnt hinder the game rules
    convert = convert_array(cells)  # makes another array with all the alive cells value as 1 and dead cells value as 0

    #random_gen(cells)  # generate random cell if not a alive cell

    for row, col in np.ndindex(cells.shape):

        alive = check_neighbours(convert, row, col)
        if cells[row, col] == 42 or cells[row, col] == 1 or cells[row, col] == 66:  # if cell is alive change its color
            color = COLOR_ALIVE_NEXT
        else:
            color = COLOR_BG

        if cells[row, col] == 1 or cells[row, col] == 42 or cells[row, col] == 66:  # passing the alive cells
            if alive < 2 and cells[row, col] != 42:  # 42 signifies last death by under population
                updated_cells[row, col] = 7  # if cell die by under pop its value is set to 7
                if with_progress:
                    color = COLOR_DIE_NEXT  # changes color of dead cell
            elif alive > 3 and cells[row, col] != 66:  # same logic as above
                updated_cells[row, col] = 11  # 11 is chosen so 7, 11 multiples dont intersect atleast till the 6 gen
                if with_progress:
                    color = COLOR_DIE_NEXT
            else:
                updated_cells[row, col] = cells[row, col]  # if all the living conditons meet old value is passed to updated cells
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        elif cells[row, col] == 36 or cells[row, col] == 55:  # priority to resurrection
            pass
        else:
            if alive == 3:  # born logic
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        if cells[row, col] > 1 and cells[row, col] != 42 and cells[row, col] != 66:  # every gen if the value is multiple of 7 a 7 gets added to it, once it reaces 42 resurrection occurs, basically 7*6 = 42 which signfies 6 generation, same for 11
            if cells[row, col] % 11 == 0:  # 11 gets added
                updated_cells[row, col] = cells[row, col] + 11
            if cells[row, col] % 7 == 0:  # 7 gets added
                updated_cells[row, col] = cells[row, col] + 7

        pygame.draw.polygon(screen, color, hexagon(col, row, size))  # drawing hexagon cells
        pygame.draw.polygon(screen, COLOR_GRID, hexagon(col, row, size), 1)  # drawing borders of hexagons
    return updated_cells


ticks = 1


def main():
    global ticks
    set_value_mode = True
    size = 20
    # pygame.init() sets up the pygame
    pygame.init()
    # Makes the screen of pygame 850X710
    screen = pygame.display.set_mode((850, 710))

    # makes a array filled with 0 of 48x49
    cells = np.zeros((48, 49))
    # Here screen is an object so .fill type of functions can be used
    screen.fill(COLOR_GRID)
    update(screen, cells, size)

    # in pygame to make frames look clean all the updates are made on the backside then using the flip function it turns to the frontside
    pygame.display.flip()
    pygame.display.update()

    running = False

    while True: # keeps running to check for input as well as updating the screen
        if running:
            ticks += 1  # increase the ticks, could be used later as generation signifier
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:  # checks for spacebar input, this constanly runs due to the while loop
                    running = not running
                    update(screen, cells, size)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:  # check of LMB press
                mouse_pos = pygame.mouse.get_pos()  # get the coords of mouse
                for row, col in np.ndindex(cells.shape):  # runs a loop and checking if the above coordinates are in any of the hexagons
                    if is_point_inside_hexagon(mouse_pos, hexagon_coords[row, col]):
                        if cells[row, col] == 42 or cells[row, col] == 66 or cells[row, col] == 1:  # if the cells the mouse click was on, is alive we leave it alone, while if its a dead cell we alive it
                            pass
                        else:
                            cells[row, col] = 1
                        break
                update(screen, cells, size)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:  # continously updating the screen
            cells = update(screen, cells, size, with_progress=True)
            pygame.display.update()

        time.sleep(0.001) # makes the loop stop for a sec
        pygame.image.save(screen.copy(), f"{ticks}.png")


if __name__ == "__main__":
    main()

