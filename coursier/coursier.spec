# this needs to be updated for a new release
%global coursier_commit d5ad55d1dcb025084ba9bd994ea47ceae0608a8f

# dependency versions
%global directories_jvm_commit 006ca7ff804ca48f692d59a7fce8599f8a1eadfc
%global windows_ansi_version 0.0.3
%global ammonite_version 2.3.8

%ifarch aarch64
# only version available on arm64 in jabba
%define graalvm_version 21.1.0
%else
%define graalvm_version 20.1.0
%endif

%global debug_package %{nil}

####

Name: coursier
Summary: Pure Scala Artifact Fetching
Version: 2.0.16
Release: 4%{?dist}
License: ASL 2.0
URL: https://github.com/coursier/coursier
Source0: https://github.com/coursier/coursier/archive/refs/tags/v%{version}.tar.gz
Source1: https://github.com/dirs-dev/directories-jvm/archive/%{directories_jvm_commit}.tar.gz
Source2: https://github.com/alexarchambault/windows-ansi/archive/refs/tags/v%{windows_ansi_version}.tar.gz

Patch0: 0200-disable-proguard.patch
Patch1: 0201-stick-mima-to-fixed-version-for-2.0.x.patch

%if 0%{?rhel}
BuildRequires: java-11-openjdk-devel
%else
BuildRequires: java-devel >= 1:11
%endif

BuildRequires: ncurses
BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: zlib-devel

%description
%{summary}

%prep
%setup -q -b0
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

# the commit hash needs to be embedded in properties
sed -i 's/Seq("git", "rev-parse", "HEAD").!!.trim/"%{git_commit}"/' project/Settings.scala
# needed to fool the build; we don't actually need the tests
mkdir -p modules/tests/metadata/https
mkdir -p modules/tests/handmade-metadata/data

%build
mkdir -p out/completions

./sbt 'set publishArtifact in (ThisBuild, Compile, packageDoc) := false' 'set version in ThisBuild := "%{version}"' jvmProjects/publishLocal cli/pack

./modules/cli/target/pack/bin/coursier java --jvm graalvm-ce-java11:%{graalvm_version} -version
COURSIER_BIN_DIR="$(pwd)" ./modules/cli/target/pack/bin/coursier install ammonite:%{ammonite_version}
 
export JAVA_HOME="$(./modules/cli/target/pack/bin/coursier java-home --jvm graalvm-ce-java11:%{graalvm_version})"
./amm launcher.sc generateNativeImage --version "%{version}" --output out/cs

./modules/cli/target/pack/bin/coursier --completions zsh > out/completions/_cs

%install
install -Dpsm755 out/cs %{buildroot}%{_bindir}/cs

%if 0%{?el7}
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%endif
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions ./out/completions/_cs

%files
%{_bindir}/cs
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cs

%changelog
* Fri Nov 26 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-4
- EPEL/CentOS-Stream support

* Wed Nov 24 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-3
- arm64 build support

* Sun May 09 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-2
- properly use tarballs instead of git clone
- use a locally built coursier launcher

* Fri Apr 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-1
- initial packaging
