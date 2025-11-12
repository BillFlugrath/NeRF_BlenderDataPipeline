To start your python script to Output Camera Poses:

1) Load the text file "camera_poses.npz" via the Scripting tab->Text->Open.

2) Choose Text->Run Script from the Scripting toolbar.

The Python console should now be open.

3) In the python console on left screen panel:
>>>myModule = bpy.data.texts[0].as_module()
>>>myModule.ExportPoses()

4) The file "camera_poses.npz" should have been generated.  Copy it to the correct location in your nerf
application folder for later use in training.

ExportPoses() is a function in the open .py script.  If a few scripts were opened, it might be necessary to change the index such as myModule = bpy.data.texts[1].as_module() for example to use the 2nd script that ws opened.


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


At this point, copy the exported image sequence and "camera_poses.npz" file to the folder where the "create_npz_files_app.py"script exists.  Open the python script, "create_npz_files_app.py" and set the input filenames, images sizes, etc.  Then run the script.  The output will be a single npz file ready to be used for training.

