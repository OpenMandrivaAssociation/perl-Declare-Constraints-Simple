%define upstream_name    Declare-Constraints-Simple
%define upstream_version 0.03

%define _requires_exceptions perl(Declare::Constraints::Simple-Library)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Declarative Validation of Data Structures
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Declare/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(aliased)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires:      perl(aliased)

%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set of
declarative keywords in the importing namespace.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Declare
