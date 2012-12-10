%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A simple painting program
Name:		mtpaint
Version:	3.40
Release:	2
License:	GPLv3
Group:		Graphics
URL:		http://mtpaint.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	ungifsicle

%description
A simple painting program to easily create pixel art and manipulate digital 
photos.

%prep
%setup -q

%build
%ifarch x86_64
%define	arch	x86-64
%endif

%ifarch %{ix86}
%define	arch	i586
%endif

%configure2_5x \
	--cpu=%{arch} \
	intl \
	man \
	gtkfilesel

%make

%install
%makeinstall_std

#screenshot menu entry
cat > %{buildroot}%{_datadir}/applications/%{name}-screenshot.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Get Screenshot
Comment=%{summary}
Exec=%{_bindir}/%{name} -s
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;X-MandrivaLinux-Multimedia-Graphics;
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-screenshot.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

