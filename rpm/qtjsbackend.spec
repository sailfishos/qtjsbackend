Name:           qt5-qtjsbackend
Summary:        Qt Javascript backend
Version:        5.0.2
Release:        1%{%dist}
Group:          Qt/Qt
License:        LGPLv2.1 with exception or GPLv3
URL:            http://qt.nokia.com
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qmake
BuildRequires:  python
BuildRequires:  fdupes


%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package is a dummy, built to make V8 packages easier to handle.

%package -n qt5-qtv8
Summary:    Qt Javascript backend
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtv8
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the V8 Javascript backend

%package -n qt5-qtv8-devel
Summary:    Qt Javascript backend - development files
Group:      Qt/Qt
Requires:   qt5-qtv8 = %{version}-%{release}

%description -n qt5-qtv8-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the V8 Javascript backend development files


#### Build section

%prep
%setup -q -n %{name}-%{version}/qtjsbackend

%build
export QTDIR=/usr/share/qt5
touch .git
qmake -qt=5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# XXX: when enabled in build, fix wrong path in prl files
#
# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt


%fdupes %{buildroot}/%{_includedir}


#### Pre/Post section

%post -n qt5-qtv8
/sbin/ldconfig

%postun -n qt5-qtv8
/sbin/ldconfig


#### Files section

# Empty by design
%files
%defattr(-,root,root,-)

%files -n qt5-qtv8
%defattr(-,root,root,-)
%{_libdir}/libQt5V8.so.5
%{_libdir}/libQt5V8.so.5.*


%files -n qt5-qtv8-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtV8/
%{_libdir}/libQt5V8.prl
%{_libdir}/libQt5V8.so
%{_libdir}/pkgconfig/Qt5V8.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_v8.pri


#### No changelog section, separate $pkg.changes contains the history

