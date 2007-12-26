Summary:	Monitor for icecram
Summary(pl.UTF-8):	Monitor dla icecream
Name:		icemon-kde3
Version:	01
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.suse.com/pub/projects/icecream/%{name}.tar.bz2
# Source0-md5:	c761b9a96007d5adc95b624d0e909ca5
URL:		http://en.opensuse.org/Icecream
BuildRequires:	icecream-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitor for icecram.

%description -l pl.UTF-8
Monitor dla icecream.

%prep
%setup -q -n %{name}

%build
%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_kdedocdir}/en/icemon

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/icemon/* $RPM_BUILD_ROOT%{_kdedocdir}/en/icemon/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/icemon
%dir %{_datadir}/apps/icemon
%dir %{_datadir}/apps/icemon/pics
%lang(en) %dir %{_kdedocdir}/en/icemon
%lang(en) %{_kdedocdir}/en/icemon
%{_datadir}/apps/icemon/icemonui.rc
%{_datadir}/apps/icemon/pics/icemonnode.png
%{_datadir}/apps/kicker/applets/icemonapplet.desktop
%{_desktopdir}/kde/icemon.desktop
