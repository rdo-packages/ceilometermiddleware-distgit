%global pypi_name ceilometermiddleware

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-ceilometermiddleware
Version:	0.4.1
Release:	1%{?dist}
Summary:        OpenStack Telemetry middleware for generating metrics
License:	ASL 2.0
URL:		http://github.com/openstack/ceilometermiddleware
Source0:	https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
# Required for running tests
BuildRequires:  python-mock
BuildRequires:  python-babel >= 1.3
BuildRequires:  python-oslo-config >= 2.3.0
BuildRequires:  python-oslo-context >= 0.2.0
BuildRequires:  python-oslo-utils >= 2.0.0
BuildRequires:  python-oslo-messaging >= 1.17.1
BuildRequires:  python-oslotest
BuildRequires:  python-pycadf >= 1.1.0
BuildRequires:  python-six >= 1.9.0
BuildRequires:  python-testscenarios

Requires:       python-babel >= 1.3
Requires:       python-oslo-config >= 2.3.0
Requires:       python-oslo-context >= 0.2.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-oslo-messaging >= 1.17.1
Requires:       python-pbr
Requires:       python-pycadf >= 1.1.0
Requires:       python-six >= 1.9.0

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
* Tue May 23 2017 Alfredo Moralejo <amoralej@redhat.com> 0.4.1-1
- Update to 0.4.1

* Wed Mar 23 2016 Haikel Guemar <hguemar@fedoraproject.org> 0.4.0-
- Update to 0.4.0



