%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

%global debug_package %{nil}

####

Name: biosctl
Summary: A cli tool to manage Dell BIOS/EFI settings on Linux 5.11+.
Version: 0.3.2
Release: 2%{?dist}
License: MIT
Source0: https://github.com/gourlaysama/biosctl/archive/v%{version}.tar.gz
URL: https://github.com/gourlaysama/biosctl

BuildRequires: rust >= 1.52.0
BuildRequires: cargo

%description
%{summary}

%prep
%setup -q

%build
RUSTFLAGS="%{rust_flags}" BUILD_ID="%{release}" cargo build --release

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Fri Nov 05 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.2-2
- rebuild with correct build id

* Fri Oct 29 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.2-1
- biosctl 0.3.2

* Wed Apr 21 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.1-1
- biosctl 0.3.1

* Mon Mar 22 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.0-1
- biosctl 0.3.0 - initial package
