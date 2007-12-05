%define name Borges
%define version 0.14.9
%define release %mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Mandriva Linux Documents Management System
License: GPL
Group: Publishing
Url: http://www.mandrivalinux.com/en/doc/project/Borges/
Source0: %{name}-%{version}.tar.bz2
Requires: %{name}-module
Requires: libxslt-proc
Requires: make
Requires: ImageMagick
Requires: xfig
Requires: libxml2-utils
Conflicts: Borges-Frontend < 0.12.2
BuildRequires: libxslt-proc
BuildRequires: perl-DateManip
BuildRequires: perl-XML-LibXML
BuildRequires: perl-XML-Twig
BuildRequires: ImageMagick
BuildRequires: xfig
BuildRequires: jadetex
BuildRequires: docbook-style-dsssl
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtd42-xml
BuildRequires: libxml2-utils
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%define INSTALLDIR /usr/share/%{name}/

%description

Borges is a content production system aimed at creating documents in
many languages. Its design goals are internationalization,
flexibility, reusable content, teamwork. The system can currently be
used for any project using documents based on the DocBook XML DTD.

%package DocBook
Summary: The Borges DocBook module 
Group: Publishing
Provides: Borges-module
Requires: Borges
Requires: docbook-dtd42-xml
Requires: docbook-style-xsl
Requires: docbook-style-dsssl
Requires: tetex-latex
Requires: jadetex
Requires: openjade

%description DocBook
This package contains the DocBook module for the Borges Documents
Management System.
It holds the different files allowing to handle documents written with
the DocBook XML DTD.


%package Frontend
Summary: The BorgesWeb frontend
Group: Publishing
Requires: Borges
Requires: apache-mod_suexec

%description Frontend
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
%setup -q

%build
%makeinstall PREFIX=$(pwd)/installdir/ REALDESTDIR=$(pwd)/installdir/usr/share/Borges/
make DESTDIR=$(pwd)/installdir/usr/share/Borges/ REALDESTDIR=$(pwd)/installdir/usr/share/Borges/

%install
rm -rf %{buildroot}
%makeinstall PREFIX=%{buildroot}/
rm -f %{buildroot}/usr/share/Borges/backend/Makefile.TDB
rm -f %{buildroot}/usr/share/Borges/template/drivers/TDB-tex.xsl
find doc/ -name .cvsignore -exec rm -f {} \;
find doc/ -name \*.validate -exec rm -f {} \;
find doc/ -type f -empty -exec rm -f {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README VERSION TODO CHANGELOG
%dir %{INSTALLDIR}
# version management stylesheets
%dir %{INSTALLDIR}/XSL
%{INSTALLDIR}/XSL/bigbrother.xsl
%{INSTALLDIR}/XSL/bigbrother-todos.xsl
%{INSTALLDIR}/XSL/extract_ids.xsl
%{INSTALLDIR}/XSL/gather_revhistories.xsl
%{INSTALLDIR}/XSL/summarize_tasks.xsl
%{INSTALLDIR}/XSL/db2omf.xsl
%{INSTALLDIR}/XSL/extract_revisions.xsl
%{INSTALLDIR}/XSL/docs_index.xsl
%{INSTALLDIR}/XSL/filter.xsl
%{INSTALLDIR}/XSL/report_summary.xsl
%{INSTALLDIR}/XSL/todo_tasks.xsl
%{INSTALLDIR}/XSL/list_modules.xsl
# management perl/shell scripts.xsl
%dir %{INSTALLDIR}/bin
%{INSTALLDIR}/bin/*.sh
%{INSTALLDIR}/bin/configure
%{INSTALLDIR}/bin/*.pl
%{INSTALLDIR}/bin/diff2html
# Utilities
%dir %{INSTALLDIR}/utils
%{INSTALLDIR}/utils/*
# Makefile structure
%dir %{INSTALLDIR}/backend
%{INSTALLDIR}/backend/cvsignore.*
%{INSTALLDIR}/backend/Makefile.entities
%{INSTALLDIR}/backend/Makefile.src.images
%{INSTALLDIR}/backend/Makefile.reports
%{INSTALLDIR}/backend/Makefile.onemodule.include
%{INSTALLDIR}/backend/Makefile.module
%{INSTALLDIR}/backend/Makefile.manual.include
%{INSTALLDIR}/backend/Makefile.manual
%{INSTALLDIR}/backend/Makefile.include.in
%{INSTALLDIR}/backend/Makefile.images
# System implementation template
%dir %{INSTALLDIR}/template/
%dir %{INSTALLDIR}/template/conf/
%dir %{INSTALLDIR}/template/drivers/
%{INSTALLDIR}/template/conf/*
%{INSTALLDIR}/template/images
%{INSTALLDIR}/backend/psgml-top.xml
%{INSTALLDIR}/template/Makefile
%{INSTALLDIR}/template/README
%{INSTALLDIR}/VERSION
%{INSTALLDIR}/README
%{INSTALLDIR}/LICENSE
%{INSTALLDIR}/COPYING
# Sample document
%dir %{INSTALLDIR}/Sample
%{INSTALLDIR}/Sample/*
# %{INSTALLDIR}/Sample/en/*


%files DocBook
%defattr(-,root,root)
%{INSTALLDIR}/template/drivers/docbook-*sl
%{INSTALLDIR}/backend/Makefile.DB

%files Frontend
%defattr(-,root,root)
%{INSTALLDIR}/bin/web-frontend.cgi

%files doc
%defattr(-,root,root)
%doc README VERSION TODO CHANGELOG LICENSE COPYING doc

