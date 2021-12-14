#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0FDE7BE0E88F5E48 (contact@emersion.fr)
#
Name     : wayland
Version  : 1.20.0
Release  : 33
URL      : https://wayland.freedesktop.org/releases/wayland-1.20.0.tar.xz
Source0  : https://wayland.freedesktop.org/releases/wayland-1.20.0.tar.xz
Source1  : https://wayland.freedesktop.org/releases/wayland-1.20.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: wayland-bin = %{version}-%{release}
Requires: wayland-data = %{version}-%{release}
Requires: wayland-filemap = %{version}-%{release}
Requires: wayland-lib = %{version}-%{release}
Requires: wayland-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : libxslt
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
Requires: wayland-data = %{version}-%{release}
Requires: wayland-license = %{version}-%{release}
Requires: wayland-filemap = %{version}-%{release}

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
Requires: wayland-lib = %{version}-%{release}
Requires: wayland-bin = %{version}-%{release}
Requires: wayland-data = %{version}-%{release}
Provides: wayland-devel = %{version}-%{release}
Requires: wayland = %{version}-%{release}

%description dev
dev components for the wayland package.


%package dev32
Summary: dev32 components for the wayland package.
Group: Default
Requires: wayland-lib32 = %{version}-%{release}
Requires: wayland-bin = %{version}-%{release}
Requires: wayland-data = %{version}-%{release}
Requires: wayland-dev = %{version}-%{release}

%description dev32
dev32 components for the wayland package.


%package filemap
Summary: filemap components for the wayland package.
Group: Default

%description filemap
filemap components for the wayland package.


%package lib
Summary: lib components for the wayland package.
Group: Libraries
Requires: wayland-data = %{version}-%{release}
Requires: wayland-license = %{version}-%{release}
Requires: wayland-filemap = %{version}-%{release}

%description lib
lib components for the wayland package.


%package lib32
Summary: lib32 components for the wayland package.
Group: Default
Requires: wayland-data = %{version}-%{release}
Requires: wayland-license = %{version}-%{release}

%description lib32
lib32 components for the wayland package.


%package license
Summary: license components for the wayland package.
Group: Default

%description license
license components for the wayland package.


%prep
%setup -q -n wayland-1.20.0
cd %{_builddir}/wayland-1.20.0
pushd ..
cp -a wayland-1.20.0 build32
popd
pushd ..
cp -a wayland-1.20.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639515734
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocumentation=false  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddocumentation=false  builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Ddocumentation=false  builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/wayland
cp %{_builddir}/wayland-1.20.0/COPYING %{buildroot}/usr/share/package-licenses/wayland/997b2f1a3639f31f0757b06a15035315baaffadc
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wayland-scanner
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/wayland/wayland-scanner.mk
/usr/share/wayland/wayland.dtd
/usr/share/wayland/wayland.xml

%files dev
%defattr(-,root,root,-)
/usr/include/wayland-client-core.h
/usr/include/wayland-client-protocol.h
/usr/include/wayland-client.h
/usr/include/wayland-cursor.h
/usr/include/wayland-egl-backend.h
/usr/include/wayland-egl-core.h
/usr/include/wayland-egl.h
/usr/include/wayland-server-core.h
/usr/include/wayland-server-protocol.h
/usr/include/wayland-server.h
/usr/include/wayland-util.h
/usr/include/wayland-version.h
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-wayland

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwayland-client.so.0
/usr/lib64/libwayland-client.so.0.20.0
/usr/lib64/libwayland-cursor.so.0
/usr/lib64/libwayland-cursor.so.0.20.0
/usr/lib64/libwayland-egl.so.1
/usr/lib64/libwayland-egl.so.1.20.0
/usr/lib64/libwayland-server.so.0
/usr/lib64/libwayland-server.so.0.20.0
/usr/share/clear/optimized-elf/lib*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libwayland-client.so.0
/usr/lib32/libwayland-client.so.0.20.0
/usr/lib32/libwayland-cursor.so.0
/usr/lib32/libwayland-cursor.so.0.20.0
/usr/lib32/libwayland-egl.so.1
/usr/lib32/libwayland-egl.so.1.20.0
/usr/lib32/libwayland-server.so.0
/usr/lib32/libwayland-server.so.0.20.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wayland/997b2f1a3639f31f0757b06a15035315baaffadc
