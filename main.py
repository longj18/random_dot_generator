import turtle as t
import random
import colorgram

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.ht()
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#         tim.color(random.choice(color))
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)

# tim.pensize(10)
# random_direction = [0, 90, 180, 270]
# def random_walk():
#     for i in range(200):
#         tim.color(random_color())
#         tim.forward(30)
#         tim.seth(random.randint(0, 360))
# random_walk()

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.seth(tim.heading() + size_of_gap)
# draw_spirograph(10)

###### DRAWING A COLORGRAM ###########

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_tuple = (red, green, blue)
#     rgb_colors.append(color_tuple)
# print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.penup()

def random_color():
    random_selection = random.randint(0,27)
    r = color_list[random_selection][0]
    g = color_list[random_selection][1]
    b = color_list[random_selection][2]
    random_color = (r, g, b)
    return random_color

def make_dot():
    for dot in range(10):
        tim.dot(20, random_color())
        if dot < 9:
            tim.forward(50)

def change_position(pos):
    tim.setpos(-300, pos)

pos = -450
while pos <= 0:
    change_position(pos)
    make_dot()
    pos += 50

screen = t.Screen()
screen.exitonclick()

