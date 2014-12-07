%define upstream_name	 DateTime-Format-ISO8601
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	14

Summary:	Parses almost all ISO8601 date and time formats
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/RPM4/
Source0:	%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Builder)
BuildRequires:	perl(Class::Factory::Util)
BuildRequires:	perl(Module::Build)
Requires:	perl(Class::Factory::Util)
BuildArch:	noarch

%description
Parse and format W3CDTF datetime strings.
ISO8601 time-intervals will be supported in a later release.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.70.0-4mdv2011.0
+ Revision: 657064
- add br
- rebuild for updated spec-helper

* Mon Nov 15 2010 Colin Guthrie <cguthrie@mandriva.org> 0.70.0-3mdv2011.0
+ Revision: 597644
- Fix Requires

* Mon Nov 15 2010 Colin Guthrie <cguthrie@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 597625
- Add a require that wasn't caught automagically for some reason

* Fri Nov 12 2010 Colin Guthrie <cguthrie@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 596595
- import perl-DateTime-Format-ISO8601

