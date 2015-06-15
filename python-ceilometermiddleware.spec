%global pypi_name ceilometermiddleware

Name:           python-ceilometermiddleware
Version:	0.1.0
Release:	1%{?dist}
Summary:        OpenStack Telemetry middleware for generating metrics
License:	ASL 2.0
URL:		http://github.com/openstack/ceilometermiddleware
Source0:	https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python-setuptools
BuildRequires:  python2-devel

Requires:       python-babel >= 1.3
Requires:       python-oslo-utils
Requires:       python-oslo-messaging >= 1.4.0
Requires:       python-oslo-context >= 0.1.0
Requires:       python-oslo-messaging
Requires:       python-oslo-config
Requires:       python-pbr
Requires:       python-pycadf >= 0.6.0
Requires:       python-six >= 1.7.0

%description
This library provides middleware modules designed to enable metric and event data 
generation to be consumed by Ceilometer.

%prep
%setup -q -n %{pypi_name}-%{version}

%build

%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%{python2_sitelib}/ceilometermiddleware
%{python2_sitelib}/ceilometermiddleware*.egg-info
%doc README.rst LICENSE


%changelog
* Fri Jun 12 2015 Pradeep Kilambi <pkilambi@redhat.com> 0.1.0-1
- initial package release


