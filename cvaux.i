%module cvaux
%{
	#include "cvaux.h"
%}
%include "cvtypemaps.i"
CvBGStatModel* cvCreateFGDStatModel( IplImage* first_frame,
                    CvFGDStatModelParams* parameters=NULL);
/* Creates Gaussian mixture background model */
CvBGStatModel* cvCreateGaussianBGModel( IplImage* first_frame,
                CvGaussBGStatModelParams* parameters=NULL);


void cvReleaseBGStatModel( CvBGStatModel** bg_model );

int cvUpdateBGStatModel( IplImage* current_frame, CvBGStatModel*  bg_model );

void cvRefineForegroundMaskBySegm( CvSeq* segments, CvBGStatModel*  bg_model );

int  cvChangeDetection( IplImage*  prev_frame,
		IplImage*  curr_frame,
		IplImage*  change_mask );

struct CvBGStatModel {
	int             type; /*type of BG model*/                                      
	CvReleaseBGStatModel release;                                                   
	CvUpdateBGStatModel update;                                                     
	IplImage*       background;   /*8UC3 reference background image*/               
	IplImage*       foreground;   /*8UC1 foreground image*/                         
	IplImage**      layers;       /*8UC3 reference background image, can be null */ 
	int             layer_count;  /* can be zero */                                 
	CvMemStorage*   storage;      /*storage for ~Sforeground_regions~T*/              
	CvSeq*          foreground_regions; /*foreground object contours*/
};

