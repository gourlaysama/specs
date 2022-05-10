%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

####

Name: dust
Summary: A more intuitive version of du in rust.
Version: 0.8.0
Release: 1%{?dist}
License: ASL 2.0
Source0: https://github.com/bootandy/dust/archive/v%{version}.tar.gz
URL: https://github.com/bootandy/dust

BuildRequires: rust
BuildRequires: cargo

%description
du + rust = dust. Like du but more intuitive.

%prep
%setup -q

%build
RUSTFLAGS="%{rust_flags}" cargo build --release

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md


%changelog
* Tue May 10 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.8.0-1
- initial packaging
