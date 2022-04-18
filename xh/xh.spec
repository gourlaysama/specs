%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

%global debug_package %{nil}

####

Name: xh
Summary: Yet another HTTPie clone in Rust
Version: 0.16.0
Release: 2%{?dist}
License: MIT
Source0: https://github.com/ducaale/xh/archive/v%{version}.tar.gz
URL: https://github.com/ducaale/xh

Patch0: 0001-ppc64-fully-disable-rusttls-in-addition-to-native-tl.patch

Provides: ht-rust%{?_isa} = %{version}-%{release}
Obsoletes: ht-rust <= 0.6.0-2

BuildRequires: rust >= 1.46.0
BuildRequires: cargo
BuildRequires: pkgconfig(openssl)

%description
%{summary}

%prep
%setup -q -n xh-%{version}
%ifarch ppc64le
%patch0 -p1
%endif

%build
RUSTFLAGS="%{rust_flags}" CARGO_PROFILE_RELEASE_LTO="true" cargo build --release --features native-tls

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
ln -s xh %{buildroot}%{_bindir}/xhs

%if 0%{?el7}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_mandir}/man1
%endif

install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions/ \
  completions/xh.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  completions/xh.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  completions/_xh
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  doc/xh.1

%files
%{_bindir}/%{name}
%{_bindir}/xhs
%license LICENSE
%doc README.md CHANGELOG.md
%{_mandir}/man1/xh.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/xh.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/xh.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_xh

%changelog
* Mon Apr 18 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.16.0-2
- fix ppc64le build

* Sun Apr 17 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.16.0-1
- xh 0.16.0

* Fri Jan 28 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.15.0-1
- xh v0.15.0

* Fri Dec 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.14.1-4
- enable ppc64le build: do not build rusttls backend

* Mon Nov 29 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.14.1-3
- use native TLS stack (link to openssl)

* Mon Nov 29 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.14.1-2
- add /usr/bin/xhs symlink to xh

* Sat Nov 27 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.14.1-1
- xh v0.14.1

* Mon Nov 15 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.14.0-1
- xh v0.14.0

* Thu Sep 16 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.13.0-1
- xh v0.13.0

* Fri Aug 06 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.12.0-1
- xh v0.12.0

* Mon Jul 26 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.11.0-1
- xh v0.11.0

* Mon May 17 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.10.0-1
- xh 0.10.0

* Thu Mar 25 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.9.2-1
- xh 0.9.2

* Wed Mar 17 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.9.1-1
- xh 0.9.1

* Tue Mar 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.9.0-1
- xh 0.9.0

* Wed Mar 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.8.1-1
- xh 0.8.1

* Sun Feb 28 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.8.0-1
- xh 0.8.0

* Fri Feb 12 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.7.0-1
- rename ht-rust to xh
- xh 0.7.0

* Tue Feb 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.0-1
- ht 0.6.0

* Tue Feb 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-3
- rename ht to ht-rust to avoid conflict

* Tue Feb 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-2
- build with lto

* Sat Feb 6 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-1
- Initial package
