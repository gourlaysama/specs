%global debug_package %{nil}

####

Name: btop
Summary: Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
Version: 1.2.13
Release: 1%{?dist}
License: ASL 2.0
Source0: https://github.com/aristocratos/btop/archive/v%{version}.tar.gz
URL: https://github.com/aristocratos/btop

BuildRequires: make
%if 0%{?el8}
BuildRequires: gcc-toolset-11-gcc-c++
BuildRequires: gcc-toolset-11-annobin-plugin-gcc
%else
BuildRequires: gcc-c++
%endif
BuildRequires: desktop-file-utils

%description
%{summary}

%prep
%setup -q

%build
%if 0%{?el8}
PATH="/opt/rh/gcc-toolset-11/root/usr/bin/:$PATH"
%endif

%set_build_flags
%make_build

%install
install -Dpsm755 bin/%{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}/themes
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/themes themes/*

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -Dpm0644 Img/icon.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dpm0644 Img/icon.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/btop.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Wed Nov 09 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.13-1
- btop 1.2.13

* Wed Oct 12 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.12-1
- btop 1.2.12

* Mon Sep 05 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.9-1
- btop 1.2.9

* Thu Jun 30 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.8-1
- btop 1.2.8

* Mon May 30 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.7-1
- btop 1.2.7
- package desktop file and icon

* Wed Apr 13 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.6-1
- btop 1.2.6

* Sun Mar 06 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.5-1
- btop 1.2.5

* Sun Feb 27 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.4-1
- btop 1.2.4

* Tue Feb 15 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.3-1
- btop 1.2.3

* Mon Feb 14 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.2-2
- add CentOS-Stream 8 support

* Sun Feb 13 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.2-1
- btop 1.2.2

* Fri Feb 11 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.1-1
- btop 1.2.1

* Sun Jan 16 2022 Antoine Gourlay <antoine@gourlay.fr> - 1.2.0-1
- initial packaging