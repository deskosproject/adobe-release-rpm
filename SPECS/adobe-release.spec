Name:           adobe-release
Version:        1.0
Release:        1%{?dist}
Summary:        Adobe repository configuration

Group:          System Environment/Base
License:        BSD
URL:            http://adobe.com
Source0:        adobe.repo
Source1:        RPM-GPG-KEY-adobe
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
Provides:       adobe-release-x86_64
Obsoletes:      adobe-release-x86_64

%description
Adobe Linux repository configuration.

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/adobe.repo

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-adobe
%config(noreplace) /etc/yum.repos.d/adobe.repo

%changelog
* Wed Jun 1 2016 Ricardo Arguello <rarguello@deskosproject.org> - 1.0-1
- Initial DeskOS release
