# BabyCare
&emsp;&emsp;Infant monitoring application based on deep learning and stereo vision
* [x] Distance Measurement
* [ ] Expression Detection
<div align=center><img  src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/gifhome_480x360.gif"/></div>

### Requirement:
* python3.6
* tenosorflow&ge;1.12(Some problem may occur; such as [**mkl**](https://github.com/tensorflow/tensorflow/issues/23145))
* opencv
* matlab.engine (MATLAB R2014b or later)
* numpy
----
### To install the engine API, choose one of the following.

&emsp;At a **Windows** operating system prompt —

    cd "matlabroot\extern\engines\python"
    python setup.py install
You might need administrator privileges to execute these commands.

&emsp;At a **macOS** or **Linux** operating system prompt —

    cd "matlabroot/extern/engines/python"
    python setup.py install
    



## Stereo Camera Calibration
1. Prepare images, camera, and calibration pattern.
2. Add image pairs.
3. Calibrate the stereo camera.
4. Evaluate calibration accuracy.
5. Adjust parameters to improve accuracy (if necessary).
6. Export the parameters object.

### chessboard :
&emsp;&emsp;To improve the results, use between 10 and 20 images of the calibration pattern. The calibrator requires at least three images. Use uncompressed images or lossless compression formats such as **PNG**. The calibration pattern and the camera setup must satisfy a set of requirements to work with the calibrator. 
 &emsp;&emsp;The checkerboard pattern you use must not be square. One side must contain an even number of squares and the other side must contain an odd number of squares. Therefore, the pattern contains two black corners along one side and two white corners on the opposite side. This criteria enables the app to determine the orientation of the pattern. The calibrator assigns the longer side to be the x-direction.

| Size  | Formats | Number<span class="Apple-tab-span" style="white-space:pre"></span> | Spacing  |
| :-: | :-: | :-: | :-: |
| A3 | 420mm×297mm | 10*7 | 42 |

* Attach the checkerboard printout to a flat surface. Imperfections on the surface can affect the accuracy of the calibration.
* Measure one side of the checkerboard square. You need this measurement for calibration. The size of the squares can vary depending on printer settings.
* To improve the detection speed, set up the pattern with as little background clutter as possible.
* Keep the pattern in focus, but do not use autofocus.Do not modify the images, (for example, do not crop them).
* Capture the images of the pattern at a distance roughly equal to the distance from your camera to the objects of interest. For example, if you plan to measure objects from 2 meters, keep your pattern approximately 2 meters from the camera.
* Place the checkerboard at an angle less than 45 degrees relative to the camera plane.
*  Make sure the checkerboard pattern is fully visible in both images of each stereo pair.
 <div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/cameracalibrator_fov2.png"/> </div>
* Capture a variety of images of the pattern so that you have accounted for as much of the image frame as possible. Lens distortion increases radially from the center of the image and sometimes is not uniform across the image frame. To capture this lens distortion, the pattern must appear close to the edges of the captured images.
<div align=center><img width='40%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/calibration_radial_distortion.png"/></div>
<div align=center><img width='30%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/calibration_tangentialdistortion.png"/></div>


## Stereo Calibration Results:
<div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/a.png"/> </div>
  <div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/b.png"/> </div>
   <div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/c.png"/> </div>
    <div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/d.png"/> </div>
     <div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/e.png"/> </div>
     <div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/f.png"/> </div>

##   Experimental model
 <div align=center><img width='80%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/325.png"/> </div>
 
## Distance Measurement

 <div align=center><img width='50%' src = "https://github.com/wang-jinchao/BabyCare/blob/master/image/g.png"/> </div>
&emsp;&emsp; Using image semantic segmentation to get pixel-level image tags. The neural network model is an improvement from segnet. The basic structure is as shown above.  
&emsp;&emsp;Through Hough Transform to detection line and using convex hulls together to measure the minimum pixel distance on the image. Using the Transformation from the 3D space to the pixel plane, with the method of binocular vision to calculate the height from the camera to the plane
    ## Expression Detection
TBD
    