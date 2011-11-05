# revision 20910
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-mla
# catalog-date 2011-01-02 13:07:58 +0100
# catalog-license lppl
# catalog-version 0.95
Name:		texlive-biblatex-mla
Version:	0.95
Release:	1
Summary:	MLA style files for biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-mla
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-mla.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-mla.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides biblatex support for citations in the
format specified by the MLA handbook.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-mla/american-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/english-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/italian-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla.bbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla.cbx
%{_texmfdistdir}/tex/latex/biblatex-mla/portuguese-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/spanish-mla.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-mla/CHANGES
%doc %{_texmfdistdir}/doc/latex/biblatex-mla/README
%doc %{_texmfdistdir}/doc/latex/biblatex-mla/doc/biblatex-mla-old.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-mla/doc/biblatex-mla.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-mla/doc/biblatex-mla.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}