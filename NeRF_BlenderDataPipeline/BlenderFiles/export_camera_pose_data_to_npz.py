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




print("start script")


def ExportPoses():
    print("ExportPoses() called")
    
    
    print("Camera pose export started...")
    # Insert your camera name here
    cam = bpy.data.objects['Camera']
 
    
    mw = cam.matrix_world
    scene = bpy.context.scene
    frame = scene.frame_start

    """
    filepath="C:\\Users\\bflug\\Documents\\BlenderFilesByBill\\camera_data.txt"
    print("Filepath=" + filepath)
    
    f = open(filepath, 'w', encoding='utf-8')
    while frame <= scene.frame_end:
        print("Entered while loop")
        scene.frame_set(frame)
        x, y, z = mw.to_translation()
        rx, ry, rz = mw.to_euler('XYZ')
        f.write("%d" % frame)
        f.write(", ")
        f.write("%5.3f, %5.3f, %5.3f" % (x, y, z))
        f.write(", ")
        f.write("%5.3f, %5.3f, %5.3f" % (rx, ry, rz))
        f.write("\n")
        frame += 1
        print("wrote camera data")
    f.close()
    """

    """
    filepath="C:\\Users\\bflug\\Documents\\BlenderFilesByBill\\cam_world.txt"
    print("Filepath=" + filepath)
    
    row=1
    print("Camera matrix world",cam.matrix_world[row] )
      
    #write 4x4 world matrix
    f = open(filepath, 'w', encoding='utf-8')
    
    for row in range(0,4):
        f.write("%5.3f, %5.3f, %5.3f, %5.3f  " % (cam.matrix_world[row][0],
            cam.matrix_world[row][1], cam.matrix_world[row][2], 
            cam.matrix_world[row][3]))
            
    f.close()
    """
    
    location, rotation = cam.matrix_world.decompose()[0:2]
    print("Camera pos:", location[0], location[1], location[2])
    
    #quaternion.  rotation[0]=w
    print("Camera quaternion:", rotation[0], rotation[1], rotation[2],  rotation[3])

    print("Camera matrix world",cam.matrix_world )
    
    
    #save npz
    """
    filepath="C:\\Users\\bflug\\Documents\\BlenderFilesByBill\\camera_pose.npz"
    print("Filepath=" + filepath)
    data_dict={'poses' : cam.matrix_world}

    numpy.savez_compressed(filepath, **data_dict)
    
     # load the npz file
    loaded_data = numpy.load(filepath)
    loaded_poses = loaded_data['poses']
    print("Poses from npz", loaded_poses)
    """
    
    # save all poses to npz
    filepath="C:\\Users\\bflug\\Documents\\BlenderFilesByBill\\camera_poses.npz"
    SavePosesToNPZ(cam, filepath)
    
     # load the npz file
    loaded_data = numpy.load(filepath)
    loaded_poses = loaded_data['poses']
    print("Loaded poses", loaded_poses)
    print("Shape of poses tensor loaded:", loaded_poses.shape)
    
    return {'FINISHED'}
