%bcond_with x

Name:           libXres
Version:        1.0.7
Release:        1
License:        MIT
Summary:        X-Resource extension client library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source0:        %{name}-%{version}.tar.bz2
Source1001: 	libXres.manifest
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%if !%{with x}
ExclusiveArch:
%endif

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
cp %{SOURCE1001} .

%build
%autogen --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXRes.so.1
%{_libdir}/libXRes.so.1.0.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/XRes.h
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
