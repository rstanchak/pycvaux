#!/usr/bin/python
from opencv.cv import *
from opencv.highgui import *
from matlab_syntax import *

im = loadimage('/home/roman/pics/goofy.jpg')
figure(1)
image(im)
figure(2)
image(im)
figure(1); print ginput()
