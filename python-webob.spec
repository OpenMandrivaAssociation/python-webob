%define tarname	WebOb

Summary:	WSGI request and response object for Python
Name:		python-webob
Version:	1.2.3
Release:	1
Source0:	http://pypi.python.org/packages/source/W/WebOb/WebOb-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/webob/
BuildArch:	noarch
Requires:	python-pkg-resources
BuildRequires:	python-setuptools

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%prep
%setup -q -n %{tarname}-%{version}

%install
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST



%changelog
* Thu Nov 03 2011 Lev Givon <lev@mandriva.org> 1.1.1-1mdv2012.0
+ Revision: 716247
- Update to 1.1.1.

* Thu Mar 31 2011 Lev Givon <lev@mandriva.org> 1.0.6-1
+ Revision: 649443
- import python-webob


