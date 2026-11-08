import turtle as t 
import math as m
import random as r
import time

s = t.Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.tracer(0)

p=t.Turtle()
p.hideturtle()

def heart(a, scale):
    x = 16 * (m.sin(a) ** 3) * scale
    y = (
        12 * m.cos(a)
        - 5 * m.cos(2 * a)
        - 2 * m.cos(3 * a)
        - m.cos(4 * a)
    ) * scale
    return x, y

for i in range(10000):
    a = r.uniform(0,2 * m.pi)
    sc = r.uniform(0.5, 15.5)
    x, y = heart(a, sc)
    
    ang = m.atan2(y, x) + r.uniform(-0.5, 0.5)
    length = r.uniform(4, 14)
    
    p.pencolor(
        1.0,
        r.uniform(0.25, 0.55),
        r.uniform(0.65, 0.85)
    )
    p.width(r.uniform(0.5, 1.2))
    
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.goto(
    x + length * m.cos(ang), 
    y + length * m.sin(ang)
    )
    
    if i % 200 ==0:
        s.update()
        time.sleep(0.002)
        
for i in range(3500):
    a = r.uniform(0, 2 * m.pi)
    x, y = heart(a, 16.0)
    
    ang = m.atan2(y, x) + r.uniform(-0.35, 0.35)
    length = r.uniform(10,32)
    
    p.pencolor(
        1.0,
        r.uniform(0.45, 0.75),
        r.uniform(0.75, 0.95)
    )
    p.width(r.uniform(0.4, 0.9))
    
    p.penup()
    p.goto(
        x + r.uniform(-2, 2),
        y + r.uniform(-2, 2)
    )
    p.pendown()
    p.goto(
        x + length * m.cos(ang),
        y + length * m.sin(ang)
    )
    
    if i % 150 == 0:
        s.update()
        time.sleep(0.002)



message = "I love you Baby"
canvas = s.getcanvas()

start_a = 5.05
end_a = 7.52

points = []

for i in range(800):
    a = start_a + (end_a - start_a) * i / 799
    x, y = heart(a, 16)
    points.append((x, y))

distances = [0]

for i in range(1, len(points)):
    x1, y1 = points[i - 1]
    x2, y2 = points[i]

    distance = m.hypot(x2 - x1, y2 - y1)
    distances.append(distances[-1] + distance)

total_length = distances[-1]

for i, letter in enumerate(message):

    target = total_length * i / (len(message) - 1)

    index = min(
        range(len(distances)),
        key=lambda j: abs(distances[j] - target)
    )

    x, y = points[index]

    before = points[max(0, index - 1)]
    after = points[min(len(points) - 1, index + 1)]

    dx = after[0] - before[0]
    dy = after[1] - before[1]

    angle = m.degrees(m.atan2(dy, dx))

    angle = max(-60, min(60, angle))

    y += 65

    if letter != " ":
        canvas.create_text(
            x,
            -y,
            text=letter,
            fill="#FC62E7",
            font=("Arial", 19, "bold"),
            angle=angle
        )

    s.update()
    time.sleep(0.15)

s.update()
t.done()
