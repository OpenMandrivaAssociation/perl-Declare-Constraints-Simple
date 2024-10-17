%define upstream_name    Declare-Constraints-Simple
%define upstream_version 0.03

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Declare::Constraints::Simple-Library\\)'
%else
%define _requires_exceptions perl(Declare::Constraints::Simple-Library)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Declarative Validation of Data Structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Declare/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(aliased)

BuildArch:	noarch
Requires:	perl(aliased)

%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set of
declarative keywords in the importing namespace.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Declare

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 681393
- mass rebuild

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 505727
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.03-3mdv2010.0
+ Revision: 430407
- rebuild

* Sun Sep 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-2mdv2009.0
+ Revision: 286344
- fix dependencies
- import perl-Declare-Constraints-Simple


* Sun Sep 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
- initial mdv release, generated with cpan2dist

