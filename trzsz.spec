Name:           trzsz
Version:        1.2.0
Release:        1
Summary:        Simple file transfer tools, similar to lrzsz (rz/sz), and compatible with tmux.

License:        MIT
URL:            https://trzsz.github.io/go
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang-bin >= 1.25

%undefine _debugsource_packages
%define debug_package %{nil}

%description
trzsz ( trz / tsz ) is a simple file transfer tools, similar to lrzsz ( rz / sz ), and compatible with tmux.

%prep
%autosetup -n %{name}-go-%{version}

%build
export CGO_ENABLED=0
export GOPROXY=direct
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
* Sat Mar 21 2026 Lonny Wong <lonnywong@qq.com> - 1.2.0-1
- Update to trzsz v1.2.0

* Sat Nov 15 2025 Lonny Wong <lonnywong@qq.com> - 1.1.8-1
- Initial RPM spec for trzsz
