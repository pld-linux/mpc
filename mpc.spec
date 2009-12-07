Summary:	Comandline client for mpd
Summary(pl.UTF-8):	Klient wiersza poleceń dla mpd
Name:		mpc
Version:	0.19
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/musicpd/mpc-%{version}.tar.bz2
# Source0-md5:	9ab2967d9ec719b06a86f3b4121be654
URL:		http://www.musicpd.org/mpc.shtml
BuildRequires:	libmpdclient-devel
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
%doc AUTHORS README NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man1/*
