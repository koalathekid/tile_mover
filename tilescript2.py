import maya.cmds as cmd
import maya.api.OpenMaya as om
import math
import time
mesh_list = cmd.ls(type="transform")
mesh_list.remove('persp')
mesh_list.remove('side')
mesh_list.remove('top')
mesh_list.remove('front')
mesh_list.remove('pCube11')

print(mesh_list)

def compare(item):
    a = cmd.objectCenter(item)
    return a[0]

mesh_list.sort(key=compare)

max_z = math.ceil(cmd.objectCenter(mesh_list[-1])[0])
min_z = math.ceil(cmd.objectCenter(mesh_list[0])[0])

print("max z", max_z)
print("min z", min_z)

starting_value = min_z
block_size = 10
sweep_line_increment = math.fabs((max_z - min_z)/ 10.0)
#while len(mesh_list) > 0:

for this_mesh in mesh_list:
    cmd.setKeyframe(this_mesh)
rotate_list = []
how_much_to_rotate = 25
time_increment = 10
while rotate_list or mesh_list:
    current_time = cmd.currentTime(query=True ) 
    print("current time", current_time)
    cmd.currentTime(current_time + time_increment)
    for item in mesh_list:
        #Get the z component of a mesh
        z_value = cmd.objectCenter(item)[0]
        if (starting_value >= z_value):
            rotate_list.append(item)
            mesh_list.remove(item)
            #print("using", item, z_value)
        else:
            break  
    #print("rotate list", rotate_list)
    
    for this_mesh in rotate_list:
        
        obj1 = cmd.xform(this_mesh, ws=1, q=1, ro=1)
        z_rotation = obj1[2]
        print("rotation of",this_mesh, obj1)
        next_rotation = how_much_to_rotate + z_rotation
        if next_rotation >= 180:
            cmd.rotate(0,0,180 - z_rotation, this_mesh, relative=True, componentSpace=True)
            cmd.select(this_mesh, visible=True )
            cmd.setKeyframe(this_mesh)
            rotate_list.remove(this_mesh)
            obj2 = cmd.xform(this_mesh, ws=1, q=1, ro=1)
            print("Removing",this_mesh, obj2)
        else:
            cmd.rotate(0,0,how_much_to_rotate, this_mesh, relative=True, componentSpace=True)
            cmd.select(this_mesh, visible=True )
            cmd.setKeyframe(this_mesh)
        
        
    time.sleep(.3)
    starting_value += sweep_line_increment   
    #print("starting value", starting_value)
    
"""
current_rotate = 10
tiles_num = len(mesh_list)
curr_tile = 1
rotate_mesh_list = []
rotate_mesh_list.append(mesh_list.pop())
how_much_to_rotate = 25
time_increment = 10
curr_time = time_increment
print('before for loop')


def max_rotate(object_name, how_much_to_rotate):
    # Get the transform matrix as a list of 16 floats
    m_list = cmd.xform(object_name, query=True, matrix=True)
    # Create the MMatrix object
    m = om.MMatrix(m_list)
    # Get the MTransformationMatrix
    mt = om.MTransformationMatrix(m)
    # Get the rotations
    rot = mt.rotation()
    # Rotations in radians (as if rotated in the xyz order):
    #print (rot.x, rot.y, rot.z)
    #print (om.MAngle(rot.x).asDegrees(), om.MAngle(rot.y).asDegrees(), om.MAngle(rot.z).asDegrees())
    rotation_z = om.MAngle(rot.z).asDegrees() + how_much_to_rotate
    if (rotation_z > 180):
        print('rotation_z', rotation_z)
        print('output', rotation_z - 180)
        return rotation_z - 180
    elif (rotation_z < -180):        
        print('rotation_z', rotation_z)
        print('output', rotation_z + 180)
        return rotation_z + 180
    else:
        print('rotation_z_else', rotation_z)
        return how_much_to_rotate
while current_rotate < 180 or curr_tile is not tiles_num:
    #print('inside for loop')
    #print(current_rotate)
    #print(curr_tile)
    current_time = cmd.currentTime( query=True )  
    if current_rotate >= 180:
        current_rotate = 0
        rotate_mesh_list.pop()
        new_mesh = mesh_list.pop()
        time_setup = current_time - 1
        cmd.setKeyframe(new_mesh, time=time_setup)
        rotate_mesh_list.append(new_mesh)

    #print("current time",current_time)
    for this_mesh in rotate_mesh_list:
        x = 5
        print(this_mesh)
        cmd.rotate(0,0,max_rotate(this_mesh, how_much_to_rotate), this_mesh, relative=True, componentSpace=True)
        cmd.select(this_mesh, visible=True )
        cmd.setKeyframe(this_mesh)
        time.sleep(0.1)
    current_rotate += how_much_to_rotate
    current_rotate = min([current_rotate, 180])
    if (current_rotate >= 180):
        curr_tile += 1
    curr_time += time_increment
   
    cmd.currentTime(current_time + time_increment)
    
"""