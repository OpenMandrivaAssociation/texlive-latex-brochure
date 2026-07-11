%global tl_name latex-brochure
%global tl_revision 40612

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A publicity flyer for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-brochure
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-brochure.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-brochure.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document is designed as a publicity flyer for LaTeX, but also serves
as an interesting showcase of what LaTeX can do. The flyer is designed
for printing, double-sided, on A3 paper, which would then be folded
once.

