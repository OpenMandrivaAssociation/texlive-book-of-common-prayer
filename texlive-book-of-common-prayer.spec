%global tl_name book-of-common-prayer
%global tl_revision 62240

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	Typeset in the style of Book of Common Prayer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/book-of-common-prayer
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/book-of-common-prayer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/book-of-common-prayer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This a package for the typesetting of liturgical documents in the style
of the 1979 "Book of Common Prayer". It provides macros for common
liturgical situations (e.g. versicle and response, longer prayers,
etc.). This package is designed to work with the Sabon font, but it is
not necessary to run the macros.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/book-of-common-prayer
%dir %{_datadir}/texmf-dist/tex/latex/book-of-common-prayer
%doc %{_datadir}/texmf-dist/doc/latex/book-of-common-prayer/README.md
%doc %{_datadir}/texmf-dist/doc/latex/book-of-common-prayer/book-of-common-prayer.pdf
%doc %{_datadir}/texmf-dist/doc/latex/book-of-common-prayer/book-of-common-prayer.tex
%{_datadir}/texmf-dist/tex/latex/book-of-common-prayer/book-of-common-prayer.sty
