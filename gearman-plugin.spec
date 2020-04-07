Name:       gearman-plugin
Version:    0.3.2
Release:    1%{?dist}
Summary:    A jenkins gearman-plugin-%{name}.hpi
Requires:   jenkins
Group:      Development/Libraries
License:    BSD
URL:        https://github.com/gooddata/gearman-plugin
Source0:    https://github.com/gooddata/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires: java
BuildRequires: maven

%description
Packaged inhouse jenkins plugin gearman-plugin-%{name}.hpi file


%prep
%setup -n %{name}-%{name}-%{version}

%build
mvn package

%install
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/juseppe
%{__cp} target/gearman-plugin.hpi %{buildroot}%{_sharedstatedir}/juseppe/

%files
%defattr(-,root,root,-)
%dir %{_sharedstatedir}/juseppe
%{_sharedstatedir}/juseppe/%{name}.hpi

%changelog
* Wed Mar 25 2020 +0700 Chien Minh Do <chien.do@gooddata.com>
- CONFIG: SETI-3633  Bump new version for gearman-plugin
