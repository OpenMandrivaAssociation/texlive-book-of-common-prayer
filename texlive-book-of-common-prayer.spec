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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This a package for the typesetting of liturgical documents in the style
of the 1979 "Book of Common Prayer". It provides macros for common
liturgical situations (e.g. versicle and response, longer prayers,
etc.). This package is designed to work with the Sabon font, but it is
not necessary to run the macros.

