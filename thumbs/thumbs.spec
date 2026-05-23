%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

%global debug_package %{nil}

####

Name:           thumbs
Summary:        A command line tool to manage the cached thumbnails of files.
Version:        0.5.2
Release:        2%{?dist}
License:        ASL 2.0
Source0:        https://github.com/gourlaysama/thumbs/archive/v%{version}.tar.gz
URL:            https://github.com/gourlaysama/thumbs

BuildRequires:  rust >= 1.87.0
BuildRequires:  cargo
BuildRequires:  systemd-rpm-macros
BuildRequires:  /usr/bin/pandoc

%description
%{summary}

%package nautilus
Summary:        Thumbs extension for nautilus
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       nautilus-python
Supplements:    (%{name} and nautilus)
	
%description nautilus
%{summary}

%prep
%setup -q

%build
RUSTFLAGS="%{rust_flags}" BUILD_ID="%{release}" cargo build --release
cargo xtask gen-completions
pandoc -s --to man doc/%{name}.1.md -o "%{name}.1"

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 -T extra/complete/%{name}.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%if 0%{?rhel}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_mandir}/man1/
%endif


install -Dpvm0644 -t %{buildroot}%{_mandir}/man1/ %{name}.1
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  extra/complete/%{name}.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  extra/complete/_%{name}

mkdir -p %{buildroot}%{_datadir}/nautilus-python/extensions/

install -Dpm0644 -t %{buildroot}%{_datadir}/nautilus-python/extensions/ extra/nautilus/%{name}-nautilus.py

install -Dpm0644 -t %{buildroot}%{_userunitdir} extra/systemd-user/thumbnail-cleanup.service
install -Dpm0644 -t %{buildroot}%{_userunitdir} extra/systemd-user/thumbnail-cleanup.timer

%files
%{_bindir}/%{name}
%license LICENSE NOTICE
%doc README.md CHANGELOG.md
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/thumbs
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/thumbs.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_thumbs
%{_mandir}/man1/thumbs.1*
%{_userunitdir}/thumbnail-cleanup.service
%{_userunitdir}/thumbnail-cleanup.timer

%files nautilus
%{_datadir}/nautilus-python/extensions/thumbs-nautilus.py*

%post
%systemd_user_post thumbnail-cleanup.service
%systemd_user_post thumbnail-cleanup.timer

%preun
%systemd_user_preun thumbnail-cleanup.service
%systemd_user_preun thumbnail-cleanup.timer

%changelog
* Sat May 23 2026 Antoine Gourlay <antoine@gourlay.fr> - 0.5.2-2
- properly reload thumbnail-cleanup.(timer/service) on (un)install

* Mon May 18 2026 Antoine Gourlay <antoine@gourlay.fr> - 0.5.2-1
- thumbs 0.5.2
- update minimum rust version to 1.87
- add systemd user service & timer (disabled by default)

* Fri Jul 22 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.4.5-2
- package shell completions

* Tue Jul 19 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.4.5-1
- thumbs 0.4.5

* Thu Jun 30 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.4.4-1
- thumbs 0.4.4
- package man page

* Wed Jun 22 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.4.3-1
- thumbs 0.4.3

* Mon May 16 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.4.2-2
- fix EPEL 7 build

* Mon May 16 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.4.2-1
- thumbs 0.4.2

* Tue Mar 22 2022 Antoine Gourlay <antoine@gourlay.fr> - 0.4.0-1
- thumbs 0.4.0

* Fri Nov 05 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.2-2
- rebuild with correct build id

* Fri Nov 05 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.2-1
- thumbs 0.3.2

* Tue Jul 13 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.3.1-1
- thumbs 0.3.1

* Fri Jul 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.2.2-1
- thumbs 0.2.2

* Wed Jul 07 2021 Antoine Gourlay <antoine@gourlay.fr> - 0.2.1-1
- thumbs 0.2.1
