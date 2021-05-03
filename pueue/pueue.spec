%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

####

Name: pueue
Summary: A command-line task management tool for sequential and parallel execution of long-running tasks.
Version: 0.12.2
Release: 1%{?dist}
License: MIT
Source0: https://github.com/Nukesor/pueue/archive/v%{version}.tar.gz
URL: https://github.com/Nukesor/pueue

BuildRequires: rust >= 1.51.0
BuildRequires: cargo
BuildRequires: systemd-rpm-macros

%description
%{summary}

%prep
%setup -q

%build
env RUSTFLAGS="%{rust_flags}" cargo build --release

%install
install -Dps -m755 target/release/pueue   %{buildroot}%{_bindir}/pueue
install -Dps -m755 target/release/pueued   %{buildroot}%{_bindir}/pueued
install -Dpm0644 -t %{buildroot}%{_userunitdir}/ utils/pueued.service
mkdir -p utils/completions
target/release/%{name} completions bash utils/completions/
target/release/%{name} completions fish utils/completions/
target/release/%{name} completions zsh utils/completions/
install -Dpm0644 -T ./utils/completions/pueue.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/pueue
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  ./utils/completions/pueue.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  ./utils/completions/_pueue

%files
%{_bindir}/pueue
%{_bindir}/pueued
%license LICENSE
%doc README.md CHANGELOG.md
%{_userunitdir}/pueued.service
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/pueue
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/pueue.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_pueue

%post
%systemd_user_post pueued.service

%preun
%systemd_user_preun pueued.service

%changelog
* Tue Apr 20 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.12.2-1
- rust 1.51
- pueue 0.12.2

* Tue Mar 16 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.12.1-1
- inital package
