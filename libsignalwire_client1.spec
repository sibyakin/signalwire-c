Name:          libsignalwire_client1
Version:       1.0.0
Release:       1
Summary:       SignalWire's C client library
License:       MIT
Group:         Development/Libraries/C and C++
Url:           https://signalwire.com/
Source:        https://github.com/signalwire/signalwire-c/archive/%{version}.tar.gz

BuildRequires: git
BuildRequires: cmake
BuildRequires: pkg-config
BuildRequires: libuuid-devel
BuildRequires: libks1-devel

%if 0%{?is_opensuse}
BuildRequires: libopenssl-devel
%endif

%if 0%{?fedora}
BuildRequires: openssl-devel
%endif

BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
SignalWire's C client library

%package devel
Summary:       SignalWire's libks
Group:         Development/Libraries/C and C++
Requires:	   %{name} = %{version}

%description devel
SignalWire's C client library. Development files

%prep
%setup -n signalwire-c-%{version}

%build
export PKG_CONFIG_PATH=/usr/lib/pkgconfig
cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/usr
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/lib/libsignalwire_client.so*
%{_datadir}/doc/signalwire-client-c

%files devel
%defattr(-,root,root)
%{_includedir}/signalwire-client-c/
/usr/lib/pkgconfig/signalwire_client.pc

%changelog
* Tue Jan 29 2019 - alex@freeswitch.com 
- Initial build
