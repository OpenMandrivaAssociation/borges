%define sname    Borges

Summary:	Mandriva Linux Documents Management System
Name:		borges
Version:	0.14.9
Release:	9
License:	GPLv2
Group:		Publishing
Url:		https://www.mandrivalinux.com/en/doc/project/Borges/
Source0:	%{sname}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd42-xml
BuildRequires:	imagemagick
BuildRequires:	jadetex
BuildRequires:	libxml2-utils
BuildRequires:	xfig
BuildRequires:	xsltproc
BuildRequires:	perl(Date::Manip)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::Twig)
Requires:	%{name}-module
Requires:	imagemagick
Requires:	libxml2-utils
Requires:	make
Requires:	xfig
Requires:	xsltproc

%description
Borges is a content production system aimed at creating documents in
many languages. Its design goals are internationalization,
flexibility, reusable content, teamwork. The system can currently be
used for any project using documents based on the DocBook XML DTD.

%package	docbook
Summary:	The Borges DocBook module 
Group:		Publishing
Provides:	borges-module
Requires:	borges
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	docbook-style-dsssl
Requires:	tetex-latex
Requires:	jadetex
Requires:	openjade

%description	docbook
This package contains the DocBook module for the Borges Documents
Management System.
It holds the different files allowing to handle documents written with
the DocBook XML DTD.

%package	frontend
Summary:	The BorgesWeb frontend
Group:		Publishing
Requires:	borges
Requires:	apache-mod_suexec

%description	frontend
This package contains the Web frontend for the Borges Documents
Management System.
It is an HTML interface allowing users to upload or edit inline the
different modules they have tasks assigned on. It then commits
modifications to CVS and eventually pass associated task.

%package	doc
Summary:	The Borges DMS documentation
Group:		Publishing

%description	doc
This package contains the documentation and the documentation sources
for the Borges Documents Management System. The doc is written with
Borges so the sources included can be regarded as a tutorial for
learning how to use Borges.

%prep
%setup -qn %{sname}-%{version}

%build

%install
%makeinstall PREFIX=%{buildroot}/ DOCDIR=%{buildroot}/%{_docdir}/%{name}
rm -f %{buildroot}/usr/share/Borges/backend/Makefile.TDB
rm -f %{buildroot}/usr/share/Borges/template/drivers/TDB-tex.xsl
rm -f %{buildroot}/usr/share/Borges/{README,LICENSE,COPYING,VERSION}

%files
%{_docdir}/%{name}
%{_datadir}/%{sname}
%exclude %{_docdir}/%{name}/doc
%exclude %{_datadir}/%{sname}/template/drivers/docbook-*sl
%exclude %{_datadir}/%{sname}/backend/Makefile.DB
%exclude %{_datadir}/%{sname}/bin/web-frontend.cgi

%files docbook
%{_datadir}/%{sname}/template/drivers/docbook-*sl
%{_datadir}/%{sname}/backend/Makefile.DB

%files frontend
%{_datadir}/%{sname}/bin/web-frontend.cgi

%files doc
%{_docdir}/%{name}/doc

