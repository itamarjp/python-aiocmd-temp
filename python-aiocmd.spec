%global pypi_name aiocmd

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        2%{?dist}
Summary:        Coroutine-based CLI generator using prompt_toolkit

License:        MIT
URL:            http://github.com/KimiNewt/aiocmd
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/KimiNewt/aiocmd/master/LICENSE
BuildArch:      noarch

%description
Coroutine-based CLI generator using prompt_toolkit, similarly to the built-in
cmd module.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Coroutine-based CLI generator using prompt_toolkit, similarly to the built-in
cmd module.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora
