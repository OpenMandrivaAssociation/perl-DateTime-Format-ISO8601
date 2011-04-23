%define upstream_name	 DateTime-Format-ISO8601
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Parses almost all ISO8601 date and time formats
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/RPM4/
Source0:	%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Builder)
BuildRequires: perl(Class::Factory::Util)
Buildrequires: perl(Module::Build)
Requires: perl(Class::Factory::Util)
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Parse and format W3CDTF datetime strings.
ISO8601 time-intervals will be supported in a later release.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*
