Summary:	Comandline client for mpd
Summary(pl.UTF-8):	Klient wiersza poleceń dla mpd
Name:		mpc
Version:	0.14
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/musicpd/mpc-0.14.tar.bz2
# Source0-md5:	f4218602342cf322872a41dfe0cc72e1
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
