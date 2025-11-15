Name:           trzsz
Version:        1.1.8
Release:        1
Summary:        Simple file transfer tools, similar to lrzsz (rz/sz), and compatible with tmux.

License:        MIT
URL:            https://github.com/trzsz/trzsz-go
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang >= 1.20
BuildRequires:  git

%if 0%{?rhel} >= 8 && 0%{?rhel} <= 9 || 0%{?mageia}
%undefine _debugsource_packages
%endif

%if 0%{?openEuler} || 0%{?mageia} == 8
%define debug_package %{nil}
%endif

%description
trzsz ( trz / tsz ) is a simple file transfer tools, similar to lrzsz ( rz / sz ), and compatible with tmux.

%prep
%autosetup -n %{name}-go-%{version}

%build
%if 0%{?mageia} == 8
export GOPROXY=direct
%endif
go build -o %{_builddir}/bin/trz ./cmd/trz
go build -o %{_builddir}/bin/tsz ./cmd/tsz
go build -o %{_builddir}/bin/trzsz ./cmd/trzsz

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/bin/trz %{buildroot}%{_bindir}/trz
install -m 0755 %{_builddir}/bin/tsz %{buildroot}%{_bindir}/tsz
install -m 0755 %{_builddir}/bin/trzsz %{buildroot}%{_bindir}/trzsz

%files
%{_bindir}/trz
%{_bindir}/tsz
%{_bindir}/trzsz

%changelog
* Sat Nov 15 2025 Lonny Wong <lonnywong@qq.com> - 1.1.8-1
- Initial RPM spec for trzsz
