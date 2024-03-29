#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-scm-publish-plugin
Version  : 1.1
Release  : 3
URL      : https://github.com/apache/maven-scm-publish-plugin/archive/maven-scm-publish-plugin-1.1.tar.gz
Source0  : https://github.com/apache/maven-scm-publish-plugin/archive/maven-scm-publish-plugin-1.1.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-scm-publish-plugin/1.1/maven-scm-publish-plugin-1.1.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-scm-publish-plugin/1.1/maven-scm-publish-plugin-1.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-scm-publish-plugin-data = %{version}-%{release}

%description
This file content is not the same as reference svn.
Will check svn checkin.

%package data
Summary: data components for the mvn-maven-scm-publish-plugin package.
Group: Data

%description data
data components for the mvn-maven-scm-publish-plugin package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-scm-publish-plugin/1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-scm-publish-plugin/1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-scm-publish-plugin/1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-scm-publish-plugin/1.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-scm-publish-plugin/1.1/maven-scm-publish-plugin-1.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-scm-publish-plugin/1.1/maven-scm-publish-plugin-1.1.pom
