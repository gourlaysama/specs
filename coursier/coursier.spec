# dependency versions
%global directories_jvm_commit 7acadf2ab9a4ce306d840d652cdb77fade11b94b
%global windows_ansi_version 0.0.3

%global debug_package %{nil}

####

Name: coursier
Summary: Pure Scala Artifact Fetching
Version: 2.1.0~M1.1
Release: 1%{?dist}
License: ASL 2.0
URL: https://github.com/coursier/coursier
Source0: https://github.com/coursier/coursier/archive/refs/tags/v2.1.0-M1-1.tar.gz
Source1: https://github.com/dirs-dev/directories-jvm/archive/%{directories_jvm_commit}.tar.gz
Source2: https://github.com/alexarchambault/windows-ansi/archive/refs/tags/v%{windows_ansi_version}.tar.gz

Patch0: 0001-no-git.patch

BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: ncurses
BuildRequires: gcc-c++
BuildRequires: zlib-devel

%description
%{summary}

%prep
%setup -q -b0 -n coursier-2.1.0-M1-1
%patch0 -p1

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
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions ./out/completions/_cs

%files
%{_bindir}/cs
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cs

%changelog
* Wed Nov 24 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M1-1
- coursier 2.1.0-M1.1

* Tue Nov 23 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.1.0~M1-1
- coursier 2.1.0-M1

* Fri Oct 29 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-169.g194ebc55c.1
- update to mill build

* Sun May 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-2
- properly use tarballs instead of git clone
- use a locally built coursier launcher

* Fri Apr 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-1
- initial packaging
