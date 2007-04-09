Summary:	struts-legacy - classes removed from the core Struts distribution
Summary(pl.UTF-8):	struts-legacy - klasy usunięte z głównej dystrybucji Struts
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
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
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

%description -l pl.UTF-8
Pakiet struts-legacy zawiera klasy, które zostały usunięte z głównej
dystrybucji Struts, ale mogą nadal być interesujące. Klasy te są
uznane za "stabilne", ale *nie* są aktywnie utrzymywane (stąd nazwa
"legacy").

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}a -

%prep
%setup -q -n struts-legacy-%{version}-src

%build
required_jars="commons-logging"
export CLASSPATH=$(/usr/bin/build-classpath $required_jars)
%ant dist \
	-Djdk.version=1.4 \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
for a in dist/*.jar; do
	jar=${a##*/}
	cp -a dist/$jar $RPM_BUILD_ROOT%{_javadir}/${jar%%.jar}-%{version}.jar
	ln -s ${jar%%.jar}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$jar
done

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc dist/LICENSE.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
