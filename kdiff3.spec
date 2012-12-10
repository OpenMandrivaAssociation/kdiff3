Name:		kdiff3
Version:	0.9.97
Release:	1
Summary:	Summary Utility for comparing/merging up to three text files or directories
License:	GPLv2+
Group:		Development/Other
Source:		http://downloads.sourceforge.net/kdiff3/kdiff3-%{version}.tar.gz
Url: 		http://kdiff3.sourceforge.net/
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
%makeinstall_std -C build

desktop-file-install --vendor="" \
  --add-category="Qt" \
  --add-category="KDE" \
  --add-category="Development" \
  --dir %{buildroot}%{_kde_datadir}/applications/kde4 %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop

%find_lang %{name} kdiff3plugin kdiff3fileitemactionplugin %{name}.lang --with-html

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/*
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/kdiff3part/kdiff3_part.rc
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/apps/*.png
%{_kde_services}/*.desktop

%changelog
* Tue Feb 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9.96-1mdv2011.0
+ Revision: 773971
- Update find_lang usage
- New version 0.9.96

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.95-3mdv2011.0
+ Revision: 612561
- the mass rebuild of 2010.1 packages

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 0.9.95-2mdv2010.1
+ Revision: 541551
- fix perms

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.9.95-1mdv2010.0
+ Revision: 370592
- New version 0.9.95

* Tue Jan 20 2009 Funda Wang <fwang@mandriva.org> 0.9.94-1mdv2009.1
+ Revision: 331516
- New version 0.9.94

* Fri Jan 09 2009 Funda Wang <fwang@mandriva.org> 0.9.93-1mdv2009.1
+ Revision: 327716
- 0.9.93 final

* Mon Jul 21 2008 Funda Wang <fwang@mandriva.org> 0.9.93-0.835723.1mdv2009.0
+ Revision: 239303
- BR dfu
- switch to kde4 version

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.9.92-1mdv2008.1
+ Revision: 136523
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 Funda Wang <fwang@mandriva.org> 0.9.92-1mdv2008.0
+ Revision: 43053
- BR kdebase
- clean spec file
  really xdg menu
- New upstream version
- Import kdiff3



* Wed Sep 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.90-2mdv2007.0
- Rebuild

* Mon May 15 2006 Laurent MONTEL <lmontel@mandriva.com> 0.9.90-1
- 0.9.90

* Mon Apr 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.89-1mdk
- New release 0.9.89

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.88-3mdk
- Fix Build
- use mkrel

* Fri May 06 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9.88-2mdk
- Fix build 

* Fri Feb 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.88-1mdk
- 0.9.88

* Tue Feb 01 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.87-1mdk
- 0.9.87

* Fri Aug 27 2004 Nick Brown <nickbrown@mandrake.org> 0.9.86-2mdk
- Rebuild for new menu

* Tue Jul 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.86-1mdk
- 0.9.86

* Mon Jun 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.84-2mdk
- Rebuild

* Tue Jun 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.84-1mdk
- 0.9.84

* Sat Mar 13 2004 Nick Brown <nickbroon@blueyonder.co.uk> 0.9.83-1mdk
- 0.9.83

* Mon Feb 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.82-1mdk

- 0.9.82

* Tue Jan 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.81-1mdk

- from Nick Brown <nickbroon@blueyonder.co.uk> : 
        - First Mandrake package release
