# NOTE: not ready for libpgm 5.x
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Perl interface to OpenPGM library
Summary(pl.UTF-8):	Perlowy interfejs do biblioteki OpenPGM
Name:		perl-OpenPgm
Version:	0.01
Release:	0.1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://openpgm.googlecode.com/files/OpenPgm-%{version}.tbz2
# Source0-md5:	770f99e3ebed4ef1f18bf43c92a2ae9d
URL:		http://openpgm.googlecode.com/
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib >= 1.161
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	libpgm-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to OpenPGM library.

%description -l pl.UTF-8
Perlowy interfejs do biblioteki OpenPGM.

%prep
%setup -q -n OpenPgm-%{version}

%{__perl} -pi -e 's/openpgm-2\.0/openpgm-5.2/g' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/OpenPgm.pm
%dir %{perl_vendorarch}/auto/OpenPgm
%{perl_vendorarch}/auto/OpenPgm/OpenPgm.bs
%attr(755,root,root) %{perl_vendorarch}/auto/OpenPgm/OpenPgm.so
%{_mandir}/man3/OpenPgm.3pm*
