%define major 1
%define libname %mklibname xv %{major}
%define develname %mklibname xv -d

Name:		libxv
Summary:	The Xv Library
Version:	1.0.8
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

%package -n %{libname}
Summary:	The Xv Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Conflicts:	XFree86-compat-libs <= 4.1.0
Provides:	%{name} = %{version}

%description -n %{libname}
The  Xv  extension provides support for video adaptors attached to an X
display. Clients use Xv to gain access and manage sharing of a
display's video resources.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxv-devel = %{version}-%{release}
Obsoletes:	%{_lib}xv1-devel < 1.0.7
Obsoletes:	%{_lib}xv-static-devel < 1.0.7
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
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

%files -n %{develname}
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
%{_includedir}/X11/extensions/Xvlib.h
%{_mandir}/man3/Xv*


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.7-1
+ Revision: 783977
- version update 1.0.7

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.6-5
+ Revision: 783383
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-4
+ Revision: 745769
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-3
+ Revision: 662431
- mass rebuild

* Sat Feb 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-2
+ Revision: 638734
- fixed typo
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 590404
- new release

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2010.1
+ Revision: 463588
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-3mdv2010.0
+ Revision: 425949
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-2mdv2009.0
+ Revision: 265013
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 192977
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 153303
- Update BuildRequires and rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 136572
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

