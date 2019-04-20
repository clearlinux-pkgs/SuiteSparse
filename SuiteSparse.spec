#
#
Name     : SuiteSparse
Version  : 5.1.0
Release  : 9
URL      : http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-5.1.0.tar.gz
Source0  : http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-5.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: SuiteSparse-bin
Requires: SuiteSparse-lib
Requires: SuiteSparse-data
BuildRequires : SuiteSparse-dev
BuildRequires : cmake
BuildRequires : openblas
BuildRequires : tbb-dev
Patch1: build.patch
Patch2: ivdep.patch

%description
This file contains some test graphs and meshes
4elt.graph
copter2.graph
mdual.graph
These are small to medium size graphs corresponding to 2D and 3D
finite element mesh. They can be used as inputs to gpmetis and ndmetis.

%package bin
Summary: bin components for the SuiteSparse package.
Group: Binaries
Requires: SuiteSparse-data

%description bin
bin components for the SuiteSparse package.


%package data
Summary: data components for the SuiteSparse package.
Group: Data

%description data
data components for the SuiteSparse package.


%package dev
Summary: dev components for the SuiteSparse package.
Group: Development
Requires: SuiteSparse-lib
Requires: SuiteSparse-bin
Requires: SuiteSparse-data
Provides: SuiteSparse-devel

%description dev
dev components for the SuiteSparse package.


%package lib
Summary: lib components for the SuiteSparse package.
Group: Libraries
Requires: SuiteSparse-data

%description lib
lib components for the SuiteSparse package.


%prep
%setup -q -n SuiteSparse
%patch1 -p1
%patch2 -p1
pushd ..
cp -a SuiteSparse buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505596563
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
make V=1  %{?_smp_mflags} BLAS=-lopenblas LAPACK=-lopenblas library metis
pushd ../buildavx2/
export CFLAGS="$CFLAGS -march=haswell"
export CXXFLAGS="$CXXFLAGS -march=haswell"
make V=1  %{?_smp_mflags} BLAS=-lopenblas LAPACK=-lopenblas library metis
popd
%install
export SOURCE_DATE_EPOCH=1505596563
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install BLAS=-lopenblas LAPACK=-lopenblas INSTALL=%{buildroot}/usr  INSTALL_LIB=%{buildroot}/usr/lib64/haswell INSTALL_BIN=%{buildroot}/usr/bin || :
popd
%make_install BLAS=-lopenblas LAPACK=-lopenblas INSTALL=%{buildroot}/usr  INSTALL_LIB=%{buildroot}/usr/lib64 INSTALL_BIN=%{buildroot}/usr/bin || :
## make_install_append content
cp -a include %{buildroot}/usr
mkdir -p  %{buildroot}/usr/bin/
#mv %{buildroot}/builddir/build/BUILD/buildavx2/bin/* %{buildroot}/usr/bin/
#mv %{buildroot}/builddir/build/BUILD/buildavx2/lib/* %{buildroot}/usr/lib64/
#mv %{buildroot}/builddir/build/BUILD/buildavx2/include/* %{buildroot}/usr/include/
#rmdir  %{buildroot}/builddir/build/BUILD/buildavx2/*
#rmdir  %{buildroot}/builddir/build/BUILD/*
#mdir  %{buildroot}/builddir/build/*
#rmdir  %{buildroot}/builddir/*
#rmdir  %{buildroot}/builddir
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/doc/suitesparse-5.1.0/AMD_README.txt
/usr/share/doc/suitesparse-5.1.0/AMD_UserGuide.pdf
/usr/share/doc/suitesparse-5.1.0/BTF_README.txt
/usr/share/doc/suitesparse-5.1.0/CAMD_README.txt
/usr/share/doc/suitesparse-5.1.0/CAMD_UserGuide.pdf
/usr/share/doc/suitesparse-5.1.0/CCOLAMD_README.txt
/usr/share/doc/suitesparse-5.1.0/CHOLMOD_README.txt
/usr/share/doc/suitesparse-5.1.0/CHOLMOD_UserGuide.pdf
/usr/share/doc/suitesparse-5.1.0/COLAMD_README.txt
/usr/share/doc/suitesparse-5.1.0/CXSPARSE_README.txt
/usr/share/doc/suitesparse-5.1.0/KLU_README.txt
/usr/share/doc/suitesparse-5.1.0/KLU_UserGuide.pdf
/usr/share/doc/suitesparse-5.1.0/LDL_README.txt
/usr/share/doc/suitesparse-5.1.0/METIS_README.txt
/usr/share/doc/suitesparse-5.1.0/METIS_manual.pdf
/usr/share/doc/suitesparse-5.1.0/RBIO_README.txt
/usr/share/doc/suitesparse-5.1.0/SPQR_README.txt
/usr/share/doc/suitesparse-5.1.0/SUITESPARSECONFIG_README.txt
/usr/share/doc/suitesparse-5.1.0/SuiteSparse_README.txt
/usr/share/doc/suitesparse-5.1.0/UMFPACK_QuickStart.pdf
/usr/share/doc/suitesparse-5.1.0/UMFPACK_README.txt
/usr/share/doc/suitesparse-5.1.0/UMFPACK_UserGuide.pdf
/usr/share/doc/suitesparse-5.1.0/ldl_userguide.pdf
/usr/share/doc/suitesparse-5.1.0/spqr_user_guide.pdf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/*.hpp
/usr/include/.gitignore
/usr/lib64/libamd.so
/usr/lib64/libbtf.so
/usr/lib64/libcamd.so
/usr/lib64/libccolamd.so
/usr/lib64/libcholmod.so
/usr/lib64/libcolamd.so
/usr/lib64/libcxsparse.so
/usr/lib64/libklu.so
/usr/lib64/libldl.so
/usr/lib64/libmetis.so
/usr/lib64/librbio.so
/usr/lib64/libspqr.so
/usr/lib64/libsuitesparseconfig.so
/usr/lib64/libumfpack.so
/usr/lib64/haswell/libamd.so
/usr/lib64/haswell/libbtf.so
/usr/lib64/haswell/libcamd.so
/usr/lib64/haswell/libccolamd.so
/usr/lib64/haswell/libcholmod.so
/usr/lib64/haswell/libcolamd.so
/usr/lib64/haswell/libcxsparse.so
/usr/lib64/haswell/libklu.so
/usr/lib64/haswell/libldl.so
/usr/lib64/haswell/libmetis.so
/usr/lib64/haswell/librbio.so
/usr/lib64/haswell/libspqr.so
/usr/lib64/haswell/libsuitesparseconfig.so
/usr/lib64/haswell/libumfpack.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libamd.so.2
/usr/lib64/libamd.so.2.4.6
/usr/lib64/libbtf.so.1
/usr/lib64/libbtf.so.1.2.6
/usr/lib64/libcamd.so.2
/usr/lib64/libcamd.so.2.4.6
/usr/lib64/libccolamd.so.2
/usr/lib64/libccolamd.so.2.9.6
/usr/lib64/libcholmod.so.3
/usr/lib64/libcholmod.so.3.0.11
/usr/lib64/libcolamd.so.2
/usr/lib64/libcolamd.so.2.9.6
/usr/lib64/libcxsparse.so.3
/usr/lib64/libcxsparse.so.3*
/usr/lib64/libklu.so.1
/usr/lib64/libklu.so.1.3.8
/usr/lib64/libldl.so.2
/usr/lib64/libldl.so.2.2.6
/usr/lib64/librbio.so.2
/usr/lib64/librbio.so.2.2.6
/usr/lib64/libspqr.so.2
/usr/lib64/libspqr.so.2.0.8
/usr/lib64/libsuitesparseconfig.so.5
/usr/lib64/libsuitesparseconfig.so.5.1.0
/usr/lib64/libumfpack.so.5
/usr/lib64/libumfpack.so.5.7.6
/usr/lib64/haswell/libamd.so.2
/usr/lib64/haswell/libamd.so.2.4.6
/usr/lib64/haswell/libbtf.so.1
/usr/lib64/haswell/libbtf.so.1.2.6
/usr/lib64/haswell/libcamd.so.2
/usr/lib64/haswell/libcamd.so.2.4.6
/usr/lib64/haswell/libccolamd.so.2
/usr/lib64/haswell/libccolamd.so.2.9.6
/usr/lib64/haswell/libcholmod.so.3
/usr/lib64/haswell/libcholmod.so.3.0.11
/usr/lib64/haswell/libcolamd.so.2
/usr/lib64/haswell/libcolamd.so.2.9.6
/usr/lib64/haswell/libcxsparse.so.3
/usr/lib64/haswell/libcxsparse.so.3.2.0
/usr/lib64/haswell/libklu.so.1
/usr/lib64/haswell/libklu.so.1.3.8
/usr/lib64/haswell/libldl.so.2
/usr/lib64/haswell/libldl.so.2.2.6
/usr/lib64/haswell/librbio.so.2
/usr/lib64/haswell/librbio.so.2.2.6
/usr/lib64/haswell/libspqr.so.2
/usr/lib64/haswell/libspqr.so.2.0.8
/usr/lib64/haswell/libsuitesparseconfig.so.5
/usr/lib64/haswell/libsuitesparseconfig.so.5.1.0
/usr/lib64/haswell/libumfpack.so.5
/usr/lib64/haswell/libumfpack.so.5.7.6
