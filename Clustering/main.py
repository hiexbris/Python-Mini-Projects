from PIL import Image
import numpy as np
import pygame
import math
import pandas as pd

img = Image.open('3.png')
img_array = np.array(img)

color = ['#007F73', '#4CCD99', '#FF204E', '#FFF455', '#FFC700', '#A0153E', '#5D0E41', '#00224D']

pygame.init()
screen = pygame.display.set_mode((640, 640))

pixel = np.zeros((64, 64))

for row in range(img_array.shape[0]):
    for col in range(img_array.shape[1]):
        if img_array[row, col][0] == 0:
            pixel[row, col] = 0
        else:
            pixel[row, col] = 1

core_cells = np.zeros((64, 64))
cluster_list = []
centroids = []


for row, col in np.ndindex(pixel.shape):
    if pixel[row, col] == 1:
        count_1 = np.sum(pixel[row-2:row+3, col-2:col+3]) - 1
        if count_1 >= 5:
            core_cells[row, col] = 1

for row, col in np.ndindex(core_cells.shape):
    if core_cells[row, col] == 1:
        count = np.sum(core_cells[row-2:row+3, col-2:col+3])-1
        if count >= 1:
            pass
        else:
            core_cells[row, col] = 0

core_cells_copy = core_cells.copy()


def cluster_initial(cluster_array, rows, cols):
    cluster_array[rows, cols] = 1
    for near_rows in range(rows-2, rows+3):
        for near_cols in range(cols-2, cols+3):
            try:
                if core_cells[near_rows, near_cols] == 1:
                    core_cells[near_rows, near_cols] = 0
                    cluster_initial(cluster_array, near_rows, near_cols)
            except IndexError:
                pass


def cluster_final(cluster_array):
    for rows, cols in np.ndindex(cluster_array.shape):
        if cluster_array[rows, cols] == 1 and core_cells_copy[rows, cols] == 1:
            for near_rows in range(rows-5, rows+6):
                for near_cols in range(cols-5, cols+6):
                    try:
                        if (near_cols == cols and near_rows == rows) or cluster_array[near_rows, near_cols] == 1:
                            pass
                        elif pixel[near_rows, near_cols] == 1:
                            cluster_array[near_rows, near_cols] = 1
                    except IndexError:
                        pass


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    squared_diff_x = (x2 - x1) ** 2
    squared_diff_y = (y2 - y1) ** 2
    dist = math.sqrt(squared_diff_x + squared_diff_y)

    return dist


k = -1
while True:
    k += 1
    for row, col in np.ndindex(core_cells.shape):
        if core_cells[row, col] == 1:
            cluster_temp = np.zeros((64, 64))
            cluster_list.append(cluster_temp)
            cluster_initial(cluster_list[k], row, col)
            break
    core_cells_unit = np.sum(core_cells)
    if core_cells_unit == 0:
        break

for i in range(0, len(cluster_list)):
    cluster_final(cluster_list[i])


for row, col in np.ndindex(core_cells.shape):
    if pixel[row, col] == 1:
        pygame.draw.rect(screen, (255, 255, 255), (col * 10, row * 10, 10, 10))
        for i in range(0, len(cluster_list)):
            if cluster_list[i][row, col] == 1:
                pygame.draw.rect(screen, color[i], (col*10, row*10, 10, 10))
                break
    else:
        pygame.draw.rect(screen, (0, 0, 0), (col*10, row*10, 10, 10))


for i in range(0, len(cluster_list)):
    xcor = 0
    ycor = 0
    units = np.sum(cluster_list[i])
    for row, col in np.ndindex(core_cells.shape):
        if cluster_list[i][row, col] == 1:
            xcor += col*10 + 5
            ycor += row*10 + 5
    centroids.append((xcor/units, ycor/units))

for centroid in centroids:
    pygame.draw.circle(screen, '#FF7ED4', centroid, 3)

centroid_dist = {}
for i in range(0, len(centroids)):
    for j in range(i+1, len(centroids)):
        centroid_dist[f"Cluster {i+1} and {j+1}"] = distance(centroids[i], centroids[j])


df = pd.DataFrame.from_dict(centroid_dist, orient='index', columns=['Distance'])
df = df.reset_index()
df.columns = ['Clusters', 'Distance']
print(df.to_string(justify='left'))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            print(f"Mouse click at: {int(mouse_pos[1]/10)}, {int(mouse_pos[0]/10)}")
            print(core_cells_copy[int(mouse_pos[1]/10), int(mouse_pos[0]/10)])
    pygame.display.flip()
