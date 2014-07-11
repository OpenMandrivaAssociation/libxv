%define major 1
%define libname %mklibname xv %{major}
%define devname %mklibname xv -d

Summary:	The Xv Library
Name:		libxv
Version:	1.0.10
Release:	7
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

%package -n %{libname}
Summary:	The Xv Library
Group:		Development/X11

%description -n %{libname}
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXv-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXv.so.%{major}*

%files -n %{devname}
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
%{_includedir}/X11/extensions/Xvlib.h
%{_mandir}/man3/Xv*

