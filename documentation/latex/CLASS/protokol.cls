   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                               %
% Tuto Šablonu vytvořil Ing. Pavel Čudek, Ph.D. %
%      pro potřeby předmětů DME a DIZ           %
%                                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                               %
% Dokument class "protokol.cls"                 %
% Šablona předpokládá kódování UTF-8 a slouží   %
% pro psaní protokolů a semestrálního projektu. %
% Šablona byla vytvořena pomocínástrojů:        %
% Overleaf (https://www.overleaf.com/),         %
% TeXstudio (https://texstudio.org),            %
% Notepad++ (https://notepad-plus-plus.org)     %
%                                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Datum poslední změny: 15.5.2024

% Definice documentclass
\NeedsTeXFormat{LaTeX2e}                  % Verze LaTeXu
\ProvidesClass{protokol}[2023/12/12 Šablona Protokolu]
\LoadClass[a4paper,                       % Výchozí velikost papíru
  oneside,                                % Jednostranně
  onecolumn,                              % Jeden odstavec
  12pt,                                   % Velikost písma
  unicode                                 % Záložky a metadata budou v unicode
  ]{article}                              % Výchozí třída dokumentu (která se upravuje)

% Preamble
%-----Obecné-----
\RequirePackage{tikz}                     % Kreslení čar a grafů
\usetikzlibrary{calc}                     % Pokročilé kreslení souřadnic
\RequirePackage{pgfplots}                 % Kreslení grafů
  \pgfplotsset{compat=newest}             % Povolí legendu pod grafem
  \usepgfplotslibrary{units}              % Povolí vložení jednotek do grafu
\RequirePackage{graphicx}                 % Pokročilá manipulace s obrázky
\RequirePackage{xcolor}                   % Povolí barevný text
\RequirePackage{hyperref}                 % Povolí hypertextové odkazy v textu (kapitoly, obrázky apod)
\RequirePackage{svg}                      % Povolí svg grafiku (JE TŘEBA NAKONFIGUROVAT INKSCAPE!!!)
\RequirePackage{chngcntr}                 % Dovolí rozšířenou práci s číslováním objektů
  \counterwithin{figure}{section}         % Čísla obrázků dle sekcí
  \counterwithin{table}{section}          % Čísla tabulek dle sekcí
  \counterwithin{equation}{section}       % Čísla vzorců dle sekcí
\RequirePackage{soulutf8}                 % Lepší zalamování textu
\RequirePackage{microtype}                % Lepší dělení slov


%-----Vzhled stránky-----
\newcommand\HRule{\rule{\textwidth}{1pt}} % povolí tvorbu rámečků okolo textu
\RequirePackage[a4paper]{geometry}        % Formát papíru
  \geometry{verbose,
    tmargin=2.5cm,                        % Okraje stránky nahoře
    bmargin=2.5cm,                        % Okraje stránky dole
    lmargin=2.5cm,                        % Okraje stránky vlevo
    rmargin=2.5cm                         % Okraje stránky vpravo
          }
  \pdfpagewidth=210mm                     % Nastavení správnou šířku A4 pro PDF
  \pdfpageheight=297mm                    % Nastavení správnou výšku A4 pro PDF

%-----Čeština-----
\RequirePackage[czech]{babel}             % Čeština
\RequirePackage[utf8]{inputenc}           % Kódování UTF8
\RequirePackage[
   figurename=Obrázek                     % Nastaví jména obrázků na Obrázek
   ,tablename=Tabulka                     % Nastaví jména tabulek na Tabulka
   ]{caption}


%-----Siroty a Vdovy-----
\clubpenalty=10000                        % Zákaz sirotů
\widowpenalty=10000                       % Zákaz vdov
\raggedbottom                             % Zarovnání konců stránek




%-----MATEMATIKA-----
\RequirePackage{mathtools}                % Povolí rozšířené nástroje pro matematiku
\RequirePackage{calc}                     % Povolení pokročilé matematiky
\RequirePackage{siunitx}                  % Rozšíření možnosti vzorců o správné používání jednotek
%\DeclareMathSizes{14}{12}{10}{8}         % {display size}{text size}{script size}{scriptscript size}

%-----Tabulky-----
\RequirePackage{array}                    % Povolí Tabulky
\RequirePackage{tabularray}               % Rozšířené typy tabulek a polí
\RequirePackage{colortbl}                 % Barevné tabulky
\RequirePackage{longtable}                % Tabulky přes stránky
\RequirePackage{multirow}                 % Víceřádková tabulka

%-----Možnost upravit styly dokumentu-----
\RequirePackage{titlesec}                 % Povolí úpravy velikosti písma sekcí
\RequirePackage{setspace}                 % Povolí úpravy řádkování
\RequirePackage{anyfontsize}              % Povolí libovolnou velikost písma
\RequirePackage{caption}                  % Povolí úpravu popisků
\RequirePackage{enumitem}                 % Definice seznamů

%-----Definice stylů dokumentu-----
\setlength{\parskip}{0cm}                 % Vertikální mezera za odstavcem textu
\setlength{\parindent}{0.5cm}             % Odsazení prvního řádku neprvního odstavce
\setstretch{1.15}                         % Nastavení řádkování na 1.15
% Nadpis 1
\titleformat{\section}                    % Změna \section (Nadpis 1)
  {\fontsize{18pt}{0}\bfseries}           % Velikost a styl písma
  {\thesection\quad}                      % Formát číslování sekce (prázdný pro vypnutí)
  {0.0cm}                                 % Horizontální mezera před názvem sekce v cm (NEMĚNIT!)
  {}                                      % Vertikální mezera za názvem sekce v cm (NEMĚNIT!)
\titlespacing*{\section}
  {0pt}                                   % Horizontální mezera před názvem sekce v pt
  {\baselineskip}
  {5pt}                                   % Vertikální mezera za názvem sekce v pt
% Nadpis 2
\titleformat{\subsection}                 % Změna \subsection (Nadpis 2)
  {\fontsize{14pt}{0}\bfseries}           % Velikost a styl písma
  {\thesubsection\quad}                   % Formát číslování subsekce (prázdný pro vypnutí)
  {0.0cm}                                 % Horizontální mezera před názvem subsekce v cm (NEMĚNIT!)
  {}                                      % Vertikální mezera za názvem subsekce v cm (NEMĚNIT!)
\titlespacing*{\subsection}
  {0pt}                                   % Horizontální mezera před názvem sekce v pt
  {\baselineskip}
  {5pt}                                   % Vertikální mezera za názvem sekce v pt
% Nadpis 3
\titleformat{\subsubsection}              % Změna \subsubsection (Nadpis 3)
  {\fontsize{14pt}{0}\bfseries}           % Velikost a styl písma
  {\thesubsubsection\quad}                % Formát číslování subsubsekce (prázdný pro vypnutí)
  {0.0cm}                                 % Horizontální mezera před názvem subsekce v cm (NEMĚNIT!)
  {}                                      % Vertikální mezera za názvem subsekce v cm (NEMĚNIT!)
\titlespacing*{\subsubsection}
  {0pt}                                   % Horizontální mezera před názvem sekce v pt
  {\baselineskip}
  {10pt}                                  % Vertikální mezera za názvem sekce v pt

\captionsetup[figure]{                    % Úprava popisu obrázků
  font={small,bf},                        % 11pt tučně
  justification=centering                 % Zarovnat na střed
  }

\captionsetup[table]{                     % Úprava popisu tabulek
  font={small,bf},                        % 11pt tučně
  justification=centering                 % zarovnat na střed
  % skip=0pt                              % Zmenší mezeru mezi popisem a tabulkou
  }

\setlist[enumerate]{                      % Upravení mezery v položkách číslovaného seznamu
  itemsep=0pt,
  topsep=5pt,                             % Malá mezera před seznamem
  partopsep=0pt,
  parsep=0pt
  }
\setlist[itemize]{                        % Upravení mezery v položkách nečíslovaného seznamu
  itemsep=0pt,
  topsep=5pt,                             % Malá mezera před seznamem
  partopsep=0pt,
  parsep=0pt
  }

%-----Ostatní (pro testovací účely)
\RequirePackage{blindtext}                % Lorem Ipsum \blinddocument
\RequirePackage{lipsum}                   % Lorem Ipsum \lipsum nebo \blindtext
