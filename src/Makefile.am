lib_LTLIBRARIES = libXRes.la

libXRes_la_SOURCES =    \
        XRes.c

libXRes_la_LIBADD = @RESOURCE_EXT_LIBS@ @XRES_LIBS@

#
# Library version info.  Check the libtool docs for
# instructions on when and how to change this value
#
libXRes_la_LDFLAGS = -version-info 0:0:0

libXResincludedir = $(includedir)/X11/extensions
libXResinclude_HEADERS = $(top_srcdir)/include/X11/extensions/XRes.h

