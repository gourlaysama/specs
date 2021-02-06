%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

####

Name: ht
Summary: Yet another HTTPie clone in Rust
Version: 0.4.0
Release: 1%{?dist}
License: MIT
Source0: https://github.com/ducaale/ht/archive/v%{version}.tar.gz
URL: https://github.com/ducaale/ht

BuildRequires: rust >= 1.46.0
BuildRequires: cargo

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
%license LICENSE
%doc README.md

%changelog
* Sat Feb 6 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-1
- Initial package
