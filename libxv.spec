%define major 1
%define libname %mklibname xv %{major}
%define develname %mklibname xv -d

Name: libxv
Summary:  The Xv Library
Version: 1.0.6
Release: 5
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

%package -n %{libname}
Summary:  The Xv Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Conflicts: XFree86-compat-libs <= 4.1.0
Provides: %{name} = %{version}

%description -n %{libname}
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libxv-devel = %{version}-%{release}
Obsoletes: %{_lib}xv1-devel
Obsoletes: %{_lib}xv-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXv-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXv.so.%{major}*

%files -n %{develname}
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
%{_includedir}/X11/extensions/Xvlib.h
%{_mandir}/man3/Xv*

