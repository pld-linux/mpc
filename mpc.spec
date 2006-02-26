Summary:	Comandline client for mpd
Summary(pl):	Klient wiersza poleceñ dla mpd
Name:		mpc
Version:	0.11.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://mercury.chem.pitt.edu/~shank/%{name}-%{version}.tar.gz
# Source0-md5:	c8411da7936662312cf9483f3490e285
URL:		http://www.musicpd.org/mpc.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comandline client for mpd daemon.

%description -l pl
Klient dla daemona mpd obs³ugiwany z wiersza poleceñ.

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
