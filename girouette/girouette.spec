%global next_version 0.4.0
%global baserelease 2
%global pre_release 0

%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

%if 0%{pre_release}
%define pkg_release 0.%{baserelease}.dev%{?dist}
%else
%define pkg_release %{baserelease}%{?dist}
%endif

####

Name: girouette
Summary: A command line tool that displays the current weather in the terminal.
Version: %{next_version}
Release: %{pkg_release}
License: MIT or ASL 2.0
%if 0%{pre_release}
Source0: %{name}-%{next_version}-dev.tar.gz
%else
Source0: https://github.com/gourlaysama/girouette/archive/v%{version}.tar.gz
%endif
URL: https://github.com/gourlaysama/girouette

BuildRequires: rust >= 1.48.0
BuildRequires: cargo
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(openssl)

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
* Tue Feb 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-2
- fix rust MSRV: 1.48.0

* Tue Feb 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-1
- girouette 0.4.0

* Fri Jan 22 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-0.1
- Initial package