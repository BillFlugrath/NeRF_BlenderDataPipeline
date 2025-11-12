
import os

os.environ["KERAS_BACKEND"] = "tensorflow"

import tensorflow as tf

# Setting random seed to obtain reproducible results.
tf.random.set_seed(42)

import tensorflow.keras as keras
from tensorflow.keras import layers

import os
import numpy as np
from PIL import Image

import matrix_math_utilities as bills_math

#BillF added to prevent multiple copies of open mp dll
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

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
