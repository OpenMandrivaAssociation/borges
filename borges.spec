%define name    borges
%define Name    Borges
%define version 0.14.9
%define release %mkrel 4

Name:   %{name}
Version: %{version}
Release: %{release}
Summary: Mandriva Linux Documents Management System
License: GPL
Group: Publishing
Url: http://www.mandrivalinux.com/en/doc/project/Borges/
Source0: %{Name}-%{version}.tar.bz2
Requires: %{name}-module
Requires: libxslt-proc
Requires: make
Requires: imagemagick
Requires: xfig
Requires: libxml2-utils
Conflicts: Borges-Frontend < 0.12.2
BuildRequires: libxslt-proc
BuildRequires: perl(Date::Manip)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(XML::Twig)
BuildRequires: imagemagick
BuildRequires: xfig
BuildRequires: jadetex
BuildRequires: docbook-style-dsssl
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtd42-xml
BuildRequires: libxml2-utils
Obsoletes: Borges
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Borges is a content production system aimed at creating documents in
many languages. Its design goals are internationalization,
flexibility, reusable content, teamwork. The system can currently be
used for any project using documents based on the DocBook XML DTD.

%package docbook
Summary: The Borges DocBook module 
Group: Publishing
Provides: borges-module
Requires: borges
Requires: docbook-dtd42-xml
Requires: docbook-style-xsl
Requires: docbook-style-dsssl
Requires: tetex-latex
Requires: jadetex
Requires: openjade
Obsoletes: Borges-DocBook

%description docbook
This package contains the DocBook module for the Borges Documents
Management System.
It holds the different files allowing to handle documents written with
the DocBook XML DTD.


%package frontend
Summary: The BorgesWeb frontend
Group: Publishing
Requires: borges
Requires: apache-mod_suexec
Obsoletes: Borges-Frontend

%description frontend
This package contains the Web frontend for the Borges Documents
Management System.
It is an HTML interface allowing users to upload or edit inline the
different modules they have tasks assigned on. It then commits
modifications to CVS and eventually pass associated task.


%package doc
Summary: The Borges DMS documentation
Group: Publishing

%description doc
This package contains the documentation and the documentation sources
for the Borges Documents Management System. The doc is written with
Borges so the sources included can be regarded as a tutorial for
learning how to use Borges.

%prep
%setup -q -n %{Name}-%{version}

%build

%install
rm -rf %{buildroot}
%makeinstall PREFIX=%{buildroot}/ DOCDIR=%{buildroot}/%{_docdir}/%{name}
rm -f %{buildroot}/usr/share/Borges/backend/Makefile.TDB
rm -f %{buildroot}/usr/share/Borges/template/drivers/TDB-tex.xsl
rm -f %{buildroot}/usr/share/Borges/{README,LICENSE,COPYING,VERSION}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_docdir}/%{name}
%{_datadir}/%{Name}
%exclude %{_docdir}/%{name}/doc
%exclude %{_datadir}/%{Name}/template/drivers/docbook-*sl
%exclude %{_datadir}/%{Name}/backend/Makefile.DB
%exclude %{_datadir}/%{Name}/bin/web-frontend.cgi


%files docbook
%defattr(-,root,root)
%{_datadir}/%{Name}/template/drivers/docbook-*sl
%{_datadir}/%{Name}/backend/Makefile.DB

%files frontend
%defattr(-,root,root)
%{_datadir}/%{Name}/bin/web-frontend.cgi

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/doc
