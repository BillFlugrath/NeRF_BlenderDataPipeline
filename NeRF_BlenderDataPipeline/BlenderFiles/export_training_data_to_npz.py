import bpy
import bpy_extras
from mathutils import Matrix
from mathutils import Vector
import numpy
from PIL import Image


def SavePosesToNPZ(cam, filepath):
    print("SavePosesToNPZ() called")
   
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



def Create_NPZFile_FromImageSequenceAndPoses(width, height,input_images_path, save_file_out_name, num_images,
                                             camera_poses_npz, fov, compress_npz):

    print("Create_NPZFile_FromImageSequenceAndPoses() called")
    
    W = width
    H = height
    num_channels = 3
    final_image_array = numpy.zeros( (num_images, H, W, num_channels ) )

    for i in range(0, num_images):
        fixed_length_string = f"{i:04d}"
        final_string_image_name = input_images_path + "/" + fixed_length_string + ".jpg"
        img_array = numpy.array(Image.open(final_string_image_name))
        image_array_float = img_array.astype(numpy.float32) / 255
        final_image_array[i] += image_array_float

    data = numpy.load(camera_poses_npz)
    poses = data["poses"]
    focal = numpy.array([fov])

    data_dict = {'images': final_image_array, 'poses': poses, 'focal': focal}

    if compress_npz == True:
        numpy.savez_compressed(save_file_out_name, **data_dict)
    else:
        numpy.savez(save_file_out_name, **data_dict)

    print("Saved images, poses, and fov to npz file")



print("Start script")

def ExportAll():
    print("ExportAll() called")
    ExportPoses()
    
def ExportPoses():
    print("ExportPoses() called")
    
    
    print("Camera pose export started...")
    
    # Insert your camera name here
    cam = bpy.data.objects['Camera']
 
    scene = bpy.context.scene
    frame = scene.frame_start

    
    #location, rotation = cam.matrix_world.decompose()[0:2]
    #print("Camera pos:", location[0], location[1], location[2])
    #quaternion.  rotation[0]=w
    #print("Camera quaternion:", rotation[0], rotation[1], rotation[2],  rotation[3])
    #print("Camera matrix world",cam.matrix_world )
    
    
    # save all poses to npz
    filepath=".\\camera_poses.npz"
    SavePosesToNPZ(cam, filepath)
    
     # load the npz file
    loaded_data = numpy.load(filepath)
    loaded_poses = loaded_data['poses']
    print("Loaded poses", loaded_poses)
    print("Shape of poses tensor loaded:", loaded_poses.shape)
    print("camera poses file loaded")
    
    
    # load image sequence into dictionary and combine with the poses
    # to create final npz training data file
    
    # USER DEFINED VALUES (ie Fill these in before export).
    
    input_images_path = "./tmp"
    save_file_out_name = "training_data_final.npz"
    input_poses_path = "./camera_poses.npz"
    num_images = 106
    width = 100
    height = 100
    fov = 29.0
    compress_npz= True

    # load raw images into npz and then combine them with the poses npz file to create final training data
    Create_NPZFile_FromImageSequenceAndPoses(width, height,input_images_path,
        save_file_out_name,num_images, input_poses_path, 
        fov, compress_npz)
    
    return {'FINISHED'}
