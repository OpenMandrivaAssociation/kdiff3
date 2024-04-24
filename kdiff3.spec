Name:		kdiff3
Version:	1.11.0
Release:	1
Summary:	Summary Utility for comparing/merging up to three text files or directories
License:	GPLv2+
Group:		Development/Other
Url:		https://kde.org/applications/en/kdiff3
Source0:	https://download.kde.org/stable/kdiff3/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:	desktop-file-utils
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	boost-devel

%description
KDiff3 is a file and directory diff and merge tool which:
   * compares and merges two or three text input files or directories
   * shows the differences line by line and character by character(!)
   * provides an automatic merge-facility
   * has an editor for comfortable solving of merge-conflicts
   * provides networktransparency via KIO
   * has options to highlight or hide changes in white-space or comments

%prep
%autosetup -p1
sed -i 's|#include <QtGlobal>|#include <QtGlobal>\n#include <limits>|' src/TypeUtils.h

%cmake -DBUILD_WITH_QT6=ON

%build
%ninja -C build


%install
%ninja_install -C build

%find_lang %{name} kdiff3plugin kdiff3fileitemactionplugin diff_ext %{name}.lang --with-html

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/qt5/plugins/kf5/kfileitemaction/kdiff3fileitemaction.so
%{_libdir}/qt5/plugins/kf5/parts/kdiff3part.so
%{_datadir}/metainfo/org.kde.kdiff3.appdata.xml
%{_datadir}/applications/org.kde.kdiff3.desktop
%{_datadir}/kxmlgui5/kdiff3/kdiff3_shell.rc
%{_datadir}/kxmlgui5/kdiff3part/kdiff3_part.rc
%{_mandir}/man1/kdiff3.1.*
%{_mandir}/*/man1/kdiff3.1.*
%{_iconsdir}/hicolor/*/apps/kdiff3.*
%{_datadir}/kservices5/kdiff3part.desktop
