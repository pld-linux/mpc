Summary:	Comandline client for mpd
Summary(pl.UTF-8):	Klient wiersza poleceń dla mpd
Name:		mpc
Version:	0.35
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://www.musicpd.org/download/mpc/0/%{name}-%{version}.tar.xz
# Source0-md5:	f609716926f9d59b189025f8c7a24dd0
URL:		http://www.musicpd.org
BuildRequires:	libmpdclient-devel >= 2.18
BuildRequires:	meson >= 0.47
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libmpdclient >= 2.18
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
BuildArch:	noarch

%description -n bash-completion-%{name}
This package provides bash-completion for mpc.

%prep
%setup -q

%build
%meson build \
	-Ddocumentation=enabled
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

install -d $RPM_BUILD_ROOT/etc/bash_completion.d
cp -p contrib/mpc-completion.bash $RPM_BUILD_ROOT/etc/bash_completion.d

rm -r $RPM_BUILD_ROOT%{_docdir}/mpc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.rst NEWS build/doc/html
%doc contrib/mpd-m3u-handler.sh contrib/mpd-pls-handler.sh
%attr(755,root,root) %{_bindir}/mpc
%{_mandir}/man1/mpc.1*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/*
