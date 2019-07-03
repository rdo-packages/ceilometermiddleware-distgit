%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name ceilometermiddleware
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

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

%if 0%{?with_python3}
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
Requires:       python3-oslo-utils >= 2.0.0
Requires:       python3-oslo-messaging >= 5.2.0
Requires:       python3-pbr
Requires:       python3-pycadf >= 1.1.0
Requires:       python3-six >= 1.9.0
Requires:       python3-keystoneauth1 >= 2.18.0
Requires:       python3-keystoneclient >= 3.8.0

%description -n python3-%{pypi_name}
This library provides middleware modules designed to enable metric and event data 
generation to be consumed by Ceilometer.
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%check
%{__python2} setup.py test ||:
%if 0%{?with_python3}
%{__python3} setup.py test ||:
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info
%endif

%changelog


