Name:           reprotest
Version:        0.7.16
Release:        2%{?dist}
Summary:        Build packages and check them for reproducibility

License:        GPLv3+
Source0:        https://salsa.debian.org/reproducible-builds/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-rstr
Requires:       diffoscope
Requires:       disorderfs
Requires:       faketime
Requires:       fakeroot
Requires:       glibc-all-langpacks
Requires:       rpm-build

%description
reprotest builds the same source code twice in different environments, and
then checks the binaries produced by each build for differences. If any are
found, then diffoscope (or if unavailable then diff) is used to display them
in detail for later analysis.

It supports different types of environment such as a "null" environment (i.e.
doing the builds directly in /tmp) or various other virtual servers, for
example schroot, ssh, qemu, and several others.

reprotest is developed as part of the "reproducible builds" Debian project.

%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%{_bindir}/reprotest
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Feb 08 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-2
- Update requirements

* Wed Feb 03 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-1
- version 0.7.16

* Mon Jan 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.15-1
- Initial RPM packaging.
