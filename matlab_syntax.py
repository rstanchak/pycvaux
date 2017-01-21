from opencv import *
from opencv.highgui import * 

#__all__ = ['imagesc', 'display', 'imread', 'imshow', 'saveimage', 'loadimage', 'pause',
#           'Image', 'Image8', 'Image8c3', 'Image32s', 'Image32f', 'Image64f']

def eye(*args):
    mat = array(*args)
    cvSetIdentity(mat);
    return mat

def ones(*args):
    mat = array(*args)
    cvSet(mat, cvScalarAll(1.0))
    return mat

def zeros(*args):
    mat = array(*args)
    cvSet(mat, cvScalarAll(0.0))
    return mat

def array(*args):
    m=1
    n=1
    c=1
    classname='single'
    nargs = len(args)
    # nasty argument parsing
    if nargs>0:
        if isinstance(args[0],tuple) or isinstance(args[0],list) and len(args[0]) > 1:
            m=args[0][0]
            n=args[0][1]
            if len(args[0])>2:
                c=args[0][2]
            if len(args)>1:
                classname = args[1]
        else:
            m=args[0]
            if nargs == 1:
                n=args[0]
            elif nargs > 1:
                # is the last argument the classname?
                if args[nargs-1].__class__ == str:
                    classname = args[nargs-1]
                    nargs-=1
                if nargs > 1:
                    n = args[1]
                if nargs > 2:
                    c = args[2]

    if(classname=='double'):
        depth=cv.CV_64F 
    elif(classname=='single'):
        depth=cv.CV_32F
    elif(classname=='int8'):
        depth=cv.CV_8S
    elif(classname=='uint8'):
        depth=cv.CV_8U
    elif(classname=='int16'):
        depth=cv.CV_16S
    elif(classname=='uint16'):
        depth=cv.CV_16U
    elif(classname=='int32' or classname=='uint32' or 
            classname=='int64' or classname=='uint64'):
        depth=cv.CV_32S
    else:
        depth=cv.CV_32F
    depth = CV_MAKETYPE(depth, c)
    return cvCreateMat(m,n,depth)
 
def size(X,dim=-1):
    # CvMat
    if hasattr(X, "type"):
        sz = (X.rows, X.cols, CV_MAT_CN(X.type))
    # IplImage
    elif hasattr(X, "nChannels"):
        sz = (X.height, X.width, X.nChannels)
    # CvMatNd
    else:
        sz = cvGetDims(X)

    if dim is -1:
        return sz
    return sz[dim]

def reshape(X, m, n=1, c=-1):
    '''
    reshape will produce different results in matlab and python due to the
    order of elements stored in the array (row-major vs. column major)
    '''
    if c==-1:
        c = CV_MAT_CN(X)
    return cvReshape(X, c, m)
     

def im2float(im):
    mat = cvGetMat(im);
    if CV_MAT_DEPTH(mat.type)==CV_32F:
        return mat
    
    im64f = array(size(im), 'float')
    cvConvertScale(im, im64f, 1.0, 0.0)
    return im64f

def im2double(im):
    mat = cvGetMat(im);
    if CV_MAT_DEPTH(mat.type)==CV_64F:
        return mat
    im64f = array(size(im), 'double')
    cvConvertScale(im, im64f, 1.0, 0.0)
    return im64f

def rgb2ntsc (rgb):
    trans = [ [0.299,  0.596,  0.211], [0.587, -0.274, -0.523], [0.114, -0.322,  0.312] ];
    return rgb * trans;
    
def rgb2gray(rgb):
    ntscmap = rgb2ntsc (rgb);
    graymap = ntscmap [:, 1] * ones (1, 3);
    return graymap

class CvFigureWindow:
    """
    Wrapper class for some matlab/octave/scilab syntax image viewing functions
    """
    wasClicked = False
    movedPoint = CvPoint()
    clickedPoint = CvPoint()
    name = ""
    flags = 0

    def __init__(self, name):
        self.name = name
        print name
        cvNamedWindow(name)

    def imagesc(self,im, clims=None):
        """
        Display a normalized version of the image
        """
        # don't normalize multichannel image
        #if(im.nChannels>1):
        #    if(im.depth!=cv.IPL_DEPTH_8U):
        #        im2 = cvCreateImage( cvSize(im.width, im.height), cv.IPL_DEPTH_8U, im.nChannels)
        #        cvScale(im, im2)
        #        im = im2
        #    cvShowImage(self.currentWindowName, im)
        #    return self.currentWindow
        
        # normalize image
        if clims:
            [minv, maxv] = clims
        else:
            [minv,maxv,minloc,maxloc] = cvMinMaxLoc(im)
        if maxv != minv:
            s = 255.0/(maxv-minv)
            shift =  255*(-minv)/(maxv-minv)
        else:
            s = 1.0
            shift = -maxv

        im2 = array( size(im), 'uint8' )
        cvConvertScale(im, im2, s, shift)
        
        cvShowImage(self.name, im2)

    def image(self, im):
        """
        Display image as is -- probably not what you'd expect for FP or integer images
        """
        cvShowImage(self.name ,im)
    
    def ginput(self, n=1):
        # bring to front
        cvNamedWindow(self.name, self.flags)

        # install ginput mouse handler
        cvSetMouseCallback(self.name, static_ginputCB, self)

        # TODO save existing handler and restore on exit 

        # reset 'clicked' indicator
        self.wasClicked=False;

        # wait until clickNum increments
        while not self.wasClicked:
            if cvWaitKey(33)=='q':
                return None
        return self.clickedPoint

    def ginputCB( self, event, x, y, flags ):
        if event==CV_EVENT_LBUTTONDOWN:
            if not self.wasClicked:
                self.clickedPoint.x = x;
                self.clickedPoint.y = y;
                self.wasClicked=True;
        if event==CV_EVENT_MOUSEMOVE:
            self.movedPoint.x = x;
            self.movedPoint.y = y;

class CvFigureManager:
    def __init__(self):
        self.currentWindow = -1
        self.maxWindow = 0 
        self.windows = {} 
        pass

    def figure(self, index=-1):
        """
        open a window
        """
        self.__figure__(index)
        return self.currentWindow
    
    def __figure__(self, index=-1):
        if(index==-1):
            if(self.currentWindow==-1): 
                self.maxWindow = a 
                index = 1
            else:
                index = self.currentWindow

        if(index > self.maxWindow):
            self.maxWindow = index;

        try:
            window = self.windows[index];
        except KeyError:
            name = "opencv-python window %d" % index
            window = CvFigureWindow( name )
            self.windows[index] = window

        self.currentWindow = index;
        return window

    def ginput( self, *args):
        return self.__figure__().ginput(*args)

    def imagesc( self, *args):
        return self.__figure__().imagesc(*args)

    def image( self, *args ):
        return self.__figure__().image(*args)

    def imshow( self, *args ):
        return self.__figure__().imshow(*args)

    def gcf( self ):
        return self.currentWindow
    



def static_ginputCB( event, x, y, flags, param ):
    param.ginputCB(event,x,y,flags)

def drawnow():
    cvWaitKey(10)

def pause(delay=-1):
    if delay<0:
        cvWaitKey(-1)
    else:
        cvWaitKey(delay*1000)


# redirect static function to FigureMangager members
__figuremanager__ = CvFigureManager()
imagesc = __figuremanager__.imagesc
display = __figuremanager__.figure
figure = __figuremanager__.figure
image = __figuremanager__.image
imshow = __figuremanager__.image
ginput = __figuremanager__.ginput
gcf = __figuremanager__.gcf

def imread(fname):
    return cvLoadImage(fname, -1)   
loadimage = imread
imload = imread

def imsave(im, fname, format):
    return cvSaveImage(fname, im)
saveimage = imsave

def gradient(F):
    F = im2float(F)
    Fx = array(size(F))
    Fy = array(size(F))
    
    # new images
    cvSobel(F, Fx, 1, 0, CV_SCHARR)
    cvSobel(F, Fy, 0, 1, CV_SCHARR)
    return (Fx, Fy)
