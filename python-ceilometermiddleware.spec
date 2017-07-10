%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name ceilometermiddleware

Name:           python-ceilometermiddleware
Version:	XXX
Release:	XXX
Summary:        OpenStack Telemetry middleware for generating metrics
License:	ASL 2.0
URL:		http://github.com/openstack/ceilometermiddleware
Source0:	https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
# Required for running tests
BuildRequires:  python-mock
BuildRequires:  python-babel >= 1.3
BuildRequires:  python-oslo-config >= 2:3.9.0
BuildRequires:  python-oslo-context >= 0.2.0
BuildRequires:  python-oslo-utils >= 2.0.0
BuildRequires:  python-oslo-messaging >= 5.2.0
BuildRequires:  python-oslotest
BuildRequires:  python-pycadf >= 1.1.0
BuildRequires:  python-six >= 1.9.0
BuildRequires:  python-testscenarios

Requires:       python-babel >= 1.3
Requires:       python-oslo-config >= 2:3.9.0
Requires:       python-oslo-context >= 0.2.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-oslo-messaging >= 5.2.0
Requires:       python-pbr
Requires:       python-pycadf >= 1.1.0
Requires:       python-six >= 1.9.0
Requires:       python-keystoneauth1 >= 2.18.0
Requires:       python-keystoneclient >= 3.8.0

%description
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

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/ceilometermiddleware
%{python2_sitelib}/ceilometermiddleware*.egg-info


%changelog


