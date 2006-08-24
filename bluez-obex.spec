
%define		snapshot	20051017

Summary:	Bluetooth OBEX utilities
Summary(pl):	Narzêdzia Bluetooth OBEX
Name:		bluez-obex
Version:	0.1.%{snapshot}
Release:	1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://gruby.cs.net.pl/~adasi/%{name}-%{version}.tar.gz
# Source0-md5:	194478cd895da5ec991a9c470f64cc59
URL:		http://www.bluez.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 2.21
BuildRequires:	libtool
BuildRequires:	openobex-devel >= 1.0.1-2
Requires:	bluez-libs >= 2.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluetooth OBEX utils.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%description -l pl
Narzêdzia Bluetooth OBEX.

Znak towarowy BLUETOOTH nale¿y do Bluetooth SIG, Inc. w USA.

%prep
%setup -q

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
