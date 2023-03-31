Name:		texlive-glossaries-portuges
Version:	36064
Release:	2
Summary:	Portuges language module for glossaries package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-portuges
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-portuges.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-portuges.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-portuges.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Portuges language module for glossaries package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/glossaries-portuges
%{_texmfdistdir}/tex/latex/glossaries-portuges
%doc %{_texmfdistdir}/doc/latex/glossaries-portuges

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
