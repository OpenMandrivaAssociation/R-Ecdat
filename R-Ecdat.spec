%global packname  Ecdat
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2.2
Release:          1
Summary:          Data sets for econometrics
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Ecdat_0.2-2.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-car R-systemfit R-sem R-lmtest R-sandwich 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-car R-systemfit R-sem R-lmtest R-sandwich 

%description
Data sets for econometrics

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demoFiles
%{rlibdir}/%{packname}/scripts

