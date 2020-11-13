# libXv is used by ffmpeg, ffmpeg is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 1
%define libname %mklibname xv %{major}
%define devname %mklibname xv -d
%define lib32name libxv%{major}
%define dev32name libxv-devel

Summary:	The Xv Library
Name:		libxv
Version:	1.0.11
Release:	5
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%if %{with compat32}
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	The Xv Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXv-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure


%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXv.so.%{major}*

%files -n %{devname}
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
%{_includedir}/X11/extensions/Xvlib.h
%{_mandir}/man3/Xv*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXv.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXv.so
%{_prefix}/lib/pkgconfig/xv.pc
%endif
