%global debug_package %{nil}

####

Name: libtree
Summary: ldd as a tree with an option to bundle dependencies into a single folder.
Version: 2.0.0
Release: 1%{?dist}
# MIT: libtree, BSD: termcolor
License: MIT and BSD
Source0: https://github.com/haampie/libtree/archive/v%{version}.tar.gz
Source1: https://github.com/ikalnytskyi/termcolor/archive/67eb0aa.tar.gz
URL: https://github.com/haampie/libtree

Patch0: 0001-build-with-unpackaged-dependencies.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(cxxopts)
BuildRequires: elfio-static

Provides: bundled(termcolor) = 2.0.0

%description
%{summary}

%prep
%setup -q
%patch0 -p1

mkdir bundled
cd bundled
tar -xf %{SOURCE1}
mv termcolor-* termcolor
cp termcolor/LICENSE ../LICENSE-TERMCOLOR

%build
%cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="bundled/"
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE LICENSE-TERMCOLOR
%doc README.md

%changelog
* Mon Dec 06 2021 Antoine Gourlay <antoine@gourlay.fr> - 2.0.0-1
- initial packaging