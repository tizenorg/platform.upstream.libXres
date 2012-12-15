Name:           libXres
Version:        1.0.6
Release:        1
License:        MIT
Summary:        X-Resource extension client library
Url:            http://www.x.org
Group:          System Environment/Libraries
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
X-Resource is an extension that allows a client to query
the X server about its usage of various resources.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libXres development package

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXRes.so.1
%{_libdir}/libXRes.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/XRes.h
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
