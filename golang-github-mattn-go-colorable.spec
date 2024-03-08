%global debug_package %{nil}

# Run tests in check section
%bcond_without check

# https://github.com/mattn/go-colorable
%global goipath		github.com/mattn/go-colorable
%global forgeurl	https://github.com/mattn/go-colorable
Version:		0.1.13

%gometa

Summary:	Colorable writer for windows in Go.
Name:		golang-github-mattn-go-colorable

Release:	1
Source0:	https://github.com/mattn/go-colorable/archive/v%{version}/go-colorable-%{version}.tar.gz
URL:		https://github.com/mattn/go-colorable
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	golang(github.com/mattn/go-isatty)

%description
Colorable writer for windows.

For example, most of logger packages doesn't show
colors on windows. (I know we can do it with ansicon.
This package is possible to handle escape sequence
for ansi color on windows.

%files
%license LICENSE
%doc README.md
%{_bindir}/colorable

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc _example README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-colorable-%{version}

%build
%gobuildroot
for cmd in $(ls -1 cmd) ; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done


%check
%if %{with check}
%gochecks
%endif

