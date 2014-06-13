# revision 28916
# category Package
# catalog-ctan /info/latex-brochure
# catalog-date 2013-01-22 18:02:11 +0100
# catalog-license lppl
# catalog-version 2013-01-22
Name:		texlive-latex-brochure
Version:	20130122
Release:	7
Summary:	A publicity flyer for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-brochure
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-brochure.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-brochure.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document is designed as a publicity flyer for LaTeX, but
also serves as an interesting showcase of what LaTeX can do.
The flyer is designed for printing, double-sided, on A3 paper,
which would then be folded once.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-brochure/README
%doc %{_texmfdistdir}/doc/latex/latex-brochure/README.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure-a3folderFB.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure-a3folderIN.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure-a4.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure-ledgerfolderFB.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure-ledgerfolderIN.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure-letter.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure.bib
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure.sty
%doc %{_texmfdistdir}/doc/latex/latex-brochure/brochure.tex
%doc %{_texmfdistdir}/doc/latex/latex-brochure/build
%doc %{_texmfdistdir}/doc/latex/latex-brochure/diagram-crop.eps
%doc %{_texmfdistdir}/doc/latex/latex-brochure/diagram-crop.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/fullscreen.eps
%doc %{_texmfdistdir}/doc/latex/latex-brochure/fullscreen.png
%doc %{_texmfdistdir}/doc/latex/latex-brochure/index.html
%doc %{_texmfdistdir}/doc/latex/latex-brochure/sample-crop.eps
%doc %{_texmfdistdir}/doc/latex/latex-brochure/sample-crop.pdf
%doc %{_texmfdistdir}/doc/latex/latex-brochure/typo-degraded.eps
%doc %{_texmfdistdir}/doc/latex/latex-brochure/typo-degraded.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
