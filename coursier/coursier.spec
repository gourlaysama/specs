# coursier build requires git, sadly
%global git_url https://github.com/coursier/coursier.git
# for mima tests to work
%global clone_base v2.0.0-RC6-7

%global debug_package %{nil}

####

Name: coursier
Summary: Pure Scala Artifact Fetching
Version: 2.0.16
Release: 1%{?dist}
License: ASL 2.0
Source0: https://github.com/coursier/coursier/releases/download/v%{version}/coursier
URL: https://github.com/coursier/coursier

BuildRequires: java-devel >= 1:11
BuildRequires: ncurses
BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: zlib-devel

%description
%{summary}

%prep
%setup -c -T
git clone --shallow-exclude=%{clone_base} --branch "v%{version}" --recurse-submodules --shallow-submodules "%{git_url}" .
mkdir -p ../cs_bin
cp '%{SOURCE0}' ../cs_bin/cs
chmod +x ../cs_bin/cs

%build
mkdir -p out/completions
export COURSIER_BIN_DIR="$(pwd)/../cs_bin"
export PATH="$PATH:$COURSIER_BIN_DIR"
cs java --jvm graalvm-ce-java11:20.1.0 -version
cs install sbt-launcher:1.2.22 ammonite:2.3.8
cs --completions zsh > out/completions/_cs
sbt 'set publishArtifact in (ThisBuild, Compile, packageDoc) := false' 'set version in ThisBuild := "%{version}"' jvmProjects/publishLocal
export JAVA_HOME="$(cs java-home --jvm graalvm-ce-java11:20.1.0)"
amm launcher.sc generateNativeImage --version "%{version}" --output out/cs

%install
install -Dpsm755 out/cs %{buildroot}%{_bindir}/cs
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions ./out/completions/_cs

%files
%{_bindir}/cs
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cs

%changelog
* Fri Apr 02 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.16-1
- initial packaging
