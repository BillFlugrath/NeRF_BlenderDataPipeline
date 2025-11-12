# NeRF_BlenderDataPipeline
Create training data for NeRF demo app.

This project is used to create training data for a Neural Radiance Field ie NeRF demo application.  This demo can be found either:

1) https://github.com/keras-team/keras-io/blob/master/examples/vision/nerf.py
Or
2) https://keras.io/examples/vision/nerf/

Please download and checkout those links first.
They contain amazing information on the theory of NeRFs and how the demo code works.  The demo includes training data which is perfect for learning how NeRFs work.  If you wish to create new training data for the demo, and continue experimentation, then this project, NeRF_BlenderDataPipeline, can help with that. The demo comes with a file "tiny_nerf_data.npz" that is used for training. To use new training data, we simply need to make a new npz file that has the new data.  The NeRF_BlenderDataPipeline projects has an example Blender scene file with a camera animation.  This scene file can be used to generate new training data.  The training data for the NeRF demo is contained in a single npz file.  This file contains:
a) The images used for training
b) The camera poses (i.e. view matrices) used for training
c) A camera intrinsic scalar value called "Focal" which is roughly the focal length.
