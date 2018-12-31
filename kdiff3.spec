Name:		kdiff3
Version:	1.7.9.0
Release:	2
Summary:	Summary Utility for comparing/merging up to three text files or directories
License:	GPLv2+
Group:		Development/Other
Source:		https://github.com/KDE/kdiff3/kdiff3-%{version}.tar.gz
Url: 		https://github.com/KDE/kdiff3
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5PrintSupport)
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
%cmake_kde5

%build
%ninja -C build


%install
%ninja_install -C build

#desktop-file-install --vendor="" \
#  --add-category="Qt" \
#  --add-category="KDE" \
#  --add-category="Development" \
#  --dir %{buildroot}%{_kde_datadir}/applications/kde5 %{buildroot}%{_kde_datadir}/applications/kde5/*.desktop

%find_lang %{name} kdiff3plugin kdiff3fileitemactionplugin %{name}.lang --with-html

%files -f %{name}.lang
%{_bindir}/%{name}
#%%{_datdir}/kde5/*
%{_libdir}/qt5/plugins/kf5/kfileitemaction/kdiff3fileitemaction.so
%{_libdir}/qt5/plugins/kf5/parts/kdiff3part.so
%{_datadir}/appdata/org.kde.kdiff3.appdata.xml
%{_datadir}/applications/org.kde.kdiff3.desktop
%{_datadir}/kservices5/kdiff3part.desktop
%{_datadir}/kxmlgui5/kdiff3/kdiff3_shell.rc
%{_datadir}/kxmlgui5/kdiff3part/kdiff3_part.rc
%{_mandir}/man1/kdiff3.1.xz
%{_iconsdir}/hicolor/*/apps/kdiff3.*[gz]
%{_docdir}/HTML/en/kdiff3/*
