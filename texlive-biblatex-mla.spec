%global tl_name biblatex-mla
%global tl_revision 62138

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1a
Release:	%{tl_revision}.1
Summary:	MLA style files for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-mla
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-mla.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-mla.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides BibLaTeX support for citations in the format
specified by the MLA handbook.

