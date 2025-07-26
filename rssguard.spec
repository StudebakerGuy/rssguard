%define		libname %mklibname %{name}
%define		develname	%{libname}-devel

Name:		rssguard
Version:	4.8.5
Release:	1
Source0:	https://github.com/martinrotter/rssguard/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	RSS Guard is a simple RSS/ATOM feed reader than can also play podcasts.
URL:		https://github.com/martinrotter/rssguard
License:	GPL-3.0
Group:		Networking/News
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Linguist)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	pkgconfig(Qt6OpenGLWidgets)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:	pkgconfig(mpv)
BuildRequires:	pkgconfig(sqlite3)
BuildSystem:	cmake

%description
RSS Guard is a simple RSS/ATOM feed reader which can work with
RSS/ATOM/JSON/iCalendar/Sitemap feeds as well as many online feed services:

Feedly
Gmail
Google Reader API (Bazqux, FreshRSS, Inoreader, Miniflux, Reedah, The Old
Reader and more)
Nextcloud News
Reddit (WIP)
Tiny Tiny RSS

RSS Guard is also podcast player as it can play everything via its built-in
mpv-based (or ffmpeg-based) media player.

Also, RSS Guard has built-in support for Gemini protocol, so it can download
all feed types over it.

%package -n %{libname}
Summary:	rssguard shared library

%description -n %{libname}
rssguard shared libary

%package -n %{develname}
Summary:	%{libname} development files

%description -n %{develname}
%{libname} development files

%prep
%autosetup -p1

%files

%{_bindir}/%{name}
%{_datadir}/applications/io.github.martinrotter.rssguard.desktop
%{_datadir}/icons/hicolor/256x256/apps/io.github.martinrotter.rssguard.png
%{_datadir}/metainfo/io.github.martinrotter.rssguard.metainfo.xml

%files -n %{libname}
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}/lib%{name}-*.so


%files -n %{develname}
%{_includedir}/lib%{name}/core/*.h
%{_includedir}/lib%{name}/database/*.h
%{_includedir}/lib%{name}/exceptions/*.h
%{_includedir}/lib%{name}/gui/*.h
%{_includedir}/lib%{name}/gui/dialogs/*.h
%{_includedir}/lib%{name}/gui/reusable/*.h
%{_includedir}/lib%{name}/gui/webviewers/qtextbrowser/*.h
%{_includedir}/lib%{name}/gui/webviewers/webengine/*.h
%{_includedir}/lib%{name}/miscellaneous/*.h
%{_includedir}/lib%{name}/network-web/*.h
%{_includedir}/lib%{name}/services/abstract/*.h
%{_includedir}/lib%{name}/services/abstract/gui/*.h

