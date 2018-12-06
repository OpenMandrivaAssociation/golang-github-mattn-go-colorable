# https://github.com/mattn/go-colorable
%global goipath         github.com/mattn/go-colorable
%global commit          efa589957cd060542a26d2dd7832fd6a6c6c3ade

%gometa

Name:           golang-github-mattn-go-colorable
Version:        0.0.9
Release:        0.1%{?dist}
Summary:        Colorable writer for windows
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/mattn/go-isatty)

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Nov 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.9-0.1.20181102gitefa5899
- Bump to commit efa589957cd060542a26d2dd7832fd6a6c6c3ade

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20170816gitad5389d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170816gitad5389d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Matthias Runge <mrunge@redhat.com> - 0.0.5-20170816gitad5389d
- add requirement to golang-github-mattn-go-isatty (rhbz#1494218)

* Thu Sep 21 2017 Matthias Runge <mrunge@redaht.com> - 0-0.4.20170816gitad5389d
- fix import path (rhbz#1493760)

* Mon Sep 18 2017 Matthias Runge <mrunge@redhat.com> - 0-0.3.20170816gitad5389d
- update to latest commit
- own /usr/share/gocode/src/gopkg.in/mattn/go-colorable.v1/cmd/
- feedback from initial review (rhbz#1376412)

* Thu Apr 7 2016 Matthias Runge <mrunge@redhat.com> - 0.1git-9cbef7c
- initial package

