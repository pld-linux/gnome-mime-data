Summary:	The GNOME2 virtual file-system libraries
Summary(pl):	Biblioteki wirtualnego systemu plików dla GNOME2
Name:		gnome-mime-data
Version:	1.0.7
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/gnome-mime-data/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildArch:	noarch
Provides:	gnome-vfs-data = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome-vfs-data

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME2

%description
This module contains the base MIME and Application database for GNOME.
It is meant to be accessed through the MIME functions in GnomeVFS.

%description -l pl
Ten modu³ zawiera bazowe MIME oraz bazê Aplikacji dla GNOME.
Przeznaczony jest do udostêpniania przez funkcje MIME w GnomeVFS.

%package devel
Summary:	Development files for gnome-mime-data
Summary(pl):	Pliki potrzebne przy tworzeniu programów u¿ywajacych gnome-mime-data
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Developmet files for gnome-mime-data.

%description devel -l pl
Pliki potrzebne przy tworzeniu programów u¿ywajacych gnome-mime-data.

%prep
%setup -q

%build
rm -f missing
gettextize --copy --force
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog README NEWS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/*
%{_datadir}/application-registry
%{_datadir}/mime-info/*
%{_mandir}/man5/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
