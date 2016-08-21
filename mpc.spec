Summary:	Comandline client for mpd
Summary(pl.UTF-8):	Klient wiersza poleceń dla mpd
Name:		mpc
Version:	0.28
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.musicpd.org/download/mpc/0/%{name}-%{version}.tar.xz
# Source0-md5:	e9cfaf17ab1db54dba4df4b08aa0db3f
URL:		http://www.musicpd.org
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libmpdclient-devel >= 2.9
BuildRequires:	pkgconfig
Requires:	libmpdclient >= 2.9
Suggests:	bash-completion-%{name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comandline client for mpd daemon.

%description -l pl.UTF-8
Klient dla daemona mpd obsługiwany z wiersza poleceń.

%package -n bash-completion-%{name}
Summary:	bash-completion for mpc
Group:		Applications/Shells
Requires:	bash-completion
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-%{name}
This package provides bash-completion for mpc.

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
	doc_DATA= \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/bash_completion.d
cp -p doc/mpc-completion.bash $RPM_BUILD_ROOT/etc/bash_completion.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%doc doc/mpd-m3u-handler.sh doc/mpd-pls-handler.sh doc/mppledit
%attr(755,root,root) %{_bindir}/mpc
%{_mandir}/man1/mpc.1*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/*
