Summary:	C++ Portable Types Library
Summary(pl):	C++ ...
Name:		ptypes
Version:	2.0.1
Release:	0.1
License:	free
Group:		Libraries
Source0:	http://www.melikyan.com/ptypes/%{name}-%{version}.tar.gz
# Source0-md5:	78338ef651975b535468cfc28f15fc37
Patch0:		%{name}-opt.patch
URL:		http://www.melikyan.com/ptypes/
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
PTypes ...

%package devel
Summary:	Development files for PTypes
Summary(pl):	Pliki rozwojowe dla PTypes
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files required for development using PTypes.

%description devel -l pl
Pliki nag³ówkowe wymagane do tworzenia programów z u¿yciem PTypes.

%package static
Summary:	Static library for PTypes development
Summary(pl):	Biblioteka statyczna do PTypes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the static library needed to develop programs
that use PTypes.

%description static -l pl
Pakiet ten zawiera bibliotekê statyczn± potrzebn± przy tworzeniu
programów wykorzystuj±cych PTypes.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/ptypes,/%{_lib},%{_libdir}}

install include/*.h $RPM_BUILD_ROOT%{_includedir}/ptypes
install lib/*.a $RPM_BUILD_ROOT%{_libdir}
install so/*.so.* $RPM_BUILD_ROOT%{_libdir}

ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib} && echo libptypes.so.*) \
	$RPM_BUILD_ROOT%{_libdir}/libptypes.so

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
