Summary:	C++ Portable Types Library
Summary(pl.UTF-8):	Przenośna biblioteka typów C++
Name:		ptypes
Version:	2.1.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.melikyan.com/ptypes/%{name}-%{version}.tar.gz
# Source0-md5:	f7ed34b09d5b764294e93382f18a0ed3
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

%description -l pl.UTF-8
PTypes (C++ Portable Types Library - przenośna biblioteka typów C++)
to prosta alternatywa dla STL zawierająca wielowątkowość i obsługę
sieci. Definiuje dynamiczne łańcuchy, warianty, zestawy znaków, listy
i inne podstawowe typy danych wraz z przenośnymi wątkami i obiektami
synchronizacji, gniazdami IP oraz nazwanymi potokami. Główną "grupą
docelową" biblioteki są programiści złożonych serwerów sieciowych,
robotów lub niewizualnych aplikacji klient-serwer dowolnego rodzaju.

%package devel
Summary:	Development files for PTypes
Summary(pl.UTF-8):	Pliki rozwojowe dla PTypes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files required for development using PTypes.

%description devel -l pl.UTF-8
Pliki nagłówkowe wymagane do tworzenia programów z użyciem PTypes.

%package static
Summary:	Static version of PTypes library
Summary(pl.UTF-8):	Biblioteka statyczna PTypes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static version of PTypes library.

%description static -l pl.UTF-8
Pakiet ten zawiera statyczną wersję biblioteki PTypes.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
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
