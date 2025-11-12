import bpy
import bpy_extras
from mathutils import Matrix
from mathutils import Vector
import numpy


def SavePosesToNPZ(cam, filepath):
    print("running write_some_data...")
   
    scene = bpy.context.scene
    frame = scene.frame_start
    num_poses = scene.frame_end+1
    cam_poses = numpy.zeros((num_poses, 4, 4),dtype=numpy.float32)

    index=0
    
    while frame <= scene.frame_end:
        scene.frame_set(frame)
        cam_poses[index] +=cam.matrix_world
        frame += 1
        index += 1
        
    data_dict={'poses' : cam_poses}

    numpy.savez_compressed(filepath, **data_dict)
    print("Saved poses to npz file")




print("Start script")


def ExportPoses():
    print("ExportPoses() called")
    
    
    print("Camera pose export started...")
    # Insert your camera name here
    cam = bpy.data.objects['Camera']
 
    
    mw = cam.matrix_world
    scene = bpy.context.scene
    frame = scene.frame_start

    
    location, rotation = cam.matrix_world.decompose()[0:2]
    print("Camera pos:", location[0], location[1], location[2])
    
    #quaternion.  rotation[0]=w
    print("Camera quaternion:", rotation[0], rotation[1], rotation[2],  rotation[3])

    print("Camera matrix world",cam.matrix_world )
    
    
    # save all poses to npz
    filepath=".\\camera_poses.npz"
    SavePosesToNPZ(cam, filepath)
    
     # load the npz file
    loaded_data = numpy.load(filepath)
    loaded_poses = loaded_data['poses']
    print("Loaded poses", loaded_poses)
    print("Shape of poses tensor loaded:", loaded_poses.shape)
    
    return {'FINISHED'}
