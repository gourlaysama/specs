
Name: neo
Summary: Simulates the digital rain from "The Matrix".
Version: 0.6
Release: 2%{?dist}
License: GPLv3
Source0: https://github.com/st3w/neo/releases/download/v%{version}/neo-%{version}.tar.gz
URL: https://github.com/st3w/neo

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: ncurses-devel

%description
Neo recreates the digital rain effect from "The Matrix"  (cmatrix clone with
32-bit color and Unicode support). Streams of random characters will endlessly
scroll down your terminal screen.

%prep
%setup -q

%build
%set_build_flags
%configure
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%license COPYING
%doc doc/NEWS
%{_mandir}/man6/%{name}.6*

%changelog
* Fri Dec 17 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6-2
- improve packaging

* Thu Dec 16 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6-1
- initial packaging