# revision 20910
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-mla
# catalog-date 2011-01-02 13:07:58 +0100
# catalog-license lppl
# catalog-version 0.95
Name:		texlive-biblatex-mla
Version:	0.95
Release:	2
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

%description
The package provides biblatex support for citations in the
format specified by the MLA handbook.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.95-2
+ Revision: 749667
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.95-1
+ Revision: 717928
- texlive-biblatex-mla
- texlive-biblatex-mla
- texlive-biblatex-mla
- texlive-biblatex-mla
- texlive-biblatex-mla

