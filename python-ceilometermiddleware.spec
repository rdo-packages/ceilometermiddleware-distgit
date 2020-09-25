
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name ceilometermiddleware

Name:           python-%{pypi_name}
Version:	2.1.0
Release:	1%{?dist}
Summary:        OpenStack Telemetry middleware for generating metrics
License:	ASL 2.0
URL:		http://github.com/openstack/%{pypi_name}
Source0:	https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library provides middleware modules designed to enable metric and event data
generation to be consumed by Ceilometer.

%package -n python3-%{pypi_name}
Summary:        OpenStack Telemetry middleware for generating metrics
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:	python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# Required for running tests
BuildRequires:  python3-mock
BuildRequires:  python3-oslo-config >= 2:3.9.0
BuildRequires:  python3-oslo-utils >= 2.0.0
BuildRequires:  python3-oslo-messaging >= 5.2.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pycadf >= 1.1.0
BuildRequires:  python3-six >= 1.9.0
BuildRequires:  python3-testscenarios

Requires:       python3-oslo-config >= 2:3.9.0
Requires:       python3-oslo-utils
Requires:       python3-oslo-messaging >= 5.2.0
Requires:       python3-pbr
Requires:       python3-pycadf >= 1.1.0
Requires:       python3-six >= 1.9.0
Requires:       python3-keystoneauth1 >= 2.18.0
Requires:       python3-keystoneclient >= 3.8.0

%description -n python3-%{pypi_name}
This library provides middleware modules designed to enable metric and event data
generation to be consumed by Ceilometer.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{py3_build}

%install
%{py3_install}

%check
python3 setup.py test ||:

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Fri Sep 25 2020 RDO <dev@lists.rdoproject.org> 2.1.0-1
- Update to 2.1.0

