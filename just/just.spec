%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

####

Name: just
Summary: Just a command runner.
Version: 0.9.2
Release: 1%{?dist}
License: CC0
Source0: https://github.com/casey/just/archive/v%{version}.tar.gz
URL: https://github.com/casey/just

BuildRequires: rust >= 1.51.0
BuildRequires: cargo

%description
%{summary}

%prep
%setup -q

%build
env RUSTFLAGS="%{rust_flags}" cargo build --release

%install
install -Dps -m755 target/release/%{name}   %{buildroot}%{_bindir}/%{name}
install -Dpm0644 -T completions/just.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/just
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  completions/just.fish
install -Dpm0644 -T completions/just.zsh \
  %{buildroot}%{_datadir}/zsh/site-functions/_just
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  man/just.1

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.adoc CHANGELOG.md GRAMMAR.md
%{_mandir}/man1/just.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/just
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/just.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_just

%changelog
* Sun May 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.9.2-1
- just 0.9.2
- Initial package
