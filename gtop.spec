Summary:	The GNOME system monitor
Summary(pl.UTF-8):	Monitor systemu dla GNOME
Name:		gtop
Version:	1.0.13
Release:	5
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtop/1.0/%{name}-%{version}.tar.gz
# Source0-md5:	4580801db3c87784b25f46a5bf1f5aba
Patch0:		%{name}-gcc296.patch
Patch1:		%{name}-nodrag.patch
Patch2:		%{name}-use_AM_GNU_GETTEXT.patch
Patch3:		%{name}-configure.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libgtop-devel >= 1.0.6
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package will install the GNOME system monitor gtop, which shows
memory graphs and processes.

%description -l pl.UTF-8
Ten pakiet zawiera gtop - monitor systemu dla GNOME, wyświetlający w
postaci graficznej informacje na temat pamięci i procesów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
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

%config(noreplace) %verify(not md5 mtime size) %{_datadir}/gtoprc

%{_applnkdir}/System/gtop.desktop
%{_pixmapsdir}/*
