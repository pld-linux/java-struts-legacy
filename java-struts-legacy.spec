Summary:	struts-legacy - classes removed from the core Struts distribution
Summary(pl):	struts-legacy - klasy usuniête z g³ównej dystrybucji Struts
Name:		jakarta-struts-legacy
Version:	1.0
Release:	0.1
License:	Apache v1.1
Source0:	http://www.apache.org/dist/jakarta/struts/struts-legacy/struts-legacy-%{version}-src.tar.gz
# Source0-md5:	805b7f3e787c1469f57fed9f5eebc3a1
Group:		Development/Languages/Java
URL:		http://struts.apache.org/
BuildRequires:	ant >= 1.6
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
BuildRequires:	jdbc-stdext >= 2.0-2
BuildRequires:	servlet
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
Requires:	jdbc-stdext >= 2.0
Requires:	servlet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The struts-legacy distribution contains classes which have been
removed from the core Struts distribution but may still be of
interest. These classes are considered "stable" but are *not* actively
maintained (hence, the name "legacy").

%description -l pl
Pakiet struts-legacy zawiera klasy, które zosta³y usuniête z g³ównej
dystrybucji Struts, ale mog± nadal byæ interesuj±ce. Klasy te s±
uznane za "stabilne", ale *nie* s± aktywnie utrzymywane (st±d nazwa
"legacy").

%prep
%setup -q -n struts-legacy-%{version}-src

%build
ant dist \
	-Dcommons-logging.jar=%{_datadir}/java/commons-logging.jar \
	-Djdk.version=1.4 \
	-Djdbc20ext.jar=%{_datadir}/java/jdbc-stdext.jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp dist/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/docs/api dist/LICENSE.txt
%{_javadir}/*.jar
