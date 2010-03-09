Summary:	A program to extract Microsoft Cabinet files
Summary(pl.UTF-8):	Program do rozpakowywania plików MS Cabinet
Name:		cabextract
Version:	1.2
Release:	2
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.cabextract.org.uk/%{name}-%{version}.tar.gz
# Source0-md5:	dc421a690648b503265c82ade84e143e
Patch0:		%{name}-libmspack.patch
URL:		http://www.cabextract.org.uk/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libmspack-devel >= 0.0.20060920alpha
Requires:	libmspack >= 0.0.20060920alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%description -l pl.UTF-8
Pliki Cabinet (.CAB) są rodzajem archiwum, który Microsoft używa do
dystrybucji swojego oprogramowania i rzeczy typu Windows Font Pack.
cabextract może takie pliki rozpakować.

%prep
%setup -q
%patch0 -p1
rm -rf mspack

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/ja/cabextract.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/cabextract.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
