%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

####

Name: ht-rust
Summary: Yet another HTTPie clone in Rust
Version: 0.4.0
Release: 3%{?dist}
License: MIT
Source0: https://github.com/ducaale/ht/archive/v%{version}.tar.gz
URL: https://github.com/ducaale/ht

BuildRequires: rust >= 1.46.0
BuildRequires: cargo

%description
%{summary}

%prep
%setup -q -n ht-%{version}

%build
env RUSTFLAGS="%{rust_flags}" CARGO_PROFILE_RELEASE_LTO="true" cargo build --release

%install
install -Dps -m755 target/release/ht   %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
* Tue Feb 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-3
- rename ht to ht-rust to avoid conflict

* Tue Feb 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-2
- build with lto

* Sat Feb 6 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-1
- Initial package
