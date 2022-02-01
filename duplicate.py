import maya.cmds as cmd
import math
import random
convert_rad = math.pi / 180
iteration = 0

mesh_name = 'pCube1'
bounding = cmd.polyEvaluate([mesh_name], boundingBox=True)
x_s = bounding[0]
y_s = bounding[1]
z_s = bounding[2]
length = x_s[1] - x_s[0]
 
 
#Create Center
cyl_radius = 1.9 - x_s[1]
cmd.polyCylinder( sx=20, sy=15, sz=5, h=y_s[1]*2, r=cyl_radius)

#number of circles to create
for circle_iter in range(0, 10):
    iteration += 1
    radius = 1.9 + (circle_iter * length)
    circumference = 2 * math.pi * (radius - x_s[1])

    iterations = math.ceil(circumference / length) #+1
    angle_iter = 360 / iterations
    
    fuzzy_rotation = random.random()* 360
    curr_iter = 0
    while curr_iter != iterations:
    #for item in range(0,360,angle_iter):
        item = (fuzzy_rotation + angle_iter * curr_iter) % 360

        circle_iter
        new_item = cmd.duplicate(mesh_name)[0]
        y = math.sin((item)* convert_rad) * radius
        x = math.cos((item)* convert_rad) * radius
        cmds.move( x, 0, y, new_item ) 
        cmd.rotate(0, -item, 0, new_item)
        curr_iter += 1
        #print(item, new_item)
    #cmds.duplicate( st=True )
#cmds.duplicate( st=True )