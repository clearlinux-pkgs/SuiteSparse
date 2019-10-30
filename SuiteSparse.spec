#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SuiteSparse
Version  : 5.1.0
Release  : 26
URL      : http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-5.1.0.tar.gz
Source0  : http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-5.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: SuiteSparse-lib = %{version}-%{release}
Requires: SuiteSparse-license = %{version}-%{release}
BuildRequires : SuiteSparse-dev
BuildRequires : buildreq-cmake
BuildRequires : metis-dev
BuildRequires : openblas
BuildRequires : tbb-dev
BuildRequires : util-linux
Patch1: build.patch
Patch2: ivdep.patch
Patch3: makefile-metis.patch

%description
SuiteSparse: a suite of sparse matrix packages by T. A. Davis et al.
(This repository contains copies of the official releases.)

%package dev
Summary: dev components for the SuiteSparse package.
Group: Development
Requires: SuiteSparse-lib = %{version}-%{release}
Provides: SuiteSparse-devel = %{version}-%{release}
Requires: SuiteSparse = %{version}-%{release}

%description dev
dev components for the SuiteSparse package.


%package doc
Summary: doc components for the SuiteSparse package.
Group: Documentation

%description doc
doc components for the SuiteSparse package.


%package lib
Summary: lib components for the SuiteSparse package.
Group: Libraries
Requires: SuiteSparse-license = %{version}-%{release}

%description lib
lib components for the SuiteSparse package.


%package license
Summary: license components for the SuiteSparse package.
Group: Default

%description license
license components for the SuiteSparse package.


%prep
%setup -q -n SuiteSparse
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a SuiteSparse buildavx2
popd

%build
## build_prepend content
find ./metis-5.1.0 ! -name 'LICENSE.txt' -type f -exec rm -f {} +
ln -s %{_includedir}/metis.h include/metis.h
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572478822
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
make  %{?_smp_mflags}  BLAS=-lopenblas LAPACK=-lopenblas library MY_METIS_LIB=/usr/lib64/libmetis.so

pushd ../buildavx2
## build_prepend content
find ./metis-5.1.0 ! -name 'LICENSE.txt' -type f -exec rm -f {} +
ln -s %{_includedir}/metis.h include/metis.h
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
make  %{?_smp_mflags}  BLAS=-lopenblas LAPACK=-lopenblas library MY_METIS_LIB=/usr/lib64/libmetis.so
popd

%install
export SOURCE_DATE_EPOCH=1572478822
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SuiteSparse
cp %{_builddir}/SuiteSparse/AMD/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/3ab21591eed55f18245a4d40d77eb92056888701
cp %{_builddir}/SuiteSparse/BTF/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b13f6d59d5b230774696d884785ec850e6d31bc2
cp %{_builddir}/SuiteSparse/CAMD/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/a62dec2a77f26f4925d49f03b155b3290cb7cfe1
cp %{_builddir}/SuiteSparse/CCOLAMD/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/de522c4d6fbb410a79215466e3449a4cb6bdd3ce
cp %{_builddir}/SuiteSparse/CHOLMOD/Demo/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/CHOLMOD/MATLAB/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/CHOLMOD/MatrixOps/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/CHOLMOD/Modify/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/CHOLMOD/Supernodal/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/CHOLMOD/Tcov/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/CHOLMOD/Valgrind/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/COLAMD/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/faa0661d302ed2af604ec96af361af9efcf81a63
cp %{_builddir}/SuiteSparse/CSparse/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/f8fdd046aa7b6df4eb00a0f5a84b0edd23c3b15a
cp %{_builddir}/SuiteSparse/CSparse/MATLAB/ssget/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/3883f9170a394433eb82463d65a377a333838188
cp %{_builddir}/SuiteSparse/CXSparse/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/21951afb2d8cb7f350c28dee727d2009d222301c
cp %{_builddir}/SuiteSparse/CXSparse/MATLAB/ssget/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/3883f9170a394433eb82463d65a377a333838188
cp %{_builddir}/SuiteSparse/CXSparse_newfiles/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/21951afb2d8cb7f350c28dee727d2009d222301c
cp %{_builddir}/SuiteSparse/GPUQREngine/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/25bc1bfcf61590bd9e715d24eecedf5ec09760e4
cp %{_builddir}/SuiteSparse/GPUQREngine/Doc/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/GraphBLAS/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/75f51f80e2c38b3294bd335fa848ae96bfd6d026
cp %{_builddir}/SuiteSparse/KLU/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/cef232b1a01b764b52f77124b54b868095253ddd
cp %{_builddir}/SuiteSparse/LDL/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/9422890a4ef75e4cbe85067fffb6fb256a306ba9
cp %{_builddir}/SuiteSparse/MATLAB_Tools/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/e6db7d30ea73e48587a96e14120efdf96f704477
cp %{_builddir}/SuiteSparse/RBio/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/8102b3aadcb879901e248d04be18843b71a894c3
cp %{_builddir}/SuiteSparse/RBio/Doc/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/SPQR/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/25d008cc9407fe74e848986127e114e3a5453c83
cp %{_builddir}/SuiteSparse/SPQR/Doc/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/SuiteSparse_GPURuntime/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/0427e4024d4d35d256a2ead9bee1b5968a36c912
cp %{_builddir}/SuiteSparse/SuiteSparse_GPURuntime/Doc/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/UMFPACK/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/a91968addad8b454bb714ff34b4adefb4bceab01
cp %{_builddir}/SuiteSparse/UMFPACK/Doc/gpl.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/SuiteSparse/metis-5.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/a7c3a4f7dcf7a014c7dfdd3f8752d699eb7f7c2e
cp %{_builddir}/SuiteSparse/ssget/Doc/License.txt %{buildroot}/usr/share/package-licenses/SuiteSparse/3883f9170a394433eb82463d65a377a333838188
pushd ../buildavx2/
%make_install_avx2 BLAS=-lopenblas LAPACK=-lopenblas INSTALL=%{buildroot}/usr  INSTALL_LIB=%{buildroot}/usr/lib64 INSTALL_BIN=%{buildroot}/usr/bin MY_METIS_LIB=/usr/lib64/libmetis.so || :
popd
%make_install BLAS=-lopenblas LAPACK=-lopenblas INSTALL=%{buildroot}/usr  INSTALL_LIB=%{buildroot}/usr/lib64 INSTALL_BIN=%{buildroot}/usr/bin MY_METIS_LIB=/usr/lib64/libmetis.so || :
## Remove excluded files
rm -f %{buildroot}/usr/include/.gitignore
## install_append content
mkdir -p %{buildroot}/usr/include
cp -a include/*.{h,hpp} %{buildroot}/usr/include/
rm -f %{buildroot}/usr/include/metis.h
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/RBio.h
/usr/include/SuiteSparseQR.hpp
/usr/include/SuiteSparseQR_C.h
/usr/include/SuiteSparseQR_definitions.h
/usr/include/SuiteSparse_config.h
/usr/include/amd.h
/usr/include/btf.h
/usr/include/camd.h
/usr/include/ccolamd.h
/usr/include/cholmod.h
/usr/include/cholmod_blas.h
/usr/include/cholmod_camd.h
/usr/include/cholmod_check.h
/usr/include/cholmod_cholesky.h
/usr/include/cholmod_complexity.h
/usr/include/cholmod_config.h
/usr/include/cholmod_core.h
/usr/include/cholmod_function.h
/usr/include/cholmod_gpu.h
/usr/include/cholmod_gpu_kernels.h
/usr/include/cholmod_io64.h
/usr/include/cholmod_matrixops.h
/usr/include/cholmod_modify.h
/usr/include/cholmod_partition.h
/usr/include/cholmod_supernodal.h
/usr/include/cholmod_template.h
/usr/include/colamd.h
/usr/include/cs.h
/usr/include/klu.h
/usr/include/ldl.h
/usr/include/spqr.hpp
/usr/include/umfpack.h
/usr/include/umfpack_col_to_triplet.h
/usr/include/umfpack_defaults.h
/usr/include/umfpack_free_numeric.h
/usr/include/umfpack_free_symbolic.h
/usr/include/umfpack_get_determinant.h
/usr/include/umfpack_get_lunz.h
/usr/include/umfpack_get_numeric.h
/usr/include/umfpack_get_symbolic.h
/usr/include/umfpack_global.h
/usr/include/umfpack_load_numeric.h
/usr/include/umfpack_load_symbolic.h
/usr/include/umfpack_numeric.h
/usr/include/umfpack_qsymbolic.h
/usr/include/umfpack_report_control.h
/usr/include/umfpack_report_info.h
/usr/include/umfpack_report_matrix.h
/usr/include/umfpack_report_numeric.h
/usr/include/umfpack_report_perm.h
/usr/include/umfpack_report_status.h
/usr/include/umfpack_report_symbolic.h
/usr/include/umfpack_report_triplet.h
/usr/include/umfpack_report_vector.h
/usr/include/umfpack_save_numeric.h
/usr/include/umfpack_save_symbolic.h
/usr/include/umfpack_scale.h
/usr/include/umfpack_solve.h
/usr/include/umfpack_symbolic.h
/usr/include/umfpack_tictoc.h
/usr/include/umfpack_timer.h
/usr/include/umfpack_transpose.h
/usr/include/umfpack_triplet_to_col.h
/usr/include/umfpack_wsolve.h
/usr/lib64/haswell/libamd.so
/usr/lib64/haswell/libbtf.so
/usr/lib64/haswell/libcamd.so
/usr/lib64/haswell/libccolamd.so
/usr/lib64/haswell/libcholmod.so
/usr/lib64/haswell/libcolamd.so
/usr/lib64/haswell/libcxsparse.so
/usr/lib64/haswell/libklu.so
/usr/lib64/haswell/libldl.so
/usr/lib64/haswell/librbio.so
/usr/lib64/haswell/libspqr.so
/usr/lib64/haswell/libsuitesparseconfig.so
/usr/lib64/haswell/libumfpack.so
/usr/lib64/libamd.so
/usr/lib64/libbtf.so
/usr/lib64/libcamd.so
/usr/lib64/libccolamd.so
/usr/lib64/libcholmod.so
/usr/lib64/libcolamd.so
/usr/lib64/libcxsparse.so
/usr/lib64/libklu.so
/usr/lib64/libldl.so
/usr/lib64/librbio.so
/usr/lib64/libspqr.so
/usr/lib64/libsuitesparseconfig.so
/usr/lib64/libumfpack.so

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/doc/suitesparse-5.1.0/RBIO_README.txt
/usr/share/doc/suitesparse-5.1.0/SPQR_README.txt
/usr/share/doc/suitesparse-5.1.0/SUITESPARSECONFIG_README.txt
/usr/share/doc/suitesparse-5.1.0/SuiteSparse_README.txt
/usr/share/doc/suitesparse-5.1.0/UMFPACK_QuickStart.pdf
/usr/share/doc/suitesparse-5.1.0/UMFPACK_README.txt
/usr/share/doc/suitesparse-5.1.0/UMFPACK_UserGuide.pdf
/usr/share/doc/suitesparse-5.1.0/ldl_userguide.pdf
/usr/share/doc/suitesparse-5.1.0/spqr_user_guide.pdf

%files lib
%defattr(-,root,root,-)
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
/usr/lib64/libcxsparse.so.3.2.0
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SuiteSparse/0427e4024d4d35d256a2ead9bee1b5968a36c912
/usr/share/package-licenses/SuiteSparse/21951afb2d8cb7f350c28dee727d2009d222301c
/usr/share/package-licenses/SuiteSparse/25bc1bfcf61590bd9e715d24eecedf5ec09760e4
/usr/share/package-licenses/SuiteSparse/25d008cc9407fe74e848986127e114e3a5453c83
/usr/share/package-licenses/SuiteSparse/3883f9170a394433eb82463d65a377a333838188
/usr/share/package-licenses/SuiteSparse/3ab21591eed55f18245a4d40d77eb92056888701
/usr/share/package-licenses/SuiteSparse/75f51f80e2c38b3294bd335fa848ae96bfd6d026
/usr/share/package-licenses/SuiteSparse/8102b3aadcb879901e248d04be18843b71a894c3
/usr/share/package-licenses/SuiteSparse/9422890a4ef75e4cbe85067fffb6fb256a306ba9
/usr/share/package-licenses/SuiteSparse/a62dec2a77f26f4925d49f03b155b3290cb7cfe1
/usr/share/package-licenses/SuiteSparse/a7c3a4f7dcf7a014c7dfdd3f8752d699eb7f7c2e
/usr/share/package-licenses/SuiteSparse/a91968addad8b454bb714ff34b4adefb4bceab01
/usr/share/package-licenses/SuiteSparse/b13f6d59d5b230774696d884785ec850e6d31bc2
/usr/share/package-licenses/SuiteSparse/b47456e2c1f38c40346ff00db976a2badf36b5e3
/usr/share/package-licenses/SuiteSparse/cef232b1a01b764b52f77124b54b868095253ddd
/usr/share/package-licenses/SuiteSparse/de522c4d6fbb410a79215466e3449a4cb6bdd3ce
/usr/share/package-licenses/SuiteSparse/e6db7d30ea73e48587a96e14120efdf96f704477
/usr/share/package-licenses/SuiteSparse/f8fdd046aa7b6df4eb00a0f5a84b0edd23c3b15a
/usr/share/package-licenses/SuiteSparse/faa0661d302ed2af604ec96af361af9efcf81a63
