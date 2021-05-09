%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

%global debug_package %{nil}

####

Name: xh
Summary: Yet another HTTPie clone in Rust
Version: 0.9.2
Release: 1%{?dist}
License: MIT
Source0: https://github.com/ducaale/xh/archive/v%{version}.tar.gz
URL: https://github.com/ducaale/xh

Provides: ht-rust%{?_isa} = %{version}-%{release}
Obsoletes: ht-rust <= 0.6.0-2

BuildRequires: rust >= 1.46.0
BuildRequires: cargo

%description
%{summary}

%prep
%setup -q -n xh-%{version}

%build
RUSTFLAGS="%{rust_flags}" CARGO_PROFILE_RELEASE_LTO="true" cargo build --release

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
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
