%define name    kdiff3
%define version 0.9.90
%define release %mkrel 2
%define Summary Utility for comparing/merging up to three text files or directories

%define section Applications/Development/Tools
%define title Kdiff3

# Work around for different libtool use in kde 
%define __libtoolize true

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release

License: GPL
Group: Development/Other
Source: kdiff3-%{version}.tar.bz2
Url: http://kdiff3.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs-devel

%description
KDiff3 is a file and directory diff and merge tool which:
   * compares and merges two or three text input files or directories
   * shows the differences line by line and character by character(!)
   * provides an automatic merge-facility
   * has an editor for comfortable solving of merge-conflicts
   * provides networktransparency via KIO
   * has options to highlight or hide changes in white-space or comments

%prep
%setup -q

%build
#make -f admin/Makefile.common cvs

export QTDIR=%_prefix/%_lib/qt3
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

# Search for qt/kde libraries in the right directories (avoid patch)
# NOTE: please don't regenerate configure scripts below
#perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt)_(libdirs|libraries)=/" configure

%{?__cputoolize: %{__cputoolize} }

%configure
%make

%install
rm -rf %buildroot
%makeinstall

# Menu
mkdir -p %{buildroot}/%{_menudir}
cat > %{buildroot}/%{_menudir}/%{name} << EOF
?package(%{name}): \
command="%{_bindir}/%{name}" \
needs="X11" \
icon="%{name}.png" \
section="%{section}" \
title="%{title}" \
longtitle="%{Summary}"\
xdg="true"
EOF

desktop-file-install --vendor="" \
  --add-category="Qt" \
  --add-category="X-MandrivaLinux-MoreApplications-Development-Tools" \
  --add-category="KDE" \
  --add-category="Development" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applnk/Development $RPM_BUILD_ROOT%{_datadir}/applnk/Development/*

#mdk icons
install -D -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png
install -D -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %buildroot

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%{_libdir}/kde3/*.la
%{_libdir}/kde3/*.so
%defattr(0644,root,root,0755)
%{_menudir}/%{name}
%{_datadir}/apps/kdiff3/kdiff3_shell.rc
%{_datadir}/apps/kdiff3part/kdiff3_part.rc
%{_datadir}/applnk/Development/kdiff3.desktop
%{_datadir}/icons/*/*/apps/*.png
%{_datadir}/services/*.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/*/*
%doc %_docdir/HTML/%{name}/*
%doc %_docdir/HTML/*/%{name}/*
