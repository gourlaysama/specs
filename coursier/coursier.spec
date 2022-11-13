# dependency versions
%global directories_jvm_commit 7acadf2ab9a4ce306d840d652cdb77fade11b94b
%global windows_ansi_version 0.0.3

%global debug_package %{nil}

####

Name: coursier
Summary: Pure Scala Artifact Fetching
Version: 2.1.0~RC1
Release: 1%{?dist}
License: ASL 2.0
URL: https://github.com/coursier/coursier
Source0: https://github.com/coursier/coursier/archive/refs/tags/v2.1.0-M7.tar.gz
Source1: https://github.com/dirs-dev/directories-jvm/archive/%{directories_jvm_commit}.tar.gz
Source2: https://github.com/alexarchambault/windows-ansi/archive/refs/tags/v%{windows_ansi_version}.tar.gz

Patch0: 0001-no-git.patch
Patch1: 0002-remove-use-of-sun.misc-package.patch

BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: ncurses
BuildRequires: gcc-c++
BuildRequires: zlib-devel

%description
%{summary}

%prep
%setup -q -b0 -n coursier-2.1.0-M7
%patch0 -p1
%patch1 -p1

cd modules

tar -xf '%{SOURCE1}'
rm -d directories
mv directories-* directories
tar -xf '%{SOURCE2}'
rm -d windows-ansi
mv windows-ansi-* windows-ansi

cd ..

# needed to fool the build; we don't actually need the tests
mkdir -p modules/tests/metadata/https
mkdir -p modules/tests/handmade-metadata/data

%build
mkdir -p out/completions
mkdir utils

export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8
./mill -i copyJarLaunchers

mv artifacts/* utils/
ln -sfT coursier utils/cs
export PATH="utils:$PATH"
eval "$(cs java --env --jvm 11 --jvm-index https://github.com/coursier/jvm-index/raw/master/index.json)"

./mill -i copyLauncher artifacts/
gunzip artifacts/*.gz

utils/cs --completions zsh > out/completions/_cs

%install
install -Dpsm755 artifacts/cs-* %{buildroot}%{_bindir}/cs

%if 0%{?el7}
install -dpm0755 %{buildroot}%{_datadir}/zsh/site-functions
%endif

install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions ./out/completions/_cs

%files
%{_bindir}/cs
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cs

%changelog
* Sun Nov 13 2022 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~RC1-1
- coursier 2.1.0-RC1

* Mon Sep 19 2022 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M7-1
- coursier 2.1.0~M7

* Sat Jul 02 2022 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M6-2
- fix build reporting wrong version

* Wed May 18 2022 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M6-1
- coursier 2.1.0~M6

* Mon Feb 07 2022 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M5-1
- coursier 2.1.0-M5

* Thu Feb 03 2022 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M4-2
- fix epel-7 build

* Tue Feb 01 2022 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M4-1
- update to mill build
- coursier 2.1.0-M4 (minimum version needed to fix scala-runners)

* Fri Dec 03 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-5
- workaround OutOfMemoryError: give GraalVM more memory

* Fri Nov 26 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-4
- EPEL/CentOS-Stream support

* Wed Nov 24 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-3
- arm64 build support

* Sun May 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-2
- properly use tarballs instead of git clone
- use a locally built coursier launcher

* Fri Apr 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-1
- initial packaging
