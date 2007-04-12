%define libxv %mklibname xv 1
Name: libxv
Summary:  The Xv Library
Version: 1.0.3
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

#-----------------------------------------------------------

%package -n %{libxv}
Summary:  The Xv Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Conflicts: XFree86-compat-libs <= 4.1.0
Provides: %{name} = %{version}

%description -n %{libxv}
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

#-----------------------------------------------------------

%package -n %{libxv}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxv} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxv-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxv}-devel
Development files for %{name}

%pre -n %{libxv}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxv}-devel
%defattr(-,root,root)
%{_libdir}/libXv.so
%{_libdir}/libXv.la
%{_libdir}/pkgconfig/xv.pc
%{_includedir}/X11/extensions/Xvlib.h
%{_mandir}/man3/Xv*

#-----------------------------------------------------------

%package -n %{libxv}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxv}-devel = %{version}
Provides: libxv-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxv}-static-devel
Static development files for %{name}

%files -n %{libxv}-static-devel
%defattr(-,root,root)
%{_libdir}/libXv.a

#-----------------------------------------------------------

%prep
%setup -q -n libXv-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxv}
%defattr(-,root,root)
%{_libdir}/libXv.so.1
%{_libdir}/libXv.so.1.0.0


