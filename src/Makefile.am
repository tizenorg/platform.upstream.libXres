lib_LTLIBRARIES = libXRes.la

libXRes_la_SOURCES =    \
        XRes.c

libXRes_la_LIBADD = @RESOURCEEXT_LIBS@ @XRES_LIBS@

AM_CFLAGS = @RESOURCEEXT_CFLAGS@

INCLUDES = -I$(top_srcdir)/include

#
# Library version info.  Check the libtool docs for
# instructions on when and how to change this value
#
libXRes_la_LDFLAGS = -version-info 1:0:0

libXResincludedir = $(includedir)/X11/extensions
libXResinclude_HEADERS = $(top_srcdir)/include/X11/extensions/XRes.h

