%define module mox

Name:           python-%{module}
Version:        0.5.3
Release:        %mkrel 1
Url:            http://code.google.com/p/pymox/
Summary:        Mock object framework
License:        Apache License, Version 2.0
Group:          Development/Python
Source:         %{module}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildArch:      noarch

%description
Mox is a mock object framework for Python based on the
Java mock object framework EasyMock.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

