Summary:        %Summary
Name:           kdiff3
Version:        0.9.95
Release:        %mkrel 3
Summary:	Summary Utility for comparing/merging up to three text files or directories
License:	GPLv2+
Group:		Development/Other
Source:		http://downloads.sourceforge.net/kdiff3/kdiff3-%{version}.tar.bz2
Url: 		http://kdiff3.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-devel
BuildRequires:	desktop-file-utils

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
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

desktop-file-install --vendor="" \
  --add-category="Qt" \
  --add-category="KDE" \
  --add-category="Development" \
  --dir $RPM_BUILD_ROOT%{_kde_datadir}/applications/kde4 $RPM_BUILD_ROOT%{_kde_datadir}/applications/kde4/*.desktop

%find_lang %{name} %{name} kdiff3plugin --with-html

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/*
%{_kde_appsdir}/%name
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_iconsdir}/*/*/apps/*.png
%{_kde_services}/*.desktop
