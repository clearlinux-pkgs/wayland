#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5E54498E697F11D7 (derekf@osg.samsung.com)
#
Name     : wayland
Version  : 1.16.0
Release  : 17
URL      : https://wayland.freedesktop.org/releases/wayland-1.16.0.tar.xz
Source0  : https://wayland.freedesktop.org/releases/wayland-1.16.0.tar.xz
Source99 : https://wayland.freedesktop.org/releases/wayland-1.16.0.tar.xz.sig
Summary  : Wayland scanner
Group    : Development/Tools
License  : MIT
Requires: wayland-bin
Requires: wayland-lib
Requires: wayland-license
Requires: wayland-data
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : grep
BuildRequires : libxslt
BuildRequires : mesa-dev
BuildRequires : mesa-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32expat)
BuildRequires : pkgconfig(32libffi)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : xmlto

%description
What is Wayland?
Wayland is a project to define a protocol for a compositor to talk to
its clients as well as a library implementation of the protocol.  The
compositor can be a standalone display server running on Linux kernel
modesetting and evdev input devices, an X application, or a wayland
client itself.  The clients can be traditional applications, X servers
(rootless or fullscreen) or other display servers.

%package bin
Summary: bin components for the wayland package.
Group: Binaries
Requires: wayland-data
Requires: wayland-license

%description bin
bin components for the wayland package.


%package data
Summary: data components for the wayland package.
Group: Data

%description data
data components for the wayland package.


%package dev
Summary: dev components for the wayland package.
Group: Development
Requires: wayland-lib
Requires: wayland-bin
Requires: wayland-data
Provides: wayland-devel

%description dev
dev components for the wayland package.


%package dev32
Summary: dev32 components for the wayland package.
Group: Default
Requires: wayland-lib32
Requires: wayland-bin
Requires: wayland-data
Requires: wayland-dev

%description dev32
dev32 components for the wayland package.


%package lib
Summary: lib components for the wayland package.
Group: Libraries
Requires: wayland-data
Requires: wayland-license

%description lib
lib components for the wayland package.


%package lib32
Summary: lib32 components for the wayland package.
Group: Default
Requires: wayland-data
Requires: wayland-license

%description lib32
lib32 components for the wayland package.


%package license
Summary: license components for the wayland package.
Group: Default

%description license
license components for the wayland package.


%prep
%setup -q -n wayland-1.16.0
pushd ..
cp -a wayland-1.16.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536125844
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-documentation
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --disable-documentation   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536125844
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/wayland
cp COPYING %{buildroot}/usr/share/doc/wayland/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wayland-scanner

%files data
%defattr(-,root,root,-)
/usr/share/wayland/wayland-scanner.mk
/usr/share/wayland/wayland.dtd
/usr/share/wayland/wayland.xml

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libwayland-client.so
/usr/lib64/libwayland-cursor.so
/usr/lib64/libwayland-egl.so
/usr/lib64/libwayland-server.so
/usr/lib64/pkgconfig/wayland-client.pc
/usr/lib64/pkgconfig/wayland-cursor.pc
/usr/lib64/pkgconfig/wayland-egl-backend.pc
/usr/lib64/pkgconfig/wayland-egl.pc
/usr/lib64/pkgconfig/wayland-scanner.pc
/usr/lib64/pkgconfig/wayland-server.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libwayland-client.so
/usr/lib32/libwayland-cursor.so
/usr/lib32/libwayland-egl.so
/usr/lib32/libwayland-server.so
/usr/lib32/pkgconfig/32wayland-client.pc
/usr/lib32/pkgconfig/32wayland-cursor.pc
/usr/lib32/pkgconfig/32wayland-egl-backend.pc
/usr/lib32/pkgconfig/32wayland-egl.pc
/usr/lib32/pkgconfig/32wayland-scanner.pc
/usr/lib32/pkgconfig/32wayland-server.pc
/usr/lib32/pkgconfig/wayland-client.pc
/usr/lib32/pkgconfig/wayland-cursor.pc
/usr/lib32/pkgconfig/wayland-egl-backend.pc
/usr/lib32/pkgconfig/wayland-egl.pc
/usr/lib32/pkgconfig/wayland-scanner.pc
/usr/lib32/pkgconfig/wayland-server.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwayland-client.so.0
/usr/lib64/libwayland-client.so.0.3.0
/usr/lib64/libwayland-cursor.so.0
/usr/lib64/libwayland-cursor.so.0.0.0
/usr/lib64/libwayland-egl.so.1
/usr/lib64/libwayland-egl.so.1.0.0
/usr/lib64/libwayland-server.so.0
/usr/lib64/libwayland-server.so.0.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libwayland-client.so.0
/usr/lib32/libwayland-client.so.0.3.0
/usr/lib32/libwayland-cursor.so.0
/usr/lib32/libwayland-cursor.so.0.0.0
/usr/lib32/libwayland-egl.so.1
/usr/lib32/libwayland-egl.so.1.0.0
/usr/lib32/libwayland-server.so.0
/usr/lib32/libwayland-server.so.0.1.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/wayland/COPYING
