import tensorflow as tf
import numpy as np
from scipy.spatial.transform import Rotation as R

def GetRotationMatrix(euler_angles_np_array):
    euler_angles_deg = euler_angles_np_array  # X,Y,Z in XYZ order
    euler_angles_rad = np.radians(euler_angles_deg)

    # Create a Rotation object from Euler angles
    # Specify the order of rotations (e.g., 'xyz' forX-Y-Z intrinsic rotations)
    rotation = R.from_euler('xyz', euler_angles_rad)

    # Get the rotation matrix.  Its a ndarray(3,3)
    rotation_matrix = rotation.as_matrix()

   # print("Euler angles (degrees, XYZ order):", euler_angles_deg)
    #print("Rotation Matrix:\n", rotation_matrix)
    return rotation_matrix


def get_translation_matrix(x,y,z):
    matrix = [
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1],
    ]
    return matrix

def get_translation_t_2(t):
    """Get the translation matrix for movement in t."""
    matrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, t],
        [0, 0, 0, 1],
    ]
    return tf.convert_to_tensor(matrix, dtype=tf.float32)

# rotation around x-axis
def get_rotation_phi_2(phi):
    """Get the rotation matrix for movement in phi."""
    matrix = [
        [1, 0, 0, 0],
        [0, tf.cos(phi), -tf.sin(phi), 0],
        [0, tf.sin(phi), tf.cos(phi), 0],
        [0, 0, 0, 1],
    ]
    return tf.convert_to_tensor(matrix, dtype=tf.float32)

# rotation around y-axis
def get_rotation_theta_2(theta):
    """Get the rotation matrix for movement in theta."""
    matrix = [
        #[tf.cos(theta), 0, -tf.sin(theta), 0],  previous
        [tf.cos(theta), 0, tf.sin(theta), 0],
        [0, 1, 0, 0],
        [-tf.sin(theta), 0, tf.cos(theta), 0],
        #[tf.sin(theta), 0, tf.cos(theta), 0], previous
        [0, 0, 0, 1],
    ]
    return tf.convert_to_tensor(matrix, dtype=tf.float32)

# translation data in the last column ie column 3, row 0, row 1, row,2.  c2w[3,3] = 1.0 and c2w[0,0]=-1.0
def pose_spherical_2(theta, phi, t,  invert_y_axis):
    """
    Get the camera to world matrix for the corresponding theta, phi
    and t.
    """
    # c2w is "Camera To World"
    c2w = get_translation_t_2(t)
    c2w = get_rotation_phi_2(phi / 180.0 * np.pi) @ c2w
    c2w = get_rotation_theta_2(theta / 180.0 * np.pi) @ c2w

    if invert_y_axis == True:
        c2w = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) @ c2w
    #else:
    #   c2w = np.array([[-1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]) @ c2w  # swaps 2nd and 3rd rows

    return c2w



def GetAffineMatrix(matrix_3x3, translation_vector):
    # Create a 4x4 identity matrix
    matrix_4x4 = np.eye(4)

    # Embed the 3x3 matrix into the upper-left 3x3 block of the 4x4 matrix
    matrix_4x4[0:3, 0:3] = matrix_3x3

    # If you have a translation vector (tx, ty, tz), you can add it to the last column
    matrix_4x4[0:3, 3] = translation_vector

    return matrix_4x4

def GetAffineMatrix_2(matrix_3x3, translation_vector):

    # translation_vector=ndarray(3,) translation_vector[:, None] = ndarray(3,1)
    # ex if translation_vector=array([1,2,3]), then translation_vector[:, None]=array([ [1], [2], [3] ])

    # np.vstack and np.hstack first parameter is a sequence of arrays ie a tuple, thus we could do
    #htuple=(matrix_3x3, translation_vector[:, None])
    #horizontal_stack=np.hstack(htuple)

    matrix_4x4 = np.vstack((np.hstack((matrix_3x3, translation_vector[:, None])), [0, 0, 0, 1]))
    return matrix_4x4

def GetPoseMatrix(euler_angles, translation_vector):

    matrix_3x3=GetRotationMatrix(euler_angles)
    matrix_4x4 = GetAffineMatrix(matrix_3x3, translation_vector)
    return matrix_4x4

# create poses for testing
def GetGeneratedPoses_Debug(num_poses):
    cam_poses = np.zeros((num_poses, 4, 4),dtype=np.float32)

    start = 3.5
    step = 0.5

    euler_angles_array = np.array([0, 0, 0])
    x= start

    for index in range(0, num_poses):
        translation_array = np.array([x,-9.0,0])
        matrix4x4 = GetPoseMatrix(euler_angles_array, translation_array)
        cam_poses[index] = matrix4x4
        x -= step

    return cam_poses



