# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _cvaux
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


cvReleaseBGStatModel = _cvaux.cvReleaseBGStatModel
cvUpdateBGStatModel = _cvaux.cvUpdateBGStatModel
cvRefineForegroundMaskBySegm = _cvaux.cvRefineForegroundMaskBySegm
cvChangeDetection = _cvaux.cvChangeDetection
class CvBGStatModel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvBGStatModel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvBGStatModel, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _cvaux.CvBGStatModel_type_set
    __swig_getmethods__["type"] = _cvaux.CvBGStatModel_type_get
    if _newclass:type = _swig_property(_cvaux.CvBGStatModel_type_get, _cvaux.CvBGStatModel_type_set)
    __swig_setmethods__["release"] = _cvaux.CvBGStatModel_release_set
    __swig_getmethods__["release"] = _cvaux.CvBGStatModel_release_get
    if _newclass:release = _swig_property(_cvaux.CvBGStatModel_release_get, _cvaux.CvBGStatModel_release_set)
    __swig_setmethods__["update"] = _cvaux.CvBGStatModel_update_set
    __swig_getmethods__["update"] = _cvaux.CvBGStatModel_update_get
    if _newclass:update = _swig_property(_cvaux.CvBGStatModel_update_get, _cvaux.CvBGStatModel_update_set)
    __swig_setmethods__["background"] = _cvaux.CvBGStatModel_background_set
    __swig_getmethods__["background"] = _cvaux.CvBGStatModel_background_get
    if _newclass:background = _swig_property(_cvaux.CvBGStatModel_background_get, _cvaux.CvBGStatModel_background_set)
    __swig_setmethods__["foreground"] = _cvaux.CvBGStatModel_foreground_set
    __swig_getmethods__["foreground"] = _cvaux.CvBGStatModel_foreground_get
    if _newclass:foreground = _swig_property(_cvaux.CvBGStatModel_foreground_get, _cvaux.CvBGStatModel_foreground_set)
    __swig_setmethods__["layers"] = _cvaux.CvBGStatModel_layers_set
    __swig_getmethods__["layers"] = _cvaux.CvBGStatModel_layers_get
    if _newclass:layers = _swig_property(_cvaux.CvBGStatModel_layers_get, _cvaux.CvBGStatModel_layers_set)
    __swig_setmethods__["layer_count"] = _cvaux.CvBGStatModel_layer_count_set
    __swig_getmethods__["layer_count"] = _cvaux.CvBGStatModel_layer_count_get
    if _newclass:layer_count = _swig_property(_cvaux.CvBGStatModel_layer_count_get, _cvaux.CvBGStatModel_layer_count_set)
    __swig_setmethods__["storage"] = _cvaux.CvBGStatModel_storage_set
    __swig_getmethods__["storage"] = _cvaux.CvBGStatModel_storage_get
    if _newclass:storage = _swig_property(_cvaux.CvBGStatModel_storage_get, _cvaux.CvBGStatModel_storage_set)
    __swig_setmethods__["foreground_regions"] = _cvaux.CvBGStatModel_foreground_regions_set
    __swig_getmethods__["foreground_regions"] = _cvaux.CvBGStatModel_foreground_regions_get
    if _newclass:foreground_regions = _swig_property(_cvaux.CvBGStatModel_foreground_regions_get, _cvaux.CvBGStatModel_foreground_regions_set)
    def __init__(self, *args): 
        this = _cvaux.new_CvBGStatModel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cvaux.delete_CvBGStatModel
    __del__ = lambda self : None;
CvBGStatModel_swigregister = _cvaux.CvBGStatModel_swigregister
CvBGStatModel_swigregister(CvBGStatModel)
cvCreateFGDStatModel = _cvaux.cvCreateFGDStatModel
cvCreateGaussianBGModel = _cvaux.cvCreateGaussianBGModel



