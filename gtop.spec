Summary:	The GNOME system monitor
Summary(pl):	Monitor systemu dla GNOME
Name:		gtop
Version:	1.0.13
Release:	5
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtop/1.0/%{name}-%{version}.tar.gz
Patch0:		%{name}-gcc296.patch
Patch1:		%{name}-nodrag.patch
Patch2:		%{name}-use_AM_GNU_GETTEXT.patch
Patch3:		%{name}-configure.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libgtop-devel >= 1.0.6
BuildRequires:	libtool
BuildRequires:	zlib-devel
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/System

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO ChangeLog
%attr(755,root,root) %{_bindir}/*

%config(noreplace) %verify(not size mtime md5) %{_datadir}/gtoprc

%{_applnkdir}/System/gtop.desktop
%{_pixmapsdir}/*
