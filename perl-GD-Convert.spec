%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Convert
Summary:	GD::Convert Perl module - additional output formats for GD
Summary(pl):	Modu³ Perla GD::Convert - dodatkowe formaty wyj¶ciowe dla GD
Name:		perl-GD-Convert
Version:	1.17
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-GD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Convert is a pure Perl module which provides additional output
functions for the GD module: ppm and xpm. These formats are useful if
you need to dynamically create photos for Tk.

%description -l pl
GD::Convert to modu³ Perla dodaj±cy obs³ugê dwóch formatów wyj¶ciowych
do modu³u GD: ppm i xpm. Te formaty s± przydatne zw³aszcza wtedy,
kiedy potrzeba dynamicznie tworzyæ obrazy dla Tk.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/GD/Convert.pm
%{_mandir}/man3/*
