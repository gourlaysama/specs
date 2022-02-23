%global debug_package %{nil}

####

Name: libtree-ldd
Summary: ldd as a tree with an option to bundle dependencies into a single folder.
Version: 3.0.3~copr
Release: 1%{?dist}
License: MIT
Source0: https://github.com/haampie/libtree/archive/v3.0.3.tar.gz
URL: https://github.com/haampie/libtree

Provides: libtree = 3.0.3-1
Obsoletes: libtree < 3.0.3-1

BuildRequires: make
BuildRequires: gcc

%description
%{summary}

%prep
%setup -q -n libtree-3.0.3

%build
%set_build_flags
%make_build

%install
install -Dpsm755 libtree %{buildroot}%{_bindir}/libtree

%if 0%{?el7}
mkdir -p %{buildroot}%{_mandir}/man1
%endif
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 doc/libtree.1


%files
%{_bindir}/libtree
%license LICENSE
%doc README.md CHANGELOG.md
%{_mandir}/man1/libtree.1*

%changelog
* Wed Feb 23 2022 Antoine Gourlay <antoine@gourlay.fr> - 3.0.3~copr-1
- libtree 3.0.3
- deprecate COPR package: will be upgraded to libtree-ldd from fedora-updates

* Fri Jan 14 2022 Antoine Gourlay <antoine@gourlay.fr> - 3.0.2-1
- libtree 3.0.2

* Wed Dec 15 2021 Antoine Gourlay <antoine@gourlay.fr> - 3.0.1-1
- libtree 3.0.1

* Wed Dec 15 2021 Antoine Gourlay <antoine@gourlay.fr> - 3.0.0-2
- build for epel/centos-stream

* Tue Dec 14 2021 Antoine Gourlay <antoine@gourlay.fr> - 3.0.0-1
- libtree 3.0.0

* Mon Dec 06 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.0-1
- initial packaging
