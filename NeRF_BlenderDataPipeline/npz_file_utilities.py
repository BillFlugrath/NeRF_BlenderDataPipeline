
import os

os.environ["KERAS_BACKEND"] = "tensorflow"

# Setting random seed to obtain reproducible results.
import tensorflow as tf

tf.random.set_seed(42)

import tensorflow.keras as keras
from tensorflow.keras import layers

import os
#import glob
#import imageio.v2 as imageio
import numpy as np
#from tqdm import tqdm
#import matplotlib.pyplot as plt
import matrix_math_utilities as bills_math
from PIL import Image

#BillF added to prevent multiple copies of open mp dll
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Initialize global variables.

def Create_NPZFile_FromImageSequenceAndPoses(width, height,input_images_path, save_file_out_name, num_images,
                                             camera_poses_npz, fov, compress_npz):

    W = width
    H = height
    num_channels = 3
    final_image_array = np.zeros( (num_images, H, W, num_channels ) )

    for i in range(0, num_images):
        fixed_length_string = f"{i:04d}"
        final_string_image_name = input_images_path + "/" + fixed_length_string + ".jpg"
        img_array = np.array(Image.open(final_string_image_name))
        image_array_float = img_array.astype(np.float32) / 255
        final_image_array[i] += image_array_float

    data = np.load(camera_poses_npz)
    poses = data["poses"]
    focal = np.array([fov])

    data_dict = {'images': final_image_array, 'poses': poses, 'focal': focal}

    if compress_npz == True:
        np.savez_compressed(save_file_out_name, **data_dict)
    else:
        np.savez(save_file_out_name, **data_dict)

    print("Saved images, poses, and fov to npz file")

def Create_NPZFile_FromImageSequence(width, height,input_images_path, save_file_out_name, num_images):

    W = width
    H = height
    num_channels = 3
    final_image_array = np.zeros( (num_images, H, W, num_channels ) )

    for i in range(0, num_images):
        fixed_length_string = f"{i:04d}"
        final_string_image_name = input_images_path + "/" + fixed_length_string + ".jpg"
        img_array = np.array(Image.open(final_string_image_name))
        image_array_float = img_array.astype(np.float32) / 255
        final_image_array[i] += image_array_float

    # load the camera poses

    data_dict = {'images': final_image_array}
    np.savez_compressed(save_file_out_name, **data_dict)
    print("Saved images to npz file")

# Demo, not used.
def Create_NPZFile_ImagesOnly_1(save_file_out_path):
    img_array1 = np.array(Image.open("./training_data_images/Countdown_01.jpg"))
    img_array2 = np.array(Image.open("./training_data_images/Countdown_02.jpg"))
    img_array3 = np.array(Image.open( "./training_data_images/Countdown_03.jpg"))

    np.savez_compressed(save_file_out_path, *[img_array1,img_array2,img_array3])
    # or np.file_out_path(tmp, *img_array[:3])


def GetImageData(filepath):
    data = np.load(filepath)
    images = data["images"]
    return images

def GetCameraData(poses_npz_path):
    data = np.load(poses_npz_path)
    poses = data["poses"]
    focal = np.array([29.0])

    return poses, focal







