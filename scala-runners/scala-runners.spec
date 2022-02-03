%global debug_package %{nil}

%global snapshot dc1ad83
%global snapshot_date 20220118

####

Name: scala-runners
Summary: Coursier-based runners for scala, scalac, scalap and scaladoc
Version: 0
Release: 0.2.%{snapshot_date}git%{snapshot}%{?dist}
License: ASL 2.0
URL: https://github.com/dwijnand/scala-runners
Source0: https://github.com/dwijnand/scala-runners/archive/%{snapshot}.tar.gz

Requires: coursier
Requires: /usr/bin/jq
Requires: /usr/bin/hub

%description
%{summary}

%prep
%setup -q -c -n %{name}-main
mv %{name}-%{snapshot}*/* .
rm -R %{name}-%{snapshot}*

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
* Thu Feb 03 2022 Antoine Gourlay <antoine@gourlay.fr> - 0-0.2.20220118gitdc1ad83
- update to latest snapshot (2022-01-18)

* Fri Nov 12 2021 Antoine Gourlay <antoine@gourlay.fr> - 0-0.2.20211110git140cc65
- update to latest snapshot (2021-11-10)

* Tue Oct 26 2021 Antoine Gourlay <antoine@gourlay.fr> - 0-0.2.20211026git949a867
- update to latest snapshot

* Fri Sep 17 2021 Antoine Gourlay <antoine@gourlay.fr> - 0-0.1.120210728git9bf096c
- initial packaging
