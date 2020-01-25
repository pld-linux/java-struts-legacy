%bcond_without  javadoc         # don't build javadoc

%define         srcname         struts-legacy
Summary:	struts-legacy - classes removed from the core Struts distribution
Summary(pl.UTF-8):	struts-legacy - klasy usunięte z głównej dystrybucji Struts
Name:		java-struts-legacy
Version:	1.0
Release:	0.1
License:	Apache v1.1
Source0:	http://archive.apache.org/dist/jakarta/struts/struts-legacy/struts-legacy-%{version}-src.tar.gz
# Source0-md5:	805b7f3e787c1469f57fed9f5eebc3a1
Group:		Libraries/Java
URL:		http://struts.apache.org/
BuildRequires:	ant >= 1.6
BuildRequires:	java(jdbc-stdext) >= 2.0-2
BuildRequires:	java(servlet)
BuildRequires:	java-commons-beanutils
BuildRequires:	java-commons-collections
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java(jdbc-stdext) >= 2.0
Requires:	java(servlet)
Requires:	java-commons-beanutils
Requires:	java-commons-collections
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
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%prep
%setup -q -n struts-legacy-%{version}-src

%build
required_jars="commons-logging"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH
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
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost
symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc dist/LICENSE.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
