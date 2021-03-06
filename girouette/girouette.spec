%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

####

%global debug_package %{nil}

####

Name: girouette
Summary: A command line tool that displays the current weather in the terminal.
Version: 0.7.4
Release: 1%{?dist}
License: MIT or ASL 2.0
Source0: https://github.com/gourlaysama/girouette/archive/v%{version}.tar.gz
URL: https://github.com/gourlaysama/girouette

BuildRequires: rust >= 1.57.0
BuildRequires: cargo
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(openssl)

# No pandoc there yet...
%if 0%{?rhel} < 9
BuildRequires: /usr/bin/pandoc
%endif

%description
%{summary}

%prep
%setup -q

%build
RUSTFLAGS="%{rust_flags}" BUILD_ID="%{release}" cargo build --release

%if 0%{?rhel} < 9
pandoc -s --to man doc/girouette.1.md -o girouette.1
%endif

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 -T target/release/build/%{name}-*/out/girouette.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/girouette

%if 0%{?rhel}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions

%if 0%{?rhel} < 9
mkdir -p %{buildroot}%{_mandir}/man1/
%endif
%endif

install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  target/release/build/%{name}-*/out/girouette.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  target/release/build/%{name}-*/out/_girouette

%if 0%{?rhel} < 9
install -Dpvm0644 -t %{buildroot}%{_mandir}/man1/ %{name}.1
%endif

%files
%{_bindir}/%{name}
%license LICENSE-APACHE LICENSE-MIT
%doc README.md CHANGELOG.md
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/girouette
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/girouette.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_girouette

%if 0%{?rhel} < 9
%{_mandir}/man1/%{name}.1*
%endif

%changelog
* Wed Jul 20 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.7.4-1
- girouette 0.7.4

* Sat Jun 11 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.7.3-1
- girouette 0.7.3

* Fri May 13 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.7.2-2
- fix EPEL/CentOS build
- disable man page generation on CentOS Stream 9

* Fri May 13 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.7.2-1
- girouette 0.7.2
- package man page

* Wed May 04 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.7.1-1
- girouette 0.7.1

* Tue Mar 08 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.7.0-1
- girouette 0.7.0

* Thu Dec 30 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.7-1
- girouette 0.6.7

* Wed Dec 15 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.6-1
- girouette 0.6.6

* Fri Nov 26 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.5-1
- girouette 0.6.5

* Wed Nov 17 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.4-1
- girouette 0.6.4

* Mon Oct 25 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.3-1
- girouette 0.6.3

* Fri Sep 10 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.2-1
- girouette 0.6.2

* Fri Sep 10 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.1-1
- girouette 0.6.1

* Fri Sep 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.0-2
- build for epel/centos-stream

* Fri Sep 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.6.0-1
- girouette 0.6.0

* Fri Jul 23 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.5.2-1
- girouette 0.5.2

* Thu May 20 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.5.1-1
- girouette 0.5.1

* Mon Mar 29 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.5.0-1
- girouette 0.5.0

* Wed Feb 10 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.3-1
- girouette 0.4.3

* Tue Feb 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.2-1
- girouette 0.4.2

* Wed Feb 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.1-3
- fix bash completion path

* Wed Feb 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.1-2
- fix epel build: fix typo

* Wed Feb 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.1-1
- girouette 0.4.1

* Tue Feb 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-2
- fix rust MSRV: 1.48.0

* Tue Feb 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-1
- girouette 0.4.0

* Fri Jan 22 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-0.1
- Initial package
