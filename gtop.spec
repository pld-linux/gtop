Summary:	The GNOME system monitor
Summary(pl):	Monitor systemu dla GNOME
Name:		gtop
Version:	1.0.11
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gtop/%{name}-%{version}.tar.gz
Patch0:		%{name}-gcc296.patch
URL:		http://www.gnome.org/
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libgtop-devel >= 1.0.6
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This package will install the GNOME system monitor gtop, which shows
memory graphs and processes.

%description -l pl
Ten pakiet zawiera gtop - monitor systemu dla GNOME, wy¶wietlaj±cy w
postaci graficznej informacje na temat pamiêci i procesów.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/System

gzip -9nf AUTHORS TODO ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/*

%config(noreplace) %verify(not size mtime md5) %{_datadir}/gtoprc

%{_applnkdir}/System/gtop.desktop
%{_pixmapsdir}/*
