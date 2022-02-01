%global debug_package %{nil}
%global goipath github.com/muesli/duf
%global godocs README.md
%global golicenses LICENSE

####

Version: 0.8.0
%gometa

Name: duf
Summary: Disk Usage/Free Utility - a better 'df' alternative
Release: 1%{?dist}
License: MIT
Source0: %{gosource}
URL: %{gourl}

BuildRequires: git

%description
%{summary}
%gopkg

%prep
%setup -q
go mod vendor
%goprep -k -e

%build
export LDFLAGS="-X main.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/duf %{goipath}

%install
%gopkginstall
install -dpvm 0755                     %{buildroot}%{_bindir}
install -pvsm 0755 %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpvm 0644 -t %{buildroot}%{_mandir}/man1/ %{name}.1

%files
%{_bindir}/%{name}
%license %{golicenses}
%doc %{godocs}
%{_mandir}/man1/%{name}.1*

%gopkgfiles

%changelog
* Tue Feb 01 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.8.0-1
- duf 0.8.0

* Sat Jan 08 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.7.0-1
- initial packaging
