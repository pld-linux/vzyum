# vzyum: stripped-down patched yum packaged for OpenVZ
#
# Changes:
# * Docs, cron scripts, configs, yum-arch removed.
# * Option --vps added.
# * Installed to /usr/share/vzyum

Summary:	RPM installer/updater used by OpenVZ template tools
Summary(pl.UTF-8):	Narzędzie do instalacji i uaktualniania RPM-ów używane przez narzędzia OpenVZ
Name:		vzyum
Version:	2.4.0
Release:	11
License:	GPL
Group:		Base
Source0:	http://linux.duke.edu/projects/yum/download/2.4/yum-%{version}.tar.gz
# Source0-md5:	c19a471ef5f72ddca3f100a60a07d1b3
Patch0:		http://download.openvz.org/template/utils/vzyum/2.4.0-11/src/yum-2.4.0-altpath.swsoft.patch
Patch1:		http://download.openvz.org/template/utils/vzyum/2.4.0-11/src/yum-2.4.0-pluginpath.swsoft.patch
Patch2:		http://download.openvz.org/template/utils/vzyum/2.4.0-11/src/yum-2.4.0-vps.swsoft.patch
URL:		http://linux.duke.edu/yum/
BuildRequires:	gettext
BuildRequires:	python
Requires:	/sbin/chkconfig
Requires:	/sbin/service
Requires:	coreutils
Requires:	libxml2-python
Requires:	python
Requires:	python-cElementTree
Requires:	python-sqlite
Requires:	urlgrabber
Obsoletes:	yum-phoebe
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/vzyum
%define		_sysconfdir	%{_prefix}/etc

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded
automatically prompting the user as necessary.

%description -l pl.UTF-8
Yum to narzędzie potrafiące sprawdzać istnienie i automatycznie ściągać
oraz instalować uaktualnione pakiety RPM. Potrzebne zależności są
ściągane automatycznie po potwierdzeniu użytkownika.

%prep
%setup -q -n yum-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pluginconf.d,%{_prefix}/plugins}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%dir %{_sysconfdir}
%{_sysconfdir}/pluginconf.d
%dir %{_bindir}
%attr(755,root,root) %{_bindir}/yum
%dir %{_prefix}/yum-cli
%{_prefix}/yum-cli/*
%{_prefix}/lib
%{_prefix}/plugins
