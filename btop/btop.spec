%global debug_package %{nil}

####

Name: btop
Summary: Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
Version: 1.2.1
Release: 1%{?dist}
License: ASL 2.0
Source0: https://github.com/aristocratos/btop/archive/v%{version}.tar.gz
URL: https://github.com/aristocratos/btop

BuildRequires: make
BuildRequires: gcc-c++

%description
%{summary}

%prep
%setup -q

%build
%set_build_flags
%make_build

%install
install -Dpsm755 bin/%{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}/themes
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/themes themes/*


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Fri Feb 11 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.1-1
- btop 1.2.1

* Sun Jan 16 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.0-1
- initial packaging