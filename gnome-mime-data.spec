Summary:	The GNOME2 virtual file-system libraries
Summary(pl):	Biblioteki wirtualnego systemu plików dla GNOME2
Summary(pt_BR):	Arquivos de dados tipo MIME para o desktop GNOME
Name:		gnome-mime-data
Version:	2.4.1
Release:	4
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-mime-data/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	a8bd52c6876a5294abc402f8a581ac1a
URL:		http://www.gnome.org/
Patch0:		%{name}-duplicate-keys.patch
Patch1:		%{name}-locale-names.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.3
BuildRequires:	libtool
Provides:	gnome-vfs-data = %{version}
Obsoletes:	gnome-vfs-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains the base MIME and Application database for GNOME.
It is meant to be accessed through the MIME functions in GnomeVFS.

%description -l pl
Ten modu³ zawiera bazowe MIME oraz bazê Aplikacji dla GNOME.
Przeznaczony jest do udostêpniania przez funkcje MIME w GnomeVFS.

%description -l pt_BR
O GNOME MIME contém arquivos de identificação e tipos MIME para o
sistema GNOME.

%package devel
Summary:	Development files for gnome-mime-data
Summary(pl):	Pliki potrzebne przy tworzeniu programów u¿ywajacych gnome-mime-data
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Developmet files for gnome-mime-data.

%description devel -l pl
Pliki potrzebne przy tworzeniu programów u¿ywajacych gnome-mime-data.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install -d $RPM_BUILD_ROOT%{_mandir}/man5
install man/gnome-vfs-mime.5 $RPM_BUILD_ROOT%{_mandir}/man5/gnome-vfs-mime.5

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%{_sysconfdir}/gnome-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
