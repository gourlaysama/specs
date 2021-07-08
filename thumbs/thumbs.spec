%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

%global debug_package %{nil}

####

Name: thumbs
Summary: A command line tool to manage the cached thumbnails of files.
Version: 0.2.1
Release: 1%{?dist}
License: ASL 2.0
Source0: https://github.com/gourlaysama/thumbs/archive/v%{version}.tar.gz
URL: https://github.com/gourlaysama/thumbs

BuildRequires: rust >= 1.52.0
BuildRequires: cargo

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
%license LICENSE NOTICE
%doc README.md CHANGELOG.md

%changelog
* Wed Jul 07 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.2.1-1
- thumbs 0.2.1