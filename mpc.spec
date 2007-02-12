Summary:	Comandline client for mpd
Summary(pl.UTF-8):   Klient wiersza poleceń dla mpd
Name:		mpc
Version:	0.12.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://musicpd.org/uploads/files/%{name}-%{version}.tar.bz2
# Source0-md5:	9ec03c5f3d136a9a58ef665dfb100e52
URL:		http://www.musicpd.org/mpc.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comandline client for mpd daemon.

%description -l pl.UTF-8
Klient dla daemona mpd obsługiwany z wiersza poleceń.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man1/*
