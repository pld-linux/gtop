Summary:	The GNOME system monitor
Summary(pl):	Monitor systemu dla GNOME
Name:		gtop
Version:	1.0.5
Release:	3
License:	GPL
Group:		X11/GNOME/Applications
Group(pl):	X11/GNOME/Aplikacje
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/gtop/%{name}-%{version}.tar.gz
Patch:		gtop-applnk.patch
URL:		http://www.gnome.org/
BuildRequires:	XFree86-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	imlib-devel
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
This package will install the GNOME system monitor gtop, which shows memory
graphs and processes.

%description -l pl
Ten pakiet zawiera gtop - monitor systemu dla GNOME, wy¶wietlaj±cy w
postaci  graficznej informacje na temat pamiêci i procesów.

%prep
%setup -q
%patch -p0

%build
gettextize --copy --force
LDFLAGS="-s" ; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS TODO ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/*

%config(noreplace) %verify(not size mtime md5) %{_datadir}/gtoprc

%{_datadir}/applnk/Utilities/gtop.desktop
