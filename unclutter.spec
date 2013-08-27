Summary:	Removes idle cursor image from screen
Name:		unclutter
Version:	8
Release:	1
License:	Public Domain
Group:		X11/Applications
Source0:	http://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.Z
# Source0-md5:	83d7a6498b69078f869378f801b6a84b
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unclutter removes the cursor image from the screen so that it does
not obstruct the area you are looking at after it has not moved for
a given time. It does not do this if the cursor is in the root
window or a button is down. It tries to ignore jitter (small
movements due to noise) if you have a mouse that twitches.

%prep
%setup -qn %{name}

%build
%{__make} \
	CC="%{__cc}"			\
	CCOPTIONS="%{rpmcflags}"	\
	LDOPTIONS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install unclutter $RPM_BUILD_ROOT%{_bindir}
install unclutter.man $RPM_BUILD_ROOT%{_mandir}/man1/unclutter.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/unclutter.1*

