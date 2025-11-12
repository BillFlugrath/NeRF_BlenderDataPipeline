
import npz_file_utilities as bills_npz

# Create a new npz file for training data from a sequence of image files and camera poses file.
input_images_path = "./training_data_images"
save_file_out_name = "./training_data_files/training_data_final.npz"
input_poses_path = "./training_data_files/camera_poses.npz"
num_images = 106
width = 100
height = 100
fov = 29.0
compress_npz= True

# load raw images into npz and then combine them with the poses npz file to create final training data
bills_npz.Create_NPZFile_FromImageSequenceAndPoses(width, height,input_images_path, save_file_out_name,
                                                   num_images, input_poses_path, fov, compress_npz)