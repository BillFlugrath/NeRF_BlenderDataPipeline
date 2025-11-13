The following describes how to generate training data for the NeRF demo app.  The training data exists in a single .npz file that contains camera poses, images, and focal length.

See the included Blender example file for an example of the process.

Create a Blender scene file with an object at origin and animate a camera that rotates around the object for a full 360 degrees. 

With the scene created, the first step is to export the image sequence.  The image sequence is a sequence of image files where each file corresponds to one frame of the camera animation.

How to output training data images:

To animate camera:
1) Set Begin and End frames for the scene in the lower right corner of Layout screen.
2) Move and rotate it and press "I" key to set a key frame.

To output png image sequence:
1) Choose camera.
2) Select the Output Properties tab ( looks like a printer)
	In Frame Range, set Frame Start and End values for the animation.
	In the Output, choose folder to write image sequence to and choose file type ex png

3) Go to the top tool bar of Window and Select Render->Render Animation.  This will trigger the frame
by frame output of the rendered images, one image per frame into the output folder.
4) Check the output folder and make sure the folder has the correct jpg, png, etc images.

The next step is to create the final npz file.  This file will hold the training data that will be read by the demo NeRF application.


Start python script to output final .npz file:


1) Load the text file "export_training_data_to_npz.py" via the Scripting tab->Text->Open.

2) Choose Text->Run Script from the Scripting toolbar.

The Python console should now be open.

3) There are several user defined variables in the script that need to be manually set, these are:

    input_images_path = "./tmp" folder with the previously output image sequence
    save_file_out_name = "training_data_final.npz" final filename with training data to output
    input_poses_path = "./camera_poses.npz" file that contains the temp npz file
    num_images = 106  the number of images in the sequence
    width = 100  width of each image
    height = 100 height of each image
    fov = 29.0  camera fov
    compress_npz= True

The only variables that *must* be updated are input_images_path, num_images, width, and height.
The other variables can use the default values if you wish.  Just update them in the python script and save the file.  Be sure that Blender uses the changes to the variables since sometimes Blender may use previous data.


4) In the python console on left screen panel type:

>>>myModule = bpy.data.texts[0].as_module()
>>>myModule.ExportAll()

ExportAll() is a function in the open .py script.  If a few scripts were opened, it might be necessary to change the index such as myModule = bpy.data.texts[1].as_module() for example to use the 2nd script that was opened.


5) The files "training_data_final.npz" and "camera_poses.npz" should have been generated. 


The file "training_data_final.npz" is the default name in the python script for the final training data file.  It can be renamed if desired.  This is the file that the NeRF application will read and use to train with.

The file "camera_poses.npz" is a temporary file and is not needed.

The NeRF app has a hardcoded filename, "tiny_nerf_data".  Either change the name to the new npz file, "training_data_final.npz" or rename the new file.






