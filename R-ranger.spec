#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-ranger
Version  : 0.16.0
Release  : 60
URL      : https://cran.r-project.org/src/contrib/ranger_0.16.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ranger_0.16.0.tar.gz
Summary  : A Fast Implementation of Random Forests
Group    : Development/Tools
License  : GPL-3.0
Requires: R-ranger-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppEigen
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : buildreq-R

%description
dimensional data. Ensembles of classification, regression, survival and
          probability prediction trees are supported. Data from genome-wide association
          studies can be analyzed efficiently. In addition to data frames, datasets of
          class 'gwaa.data' (R package 'GenABEL') and 'dgCMatrix' (R package 'Matrix') 
          can be directly analyzed.

%package lib
Summary: lib components for the R-ranger package.
Group: Libraries

%description lib
lib components for the R-ranger package.


%prep
%setup -q -n ranger
pushd ..
cp -a ranger buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699902307

%install
export SOURCE_DATE_EPOCH=1699902307
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ranger/CITATION
/usr/lib64/R/library/ranger/DESCRIPTION
/usr/lib64/R/library/ranger/INDEX
/usr/lib64/R/library/ranger/Meta/Rd.rds
/usr/lib64/R/library/ranger/Meta/features.rds
/usr/lib64/R/library/ranger/Meta/hsearch.rds
/usr/lib64/R/library/ranger/Meta/links.rds
/usr/lib64/R/library/ranger/Meta/nsInfo.rds
/usr/lib64/R/library/ranger/Meta/package.rds
/usr/lib64/R/library/ranger/NAMESPACE
/usr/lib64/R/library/ranger/NEWS
/usr/lib64/R/library/ranger/R/ranger
/usr/lib64/R/library/ranger/R/ranger.rdb
/usr/lib64/R/library/ranger/R/ranger.rdx
/usr/lib64/R/library/ranger/help/AnIndex
/usr/lib64/R/library/ranger/help/aliases.rds
/usr/lib64/R/library/ranger/help/paths.rds
/usr/lib64/R/library/ranger/help/ranger.rdb
/usr/lib64/R/library/ranger/help/ranger.rdx
/usr/lib64/R/library/ranger/html/00Index.html
/usr/lib64/R/library/ranger/html/R.css
/usr/lib64/R/library/ranger/include/ranger.h
/usr/lib64/R/library/ranger/tests/test_gwaa.rds
/usr/lib64/R/library/ranger/tests/testthat.R
/usr/lib64/R/library/ranger/tests/testthat/test_betasplit.R
/usr/lib64/R/library/ranger/tests/testthat/test_char.R
/usr/lib64/R/library/ranger/tests/testthat/test_classification.R
/usr/lib64/R/library/ranger/tests/testthat/test_classweights.R
/usr/lib64/R/library/ranger/tests/testthat/test_csrf.R
/usr/lib64/R/library/ranger/tests/testthat/test_deforest.R
/usr/lib64/R/library/ranger/tests/testthat/test_extratrees.R
/usr/lib64/R/library/ranger/tests/testthat/test_formula.R
/usr/lib64/R/library/ranger/tests/testthat/test_genabel.R
/usr/lib64/R/library/ranger/tests/testthat/test_hellinger.R
/usr/lib64/R/library/ranger/tests/testthat/test_importance.R
/usr/lib64/R/library/ranger/tests/testthat/test_importance_casewise.R
/usr/lib64/R/library/ranger/tests/testthat/test_importance_pvalues.R
/usr/lib64/R/library/ranger/tests/testthat/test_inbag.R
/usr/lib64/R/library/ranger/tests/testthat/test_interface.R
/usr/lib64/R/library/ranger/tests/testthat/test_jackknife.R
/usr/lib64/R/library/ranger/tests/testthat/test_maxstat.R
/usr/lib64/R/library/ranger/tests/testthat/test_nodestats.R
/usr/lib64/R/library/ranger/tests/testthat/test_predict.R
/usr/lib64/R/library/ranger/tests/testthat/test_print.R
/usr/lib64/R/library/ranger/tests/testthat/test_probability.R
/usr/lib64/R/library/ranger/tests/testthat/test_quantreg.R
/usr/lib64/R/library/ranger/tests/testthat/test_ranger.R
/usr/lib64/R/library/ranger/tests/testthat/test_regression.R
/usr/lib64/R/library/ranger/tests/testthat/test_regularization.R
/usr/lib64/R/library/ranger/tests/testthat/test_seed.R
/usr/lib64/R/library/ranger/tests/testthat/test_sparse.R
/usr/lib64/R/library/ranger/tests/testthat/test_splitweights.R
/usr/lib64/R/library/ranger/tests/testthat/test_survival.R
/usr/lib64/R/library/ranger/tests/testthat/test_treeInfo.R
/usr/lib64/R/library/ranger/tests/testthat/test_unordered.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ranger/libs/ranger.so
/usr/lib64/R/library/ranger/libs/ranger.so.avx2
/usr/lib64/R/library/ranger/libs/ranger.so.avx512
