# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name ceilometermiddleware

Name:           python-%{pypi_name}
Version:	XXX
Release:	XXX
Summary:        OpenStack Telemetry middleware for generating metrics
License:	ASL 2.0
URL:		http://github.com/openstack/%{pypi_name}
Source0:	https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library provides middleware modules designed to enable metric and event data
generation to be consumed by Ceilometer.

%package -n python%{pyver}-%{pypi_name}
Summary:        OpenStack Telemetry middleware for generating metrics
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}

BuildRequires:	python%{pyver}-setuptools
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
# Required for running tests
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-oslo-config >= 2:3.9.0
BuildRequires:  python%{pyver}-oslo-utils >= 2.0.0
BuildRequires:  python%{pyver}-oslo-messaging >= 5.2.0
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-pycadf >= 1.1.0
BuildRequires:  python%{pyver}-six >= 1.9.0
BuildRequires:  python%{pyver}-testscenarios

Requires:       python%{pyver}-oslo-config >= 2:3.9.0
Requires:       python%{pyver}-oslo-utils >= 2.0.0
Requires:       python%{pyver}-oslo-messaging >= 5.2.0
Requires:       python%{pyver}-pbr
Requires:       python%{pyver}-pycadf >= 1.1.0
Requires:       python%{pyver}-six >= 1.9.0
Requires:       python%{pyver}-keystoneauth1 >= 2.18.0
Requires:       python%{pyver}-keystoneclient >= 3.8.0

%description -n python%{pyver}-%{pypi_name}
This library provides middleware modules designed to enable metric and event data
generation to be consumed by Ceilometer.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{pyver_bin} setup.py build

%install
%{pyver_install}

%check
%{pyver_bin} setup.py test ||:

%files -n python%{pyver}-%{pypi_name}
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{pypi_name}
%{pyver_sitelib}/%{pypi_name}*.egg-info

%changelog
