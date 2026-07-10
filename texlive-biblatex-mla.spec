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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides BibLaTeX support for citations in the format
specified by the MLA handbook.

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
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-mla
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-mla
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/CHANGES
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/biblatex-mla.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/biblatex-mla.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/bibtex_documentation.sty
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/examples.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/examples.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/handbook9.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-mla/doc/handbook9_messy.bib
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/american-mla.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/english-mla.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/italian-mla.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla-footnotes.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla-new.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla-new.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla-strict.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla-strict.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla7.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/mla7.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/portuguese-mla.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-mla/spanish-mla.lbx
