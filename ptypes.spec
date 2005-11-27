Summary:	C++ Portable Types Library
Summary(pl):	Przeno¶na biblioteka typów C++
Name:		ptypes
Version:	2.0.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.melikyan.com/ptypes/%{name}-%{version}.tar.gz
# Source0-md5:	f5a6c90a3f9e89f90f4ea81f71c4ec7d
Patch0:		%{name}-opt.patch
URL:		http://www.melikyan.com/ptypes/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PTypes (C++ Portable Types Library) is a simple alternative to the STL
that includes multithreading and networking. It defines dynamic
strings, variants, character sets, lists and other basic data types
along with portable thread and synchronization objects, IP sockets and
named pipes. Its main `target audience' is developers of complex
network daemons, robots or non-visual client/server applications of
any kind.

%description -l pl
PTypes (C++ Portable Types Library - przeno¶na biblioteka typów C++)
to prosta alternatywa dla STL zawieraj±ca wielow±tkowo¶æ i obs³ugê
sieci. Definiuje dynamiczne ³añcuchy, warianty, zestawy znaków, listy
i inne podstawowe typy danych wraz z przeno¶nymi w±tkami i obiektami
synchronizacji, gniazdami IP oraz nazwanymi potokami. G³ówn± "grup±
docelow±" biblioteki s± programi¶ci z³o¿onych serwerów sieciowych,
robotów lub niewizualnych aplikacji klient-serwer dowolnego rodzaju.

%package devel
Summary:	Development files for PTypes
Summary(pl):	Pliki rozwojowe dla PTypes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files required for development using PTypes.

%description devel -l pl
Pliki nag³ówkowe wymagane do tworzenia programów z u¿yciem PTypes.

%package static
Summary:	Static version of PTypes library
Summary(pl):	Biblioteka statyczna PTypes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static version of PTypes library.

%description static -l pl
Pakiet ten zawiera statyczn± wersjê biblioteki PTypes.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/ptypes,%{_libdir},%{_libdir}}

install include/*.h $RPM_BUILD_ROOT%{_includedir}/ptypes
install lib/*.a $RPM_BUILD_ROOT%{_libdir}
install so/*.so.* $RPM_BUILD_ROOT%{_libdir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libptypes.so.* libptypes.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc index.* doc
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
