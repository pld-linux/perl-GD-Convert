#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Convert
Summary:	GD::Convert Perl module - additional output formats for GD
Summary(pl.UTF-8):	Moduł Perla GD::Convert - dodatkowe formaty wyjściowe dla GD
Name:		perl-GD-Convert
Version:	2.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fdab5cbbc56266a3051d68bfada1a7ba
Patch0:		%{name}-nocroak.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-GD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Convert is a pure Perl module which provides additional output
functions for the GD module: ppm and xpm. These formats are useful if
you need to dynamically create photos for Tk.

%description -l pl.UTF-8
GD::Convert to moduł Perla dodający obsługę dwóch formatów wyjściowych
do modułu GD: ppm i xpm. Te formaty są przydatne zwłaszcza wtedy,
kiedy potrzeba dynamicznie tworzyć obrazy dla Tk.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/GD/Convert.pm
%{_mandir}/man3/*
