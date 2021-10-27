%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

%global debug_package %{nil}

####

Name: dcamctl
Summary: A command line tool to use an android device connected over USB as a webcam.
Version: 0.4.2
Release: 1%{?dist}
License: ASL 2.0
Source0: https://github.com/gourlaysama/dcamctl/archive/v%{version}.tar.gz
URL: https://github.com/gourlaysama/dcamctl

BuildRequires: rust >= 1.51.0
BuildRequires: cargo
BuildRequires: pkgconfig(gstreamer-1.0) >= 1.10
BuildRequires: pkgconfig(gstreamer-video-1.0) >= 1.10

Requires: /usr/bin/pactl
Requires: /usr/bin/adb

%description
%{summary}

%prep
%setup -q

%build
RUSTFLAGS="%{rust_flags}" cargo build --release

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Wed Oct 27 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.2-1
- dcamctl 0.4.2

* Wed Sep 08 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.1-2
- fix license file inclusion

* Wed Sep 08 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.1-1
- dcamctl 0.4.1

* Mon Sep 06 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-1
- dcamctl 0.4.0

* Mon Aug 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.1-1
- dcamctl 0.3.1

* Fri Jul 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.0-1
- dcamctl 0.3.0

* Tue Jun 15 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.2.1-1
- dcamctl 0.2.1

* Wed May 26 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.2.0-1
- dcamctl 0.2.0
- drop dependency on pacmd

* Fri Apr 23 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.1.1-1
- dcamctl 0.1.1

* Wed Apr 14 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.1.0-1
- dcamctl 0.1.0