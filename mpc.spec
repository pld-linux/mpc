Summary:	Comandline client for mpd
Summary(pl.UTF-8):	Klient wiersza poleceń dla mpd
Name:		mpc
Version:	0.20
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/musicpd/mpc-%{version}.tar.bz2
# Source0-md5:	24c81ad6afe6099e8d7a6826ef4b7105
URL:		http://www.musicpd.org/mpc.shtml
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libmpdclient-devel >= 2.2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comandline client for mpd daemon.

%description -l pl.UTF-8
Klient dla daemona mpd obsługiwany z wiersza poleceń.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
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
%doc AUTHORS README NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man1/*
