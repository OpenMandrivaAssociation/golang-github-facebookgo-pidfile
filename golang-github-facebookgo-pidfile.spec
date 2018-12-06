# Run tests in check section
%bcond_without check

%global goipath         github.com/facebookgo/pidfile
%global commit          f242e2999868dcd267a2b86e49ce1f9cf9e15b16

%global common_description %{expand:
Package pidfile manages pid files.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Pid files management
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/facebookgo/atomicfile)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license license
%doc readme.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf242e29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180517gitf242e29
- First package for Fedora

