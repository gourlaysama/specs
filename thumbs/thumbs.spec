%global rust_flags -Ccodegen-units=1 -Clink-arg=-Wl,-z,relro,-z,now --cap-lints warn

%global debug_package %{nil}

####

Name:           thumbs
Summary:        A command line tool to manage the cached thumbnails of files.
Version:        0.4.5
Release:        1%{?dist}
License:        ASL 2.0
Source0:        https://github.com/gourlaysama/thumbs/archive/v%{version}.tar.gz
URL:            https://github.com/gourlaysama/thumbs

BuildRequires:  rust >= 1.57.0
BuildRequires:  cargo

# No pandoc there yet...
%if 0%{?rhel} < 9
BuildRequires: /usr/bin/pandoc
%endif

%description
%{summary}

%package nautilus
Summary:        Thumbs extention for nautilus
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       nautilus-python
%if 0%{?rhel} > 7
Supplements:    (thumbs and nautilus)
%endif
	
%description nautilus
%{summary}

%prep
%setup -q

%build
RUSTFLAGS="%{rust_flags}" BUILD_ID="%{release}" cargo build --release

%if 0%{?rhel} < 9
pandoc -s --to man doc/thumbs.1.md -o thumbs.1
%endif

%install
install -Dpsm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%if 0%{?rhel} < 9
mkdir -p %{buildroot}%{_mandir}/man1/
%endif

%if 0%{?rhel} < 9
install -Dpvm0644 -t %{buildroot}%{_mandir}/man1/ %{name}.1
%endif

%if 0%{?rhel} < 8
mkdir -p %{buildroot}%{_datadir}/nautilus-python/extensions/
%endif

install -Dpm0644 -t %{buildroot}%{_datadir}/nautilus-python/extensions/ extra/nautilus/%{name}-nautilus.py

%files
%{_bindir}/%{name}
%license LICENSE NOTICE
%doc README.md CHANGELOG.md
%if 0%{?rhel} < 9
%{_mandir}/man1/%{name}.1*
%endif

%files nautilus
%{_datadir}/nautilus-python/extensions/%{name}-nautilus.py*

%changelog
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
