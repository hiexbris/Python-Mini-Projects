import tkinter as tk
from math import cos, sin, radians

window = tk.Tk()

canvas = tk.Canvas(window, width=800, height=600, bg='black')
canvas.pack()

length = 100


def get_cube_vertices(length, base_x=400, base_y=300, base_z=0):

    vertices = [
      (base_x, base_y, base_z),
      (base_x + length, base_y, base_z),
      (base_x + length, base_y + length, base_z),
      (base_x, base_y + length, base_z),
      (base_x, base_y, base_z + length),
      (base_x + length, base_y, base_z + length),
      (base_x + length, base_y + length, base_z + length),
      (base_x, base_y + length, base_z + length),
    ]

    return vertices


vertices = get_cube_vertices(length)


def create_triangle(x1, y1, x2, y2, x3, y3):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='white')


def create_square_2():

    create_triangle(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], vertices[3][0], vertices[3][1])
    create_triangle(vertices[2][0], vertices[2][1], vertices[1][0], vertices[1][1], vertices[3][0], vertices[3][1])
    create_triangle(vertices[2][0], vertices[2][1], vertices[1][0], vertices[1][1], vertices[6][0], vertices[6][1])
    create_triangle(vertices[5][0], vertices[5][1], vertices[1][0], vertices[1][1], vertices[6][0], vertices[6][1])
    create_triangle(vertices[4][0], vertices[4][1], vertices[7][0], vertices[7][1], vertices[3][0], vertices[3][1])
    create_triangle(vertices[0][0], vertices[0][1], vertices[3][0], vertices[3][1], vertices[4][0], vertices[4][1])
    create_triangle(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], vertices[4][0], vertices[4][1])
    create_triangle(vertices[5][0], vertices[5][1], vertices[1][0], vertices[1][1], vertices[4][0], vertices[4][1])
    create_triangle(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], vertices[3][0], vertices[3][1])
    create_triangle(vertices[7][0], vertices[7][1], vertices[6][0], vertices[6][1], vertices[4][0], vertices[4][1])
    create_triangle(vertices[5][0], vertices[5][1], vertices[6][0], vertices[6][1], vertices[4][0], vertices[4][1])
    create_triangle(vertices[7][0], vertices[7][1], vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1])
    create_triangle(vertices[7][0], vertices[7][1], vertices[6][0], vertices[6][1], vertices[2][0], vertices[2][1])
    # canvas.create_line(vertices[1][0], vertices[1][1], vertices[3][0], vertices[3][1], fill="white", width=2)
    # canvas.create_line(vertices[1][0], vertices[1][1], vertices[6][0], vertices[6][1], fill="white", width=2)
    # canvas.create_line(vertices[4][0], vertices[4][1], vertices[3][0], vertices[3][1], fill="white", width=2)
    # canvas.create_line(vertices[1][0], vertices[1][1], vertices[4][0], vertices[4][1], fill="white", width=2)
    # canvas.create_line(vertices[4][0], vertices[4][1], vertices[6][0], vertices[6][1], fill="white", width=2)
    # canvas.create_line(vertices[7][0], vertices[7][1], vertices[2][0], vertices[2][1], fill="white", width=2)



def create_square_1():
    line_width = 2  # Adjust line thickness
    canvas.create_line(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], fill="white", width=line_width)
    canvas.create_line(vertices[0][0], vertices[0][1], vertices[3][0], vertices[3][1], fill="white", width=line_width)
    canvas.create_line(vertices[0][0], vertices[0][1], vertices[4][0], vertices[4][1], fill="white", width=line_width)
    canvas.create_line(vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1], fill="white", width=line_width)
    canvas.create_line(vertices[1][0], vertices[1][1], vertices[5][0], vertices[5][1], fill="white", width=line_width)
    canvas.create_line(vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1], fill="white", width=line_width)
    canvas.create_line(vertices[2][0], vertices[2][1], vertices[6][0], vertices[6][1], fill="white", width=line_width)
    canvas.create_line(vertices[3][0], vertices[3][1], vertices[7][0], vertices[7][1], fill="white", width=line_width)
    canvas.create_line(vertices[7][0], vertices[7][1], vertices[6][0], vertices[6][1], fill="white", width=line_width)
    canvas.create_line(vertices[7][0], vertices[7][1], vertices[4][0], vertices[4][1], fill="white", width=line_width)
    canvas.create_line(vertices[4][0], vertices[4][1], vertices[5][0], vertices[5][1], fill="white", width=line_width)
    canvas.create_line(vertices[5][0], vertices[5][1], vertices[6][0], vertices[6][1], fill="white", width=line_width)


def get_rotated_x(h):
    for index in range(0, len(vertices)):
        vertices[index] = (vertices[index][0], vertices[index][1]*cos(h)+vertices[index][2]*sin(h), -vertices[index][1]*sin(h)+vertices[index][2]*cos(h))


def get_rotated_y(h):
    for index in range(0, len(vertices)):
        vertices[index] = (vertices[index][0]*cos(h)-vertices[index][2]*sin(h), vertices[index][1], vertices[index][0]*sin(h)+vertices[index][2]*cos(h))


def get_rotated_z(h):
    for index in range(0, len(vertices)):
        vertices[index] = (vertices[index][0]*cos(h)+vertices[index][1]*sin(h), vertices[index][1]*cos(h)-vertices[index][0]*sin(h), vertices[index][2])


get_rotated_x(radians(30))
get_rotated_y(radians(45))
get_rotated_y(radians(0))
create_square_2()


window.mainloop()
