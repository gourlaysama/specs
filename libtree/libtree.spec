%global debug_package %{nil}

####

Name: libtree
Summary: ldd as a tree with an option to bundle dependencies into a single folder.
Version: 3.0.1
Release: 1%{?dist}
License: MIT
Source0: https://github.com/haampie/libtree/archive/v%{version}.tar.gz
URL: https://github.com/haampie/libtree

BuildRequires: make
BuildRequires: gcc

%description
%{summary}

%prep
%setup -q

%build
%set_build_flags
%make_build

%install
install -Dpsm755 %{name} %{buildroot}%{_bindir}/%{name}

%if 0%{?el7}
mkdir -p %{buildroot}%{_mandir}/man1
%endif
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 doc/%{name}.1


%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md CHANGELOG.md
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Dec 15 2021 Antoine Gourlay <antoine@gourlay.fr> - 3.0.1-1
- libtree 3.0.1

* Wed Dec 15 2021 Antoine Gourlay <antoine@gourlay.fr> - 3.0.0-2
- build for epel/centos-stream

* Tue Dec 14 2021 Antoine Gourlay <antoine@gourlay.fr> - 3.0.0-1
- libtree 3.0.0

* Mon Dec 06 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.0-1
- initial packaging
