CXX_FLAGS=`pkg-config opencv --cflags` -I/usr/include/python2.4
LD_FLAGS=`pkg-config opencv --libs`

_cvaux.so: _cvaux.o
	g++ -shared $(LD_FLAGS) $< -o $@

_cvaux.o: _cvaux.cxx
	g++ $(CXX_FLAGS) -fPIC -c $<

_cvaux.cxx: cvaux.i cvtypemaps.i
	swig -c++ -python -shadow $(CXX_FLAGS) -o $@ $<

clean: 
	rm -f _cvaux.cxx _cvaux.o _cvaux.so
