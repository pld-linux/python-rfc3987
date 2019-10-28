#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

Summary:	Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
Summary(pl.UTF-8):	Analiza i sprawdzanie poprawności URI (RFC 3986) oraz IRI (RFC 3987)
Name:		python-rfc3987
Version:	1.3.7
Release:	3
License:	GPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/rfc3987/
Source0:	https://files.pythonhosted.org/packages/source/r/rfc3987/rfc3987-%{version}.tar.gz
# Source0-md5:	aa108c7590902fe609c036864ecb7f84
URL:		https://pypi.python.org/pypi/rfc3987/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides regular expressions according to RFC 3986
"Uniform Resource Identifier (URI): Generic Syntax"
<http://tools.ietf.org/html/rfc3986> and RFC 3987 "Internationalized
Resource Identifiers (IRIs)" <http://tools.ietf.org/html/rfc3987>, and
utilities for composition and relative resolution of references.

%description -l pl.UTF-8
Ten moduł zawiera wyrażenia regularne zgodne z RFC 3986 ("Uniform
Resource Identifier (URI): Generic Syntax")
<http://tools.ietf.org/html/rfc3986> oraz RFC 3987 "Internationalized
Resource Identifiers (IRIs)" <http://tools.ietf.org/html/rfc3987>, a
także narzędzia do składania i względnego rozwiązywania odnośników.

%package -n python3-rfc3987
Summary:	Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
Summary(pl.UTF-8):	Analiza i sprawdzanie poprawności URI (RFC 3986) oraz IRI (RFC 3987)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-rfc3987
This module provides regular expressions according to RFC 3986
"Uniform Resource Identifier (URI): Generic Syntax"
<http://tools.ietf.org/html/rfc3986> and RFC 3987 "Internationalized
Resource Identifiers (IRIs)" <http://tools.ietf.org/html/rfc3987>, and
utilities for composition and relative resolution of references.

%description -n python3-rfc3987 -l pl.UTF-8
Ten moduł zawiera wyrażenia regularne zgodne z RFC 3986 ("Uniform
Resource Identifier (URI): Generic Syntax")
<http://tools.ietf.org/html/rfc3986> oraz RFC 3987 "Internationalized
Resource Identifiers (IRIs)" <http://tools.ietf.org/html/rfc3987>, a
także narzędzia do składania i względnego rozwiązywania odnośników.

%prep
%setup -q -n rfc3987-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/rfc3987.py[co]
%{py_sitescriptdir}/rfc3987-%{version}-py*.egg-info

%files -n python3-rfc3987
%defattr(644,root,root,755)
%doc README.txt
%{py3_sitescriptdir}/rfc3987.py
%{py3_sitescriptdir}/__pycache__/rfc3987.cpython-*.py[co]
%{py3_sitescriptdir}/rfc3987-%{version}-py*.egg-info
