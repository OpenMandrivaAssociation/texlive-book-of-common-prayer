Name:		texlive-book-of-common-prayer
Version:	62240
Release:	2
Summary:	Typeset in the style of "Book of Common Prayer"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/book-of-common-prayer
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/book-of-common-prayer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/book-of-common-prayer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This a package for the typesetting of liturgical documents in
the style of the 1979 "Book of Common Prayer". It provides
macros for common liturgical situations (e.g. versicle and
response, longer prayers, etc.). This package is designed to
work with the Sabon font, but it is not necessary to run the
macros.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/book-of-common-prayer
%doc %{_texmfdistdir}/doc/latex/book-of-common-prayer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
