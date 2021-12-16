%global debug_package %{nil}

####

Name: neo
Summary: Simulates the digital rain from "The Matrix" (cmatrix clone with 32-bit color and Unicode support).
Version: 0.6
Release: 1%{?dist}
License: GPLv3
Source0: https://github.com/st3w/neo/releases/download/v%{version}/neo-%{version}.tar.gz
URL: https://github.com/st3w/neo

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: ncurses-devel

%description
%{summary}

%prep
%setup -q
%configure

%build
%set_build_flags
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%license COPYING
%doc doc/NEWS
%{_mandir}/man6/%{name}.6*

%changelog
* Thu Dec 16 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6-1
- initial packaging