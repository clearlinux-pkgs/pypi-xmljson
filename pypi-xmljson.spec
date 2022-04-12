#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-xmljson
Version  : 0.2.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/e8/6f/d9f109ba19be510fd3098bcb72143c67ca6743cedb48ac75aef05ddfe960/xmljson-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/6f/d9f109ba19be510fd3098bcb72143c67ca6743cedb48ac75aef05ddfe960/xmljson-0.2.1.tar.gz
Summary  : Converts XML into JSON/Python dicts/arrays and vice-versa.
Group    : Development/Tools
License  : MIT
Requires: pypi-xmljson-bin = %{version}-%{release}
Requires: pypi-xmljson-license = %{version}-%{release}
Requires: pypi-xmljson-python = %{version}-%{release}
Requires: pypi-xmljson-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi-lxml

%description
xmljson
        ===============================

%package bin
Summary: bin components for the pypi-xmljson package.
Group: Binaries
Requires: pypi-xmljson-license = %{version}-%{release}

%description bin
bin components for the pypi-xmljson package.


%package license
Summary: license components for the pypi-xmljson package.
Group: Default

%description license
license components for the pypi-xmljson package.


%package python
Summary: python components for the pypi-xmljson package.
Group: Default
Requires: pypi-xmljson-python3 = %{version}-%{release}

%description python
python components for the pypi-xmljson package.


%package python3
Summary: python3 components for the pypi-xmljson package.
Group: Default
Requires: python3-core
Provides: pypi(xmljson)

%description python3
python3 components for the pypi-xmljson package.


%prep
%setup -q -n xmljson-0.2.1
cd %{_builddir}/xmljson-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649796764
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xmljson
cp %{_builddir}/xmljson-0.2.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-xmljson/e4450853b9d2e70fca35febb7767291178b4159d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xml2json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-xmljson/e4450853b9d2e70fca35febb7767291178b4159d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*