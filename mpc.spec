Summary:	Comandline client for mpd
Summary(pl.UTF-8):	Klient wiersza poleceń dla mpd
Name:		mpc
Version:	0.23
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.musicpd.org/download/mpc/0/%{name}-%{version}.tar.bz2
# Source0-md5:	2b2c093e80b37fc5717caf319986c52b
Patch0:		%{name}-missing_macros.patch
URL:		http://www.musicpd.org
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libmpdclient-devel >= 2.2
BuildRequires:	pkgconfig
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

%description -n bash-completion-%{name}
This package provides bash-completion for mpc.

%prep
%setup -q
%patch0 -p1

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
