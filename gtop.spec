# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      3
%define prefix   /usr

Summary: The GNOME system monitor.
Name: gtop
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/System
Source: ftp://ftp.gnome.org/pub/gtop-%{ver}.tar.gz
BuildRoot: /var/tmp/gtop-%{PACKAGE_VERSION}-root
Obsoletes: gnome
URL: http://www.gnome.org
Docdir: %{prefix}/doc

Patch: gtop-desktop.patch

%description
GNOME is the GNU Network Object Model Environment. This powerful
environment is both easy to use and easy to configure.

This package will install the GNOME system monitor gtop,
which shows memory graphs and processes.

%prep
%setup

%patch -p1

%build
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

#
# hack or else desktop entry not installed
#
make prefix=$RPM_BUILD_ROOT%{prefix} INSTALL-data-local

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/not strip/ { print $1 }'`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/share/gtoprc
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/apps/*
