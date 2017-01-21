#!/usr/bin/python

from opencv.cv import *
from opencv.highgui import *
from cvaux import *
import sys
from matlab_syntax import figure,image,ginput 
from opencv.adaptors import *
from scipy import *

def usage(name):
    print "USAGE: %s <file1> <sync_idx> <start_idx> <file2> <sync_idx>" % name
    print "    <sync_idx> the zero-based frame index to syncronize the two files on"
    print "    <start_idx> the zero-based frame index to start training on"

def main(argv):
    if len(argv)<6:
        usage(argv[0])
        sys.exit(-1)

    cap = [None, None]
    cap[0] = cvCreateFileCapture( argv[1] )
    assert(cap[0])
    cap[1] = cvCreateFileCapture( argv[4] )
    assert(cap[1])

    
    sync_idx = [ int(sys.argv[2]), int(sys.argv[5]) ]
    start_idx = int(sys.argv[3])


    print "Syncronizing files"
    for k in range(2):
        for i in range(sync_idx[k]):
            cvGrabFrame(cap[k])

    print "Seeking to frame %d" % start_idx
    for i in xrange(start_idx):
        cvGrabFrame(cap[0])
        cvGrabFrame(cap[1])
        if(i % 30 == 0):
            print "%d of %d" % (i, start_idx)
    
    bgmodel = [ cvCreateGaussianBGModel( cvRetrieveFrame(cap[0]) ),
                cvCreateGaussianBGModel( cvRetrieveFrame(cap[1]) ) ]

    figure(1); image( cvRetrieveFrame(cap[0]) ) 
    figure(2); image( cvRetrieveFrame(cap[1]) )
    query_pt=None

    figure(1)
    print "Select a point in figure 1 to learn"
    while query_pt is None:
        query_pt = ginput(1)

    print "Selected point =", query_pt

    ### initialize model
    num_fg1 = 0
    sz = [ cvGetSize(cvRetrieveFrame(cap[0])),
           cvGetSize(cvRetrieveFrame(cap[1])) ]
    num_fg1_image2 = [ ones( [sz[0].height, sz[0].width] ), 
                       ones( [sz[1].height, sz[1].width] ) ]
    num_image2 = [ ones( [sz[0].height, sz[0].width] ), 
                   ones( [sz[1].height, sz[1].width] ) ]
    X=[]
    Y=[]
    frameno=1
    while cvWaitKey(33)!='q':
        im0 = cvQueryFrame( cap[0] )
        im1 = cvQueryFrame( cap[1] )
        cvUpdateBGStatModel( im0, bgmodel[0] )
        cvUpdateBGStatModel( im1, bgmodel[1] )

        fg2 = Ipl2NumPy(bgmodel[1].foreground)
        bg2 = ~fg2

        fg1 = int( bgmodel[0].foreground[query_pt.y, query_pt.x] > 0 )
        bg1 = int( ~fg1 )
    
        ### prediction
        prior = num_fg1/float(frameno);
        pr = prior;

        if prior > 0:
            fgratio = fg2 * (num_fg1_image2[1] / (prior * num_image2[1]))
            bgratio = bg2 * (num_fg1_image2[0] / (prior * num_image2[0]))
            ratio = fgratio + bgratio; 
	       
            X.append( fg1 );
            Y.append( sum(log(ratio)) );
            print X
            print Y

        ### update model
        num_fg1 = num_fg1 + fg1;
        if fg1:
            num_fg1_image2[0] += bg2;
            num_fg1_image2[1] += fg2;
        print "isfg1: %d totalfg1: %d" % (fg1, num_fg1)

        num_image2[0] += bg2;
        num_image2[1] += fg2;

        frameno += 1

        # display results
        figure(1); image(bgmodel[0].foreground)
        figure(2); image(bgmodel[1].foreground)
        

if __name__ == "__main__":
    main(sys.argv)

