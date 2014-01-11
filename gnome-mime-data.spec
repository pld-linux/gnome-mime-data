Summary:	MIME and Application database for GNOME 2
Summary(pl.UTF-8):	Baza danych MIME i aplikacji dla GNOME 2
Name:		gnome-mime-data
Version:	2.18.0
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-mime-data/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	541858188f80090d12a33b5a7c34d42c
Patch0:		%{name}-duplicate-keys.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.2.3
BuildRequires:	intltool
BuildRequires:	rpmbuild(macros) >= 1.446
Provides:	gnome-vfs-data = %{version}
Obsoletes:	gnome-vfs-data
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the base MIME and Application database for GNOME
2. It is meant to be accessed through the MIME functions in GnomeVFS.

%description -l pl.UTF-8
Ten pakiet zawiera podstawowe bazy danych MIME i aplikacji dla GNOME
2. Przeznaczony jest do udostępniania przez funkcje MIME w GnomeVFS.

%description -l pt_BR.UTF-8
O GNOME MIME contém arquivos de identificação e tipos MIME para o
sistema GNOME 2.

%package devel
Summary:	Development files for gnome-mime-data
Summary(pl.UTF-8):	Pliki potrzebne przy tworzeniu programów używajacych gnome-mime-data
Group:		X11/Development/Libraries
# doesn't require base

%description devel
Developmet files for gnome-mime-data.

%description devel -l pl.UTF-8
Pliki potrzebne przy tworzeniu programów używajacych gnome-mime-data.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man5

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install man/gnome-vfs-mime.5 $RPM_BUILD_ROOT%{_mandir}/man5/gnome-vfs-mime.5

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{sr@Latn,sr@latin}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{sr@ije,sr@ijekavian}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_sysconfdir}/gnome-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info
%{_mandir}/man5/gnome-vfs-mime.5*

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/gnome-mime-data-2.0.pc
