%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name ceilometermiddleware

Name:           python-%{pypi_name}
Version:	1.4.0
Release:	1%{?dist}
Summary:        OpenStack Telemetry middleware for generating metrics
License:	ASL 2.0
URL:		http://github.com/openstack/%{pypi_name}
Source0:	https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library provides middleware modules designed to enable metric and event data 
generation to be consumed by Ceilometer.

%package -n python2-%{pypi_name}
Summary:        OpenStack Telemetry middleware for generating metrics
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:	python2-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
# Required for running tests
BuildRequires:  python2-mock
BuildRequires:  python2-oslo-config >= 2:3.9.0
BuildRequires:  python2-oslo-utils >= 2.0.0
BuildRequires:  python2-oslo-messaging >= 5.2.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pycadf >= 1.1.0
BuildRequires:  python2-six >= 1.9.0
BuildRequires:  python2-testscenarios

Requires:       python2-oslo-config >= 2:3.9.0
Requires:       python2-oslo-utils >= 2.0.0
Requires:       python2-oslo-messaging >= 5.2.0
Requires:       python2-pbr
Requires:       python2-pycadf >= 1.1.0
Requires:       python2-six >= 1.9.0
Requires:       python2-keystoneauth1 >= 2.18.0
Requires:       python2-keystoneclient >= 3.8.0

%description -n python2-%{pypi_name}
This library provides middleware modules designed to enable metric and event data 
generation to be consumed by Ceilometer.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} setup.py test ||:

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}*.egg-info


%changelog
* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 1.4.0-1
- Update to 1.4.0



