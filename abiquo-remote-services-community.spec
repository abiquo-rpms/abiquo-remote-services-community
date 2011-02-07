%define abiquo_basedir /opt/abiquo

Name:     abiquo-remote-services-community
Version:  1.7
Release:  3%{?dist}%{?buildstamp}
Summary:  Abiquo Remote Services
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  README 
Source1:  abiquo.properties.remoteservices
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-vsm abiquo-am abiquo-virtualfactory-community libvirt-client dhcp redis nfs-utils abiquo-server-tools
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package installs Abiquo Remote Services components.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}/
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/
cp ../SOURCES/README $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp %{SOURCE1} $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/README
%{abiquo_basedir}/config/examples/abiquo.properties.remoteservices

%changelog
* Mon Feb 07 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- changed buildarch

* Mon Feb 07 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- remove post scripts

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-1
- Initial Release
