%include "exception.i"

%typemap(in) IplImage * (IplImage header){
	void * vptr;
	int res = SWIG_ConvertPtr($input, (&vptr), $descriptor( CvMat * ), 0);
	if ( res == -1 ){
		SWIG_exception( SWIG_TypeError, "%%typemap(in) IplImage * : could not convert to CvMat");
		SWIG_fail;
	}
	$1 = cvGetImage((CvMat *)vptr, &header);
}


%typemap(typecheck) IplImage * {
	void * ptr;
	if(SWIG_ConvertPtr($input, (void **) &ptr, $1_descriptor, 0) != -1 ) {
		$1 = 1;
	}
	else if(SWIG_ConvertPtr($input, (void **) &ptr, $descriptor(CvMat *), 0) != -1 ){
		$1 = 1;
	}
	else{
		$1 = 0;
	}
}

%typemap(out) IplImage * {
	IplImage * im = $1;
	if(im){
		CvMat * mat = (CvMat *)cvAlloc(sizeof(CvMat));
		mat = cvGetMat(im, mat);
		$result = SWIG_NewPointerObj(mat, $descriptor(CvMat *), 1); 
	}
	else{
		$result = Py_None;
	}
}

