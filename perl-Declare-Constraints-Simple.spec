%define module   Declare-Constraints-Simple
%define version    0.03
%define release    %mkrel 3

%define _requires_exceptions perl(Declare::Constraints::Simple-Library)

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Declarative Validation of Data Structures
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Declare/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl-aliased
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
Requires:      perl-aliased
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set of
declarative keywords in the importing namespace.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

