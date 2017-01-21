#!/usr/bin/python

from opencv.cv import *
from opencv.highgui import *
from cvaux import *
import sys

cap = cvCreateFileCapture( sys.argv[1] )
assert(cap)

#bgmodel = cvCreateFGDStatModel( cvQueryFrame(cap) );
bgmodel = cvCreateGaussianBGModel( cvQueryFrame(cap) );

cvNamedWindow("orig")
cvNamedWindow("fg")
cvNamedWindow("bg")
while cap:
    im = cvQueryFrame(cap)
    cvUpdateBGStatModel( im, bgmodel )
    cvShowImage("fg", bgmodel.foreground)
    cvShowImage("bg", bgmodel.background)
    cvShowImage("orig", im)
    if cvWaitKey(33)=='q':
        break;
