%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

####

Name: dcamctl
Summary: A command line tool to use an android device connected over USB as a webcam.
Version: 0.1.0
Release: 1%{?dist}
License: MIT or ASL 2.0
Source0: https://github.com/gourlaysama/dcamctl/archive/v%{version}.tar.gz
URL: https://github.com/gourlaysama/dcamctl

BuildRequires: rust >= 1.50.0
BuildRequires: cargo
BuildRequires: pkgconfig(gstreamer-1.0)

Requires: /usr/bin/pactl
Requires: /usr/bin/pacmd
Requires: /usr/bin/adb

%description
%{summary}

%prep
%setup -q

%build
env RUSTFLAGS="%{rust_flags}" cargo build --release

%install
install -Dps -m755 target/release/%{name}   %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE-APACHE LICENSE-MIT
%doc README.md CHANGELOG.md

%changelog
* Wed Apr 14 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.1.0-1
- dcamctl 0.1.0