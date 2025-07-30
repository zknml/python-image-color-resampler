# python-image-color-resampler
Simple python script to convert an image's colors to those of another image. The script uses a *k*-d tree to find the nearest neighbor of each color in the target image among the colors of the source image, in RGB coordinates. 

Provide the filenames or filepaths of your color source, target image, and output image when prompted. The script will create the output image in the directory from which it is run.

## Sample Target Image
![Target image, a saturated blue desktop background](sampletarget.jpg)

## Sample Color Source
![Color source image, a more subdued sunset desktop background](samplesource.png)

## Sample Output
![Output image, a now-desaturated blue desktop background](sampleoutput.jpg)

<sub>*Useful for matching your desktop backgrounds!*</sub>
