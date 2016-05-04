# Created by pyp2rpm-3.0.2
%global pypi_name lazr.uri
%global prettyname lazr-uri

Name:           python-lazr-uri
Version:        1.0.3
Release:        1%{?dist}
Summary:        A self-contained, easily reusable library for parsing, manipulating,

License:        LGPL v3
URL:            https://launchpad.net/lazr.uri
Source0:        https://pypi.python.org/packages/ea/bf/71ad2f5eaf7885d36e3cbd0a87cf3812ad043cf99c9fa6cc6ab4c94ee862/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
..
    This file is part of lazr.uri.

    lazr.uri is free software: you can
redistribute it and/or modify it
    under the terms of the GNU Lesser General
Public License as published by
    the Free Software Foundation, version 3 of
the License.

    lazr.uri is distributed in the hope that it will be useful,
but
    WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY
 ...

%package -n     python2-%{prettyname}
Summary:        A self-contained, easily reusable library for parsing, manipulating,
%{?python_provide:%python_provide python2-%{prettyname}}
 
Requires:       python-setuptools
%description -n python2-%{prettyname}
..
    This file is part of lazr.uri.

    lazr.uri is free software: you can
redistribute it and/or modify it
    under the terms of the GNU Lesser General
Public License as published by
    the Free Software Foundation, version 3 of
the License.

    lazr.uri is distributed in the hope that it will be useful,
but
    WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY
 ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%check
%{__python2} setup.py test

%files -n python2-%{prettyname} 
%doc README.txt src/lazr/uri/README.txt COPYING.txt
# %{python2_sitelib}/lazr.uri_1.0.3_py2.7_nspkg.pth
%{python2_sitelib}/lazr
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Initial package.
