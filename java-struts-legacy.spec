Summary:	struts-legacy
Name:		jakarta-struts-legacy
Version:	1.0
Release:	0.1
License:	Apache License
Source0:	http://www.apache.org/dist/jakarta/struts/struts-legacy/struts-legacy-%{version}-src.tar.gz
# Source0-md5:	805b7f3e787c1469f57fed9f5eebc3a1
Group:		Development/Languages/Java
URL:		http://jakarta.apache.org/struts
Requires:	servlet
Requires:	jdbc-stdext >= 2.0
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
BuildRequires:	jakarta-ant >= 1.5
BuildRequires:	jaxp_transform_impl
BuildRequires:	servlet
BuildRequires:	jdbc-stdext >= 2.0-2
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
struts-legacy

%prep
%setup -q -n struts-legacy-%{version}-src

%build
ant -Dcommons-logging.jar=/usr/share/java/commons-logging.jar \
    -Djdk.version=1.4 \
    -Djdbc20ext.jar=/usr/share/java/jdbc-stdext.jar \
    dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
cp dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/docs/api dist/LICENSE.txt
%{_javalibdir}/*.jar
