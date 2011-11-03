%define tarname	WebOb
%define name	python-webob
%define version 1.1.1
%define release %mkrel 1

Summary:	WSGI request and response object for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/W/%{tarname}/%{tarname}-%{version}.zip
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/webob/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%__rm -rf %{buildroot}
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)

