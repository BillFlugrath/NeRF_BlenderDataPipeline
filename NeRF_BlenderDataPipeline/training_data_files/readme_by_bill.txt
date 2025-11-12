This directory contains the  file required to train the nerf. Specifically, it contains
an npz file with:

1) the training image data
2) the poses for the camera used to generate each image
3) camera fov



The pose data and image data can be created using Blender.  Create a scene in Blender with an
animated camera that orbits around a model.  The camera should orbit around the entire model ie
360 degrees.

Use the py script "export_camera_pose_data_to_npz.py" to generate a view matrix for each
camera position used to generate the image training data.  This is a single output file, "camera_poses.npz"
that can be used directly with the nerf app.  There must be one view matrix (i.e. pose) for each
frame of animation.

The image data (ie jpg or png image sequence) should be output with the Blender interface.
To output png image sequence in Blender:
Choose camera. Select the Output Properties tab ( looks like a printer)
	In Frame Range, set Frame Start and End values for the animation.
	In the Output choose folder to write image sequence to and choose file type ex png
