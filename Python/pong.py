from ursina import *

app = Ursina()
window.color = rgb(38, 43, 42)

camera.position = (0, 10, -60)
camera.rotation_x = 10

playfield = Entity(
    model = "cube",
    color = rgb(219, 241, 255)
    scale = (20, .5, 30)
    position = (0, 0, 0)
    texture = "assets/ice"
)

left_wall = Entity(
    parent = playfield,
    model = "cube",
    position = (0, .5, -.49),
    scale = (1, .7, .02),
    collider = "box",
    texture = "assets/rinkwall"
)

right_wall = duplicate(left_wall, position =(0, .5, .49))

walls = []
walls.append(left_wall)
walls.append(right_wall)

paddles = []
paddle1 = Entity(
    model = "cube",
    parent = playfield,
    position = (-.45, 1, 0),
    scale = (.05, .8, .2),
    texture = "assets/ice",
    color = rgb(100, 120, 200),
    collider = "box"
)

paddle2 = duplicate(paddle1, position(.45, 1, 0))
paddles.append(paddle1)
paddles.append(paddle2)

puck = Entity(
    model = "assets/Pumpkin.obj",
    color = color.white,
    scale = 1, 
    position = (0, .2, 0),
    collider = "box",
    texture = "assets/Pumpkin_Color"
)

speed = .005
ps_x = 5
ps_z = 5
p1_score = 0
p2_score = 0

def score():
    puck.x = 0
    puck.z = 0
    Audio("assets/audio/score")
    print_on_screen(
        text = f"Total Score = {p1_score} to {p2_score}",
        position = (-.6, .4, 0),
        duration = 2.5,
        scale = 1.5
    )

def update():
    global speed, ps_x, ps_z, p1_score, p2_score

    if paddle1.z > .4:
        paddle1.z = .05
    elif paddle1.z < -.4:
        paddle1.z += .05
    else:
        paddle1.z += speed * held_keys["w"]
        paddle1.z -= speed * held_keys ["s"]

    if paddle2.z > .4:
        paddle2.z = .05
    elif paddle2.z < -.4:
        paddle2.z += .05
    else:
        paddle2.z += speed * held_keys["w"]
        paddle2.z -= speed * held_keys["s"]
    
    puck.x += time.dt * ps_x
    puck.z += time.dt * ps_z

    hit_info = puck.intersects()
    if hit_info.hit:
        if hit_info.entity in paddles:
            ps_x *= -1
            Audio("assets/audio/impact")

        if hit_info.entity in walls:
            ps_z *= -1
            Audio("assets/audio/impact")

    if puck.x >= 10.5:
        p1_score += 1
        score()
        print_on_screen(
            text = "Player 1 Scores!",
            position = (-.1, .15, 0)
        )
    
    if puck.x <= -10.5:
        p2_score += 1
        score()
        print_on_screen(
            text = "Player 2 Scores!",
            position = (-.1, .15, 0)
        )

app.run()