%global debug_package %{nil}

%global snapver .120210728git9bf096c

####

Name: scala-runners
Summary: Coursier-based runners for scala, scalac, scalap and scaladoc
Version: 0
Release: 0.1%{?snapver}%{?dist}
License: ASL 2.0
URL: https://github.com/dwijnand/scala-runners
Source0: https://github.com/dwijnand/scala-runners/archive/refs/heads/main.tar.gz

Requires: coursier
Requires: /usr/bin/jq
Requires: /usr/bin/hub

%description
%{summary}

%prep
%setup -q -n %{name}-main

%build

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}/
install -Dpm755 scala-runner %{buildroot}%{_libexecdir}/%{name}/
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libexecdir}/%{name}/scala-runner %{buildroot}%{_bindir}/scala
ln -s %{_libexecdir}/%{name}/scala-runner %{buildroot}%{_bindir}/scalac
ln -s %{_libexecdir}/%{name}/scala-runner %{buildroot}%{_bindir}/scalap
ln -s %{_libexecdir}/%{name}/scala-runner %{buildroot}%{_bindir}/scaladoc

%files
%{_bindir}/scala
%{_bindir}/scalac
%{_bindir}/scaladoc
%{_bindir}/scalap
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/scala-runner
%doc README.md
%license LICENSE NOTICE

%changelog
* Fri Sep 17 2021 Antoine Gourlay <antoine@gourlay.fr> - 0-0.1.120210728git9bf096c
- initial packaging
