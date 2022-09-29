\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ms-cv}[2022/05/07 v2.0.1 MS CV]


\providecommand{\isresume}{}
\DeclareOption{resume}{
    \renewcommand{\isresume}{true}
}
\DeclareOption{cv}{
    \renewcommand{\isresume}{false}
}

% Inherit options of article
\DeclareOption*{
  \PassOptionsToClass{\CurrentOption}{article}
}

\ExecuteOptions{resume}

\ProcessOptions\relax

\LoadClass{article}

% Needed to configure page layout
\RequirePackage{geometry}
% Needed to change line spacing in specific environment
\RequirePackage{setspace}
% Needed to manage fonts
\RequirePackage{fontspec}
% Times New Roman
\RequirePackage{newtxtext, newtxmath}
% Tables
\RequirePackage{tabularx}
% Table borders
\RequirePackage{tabularborder}
% Forloop
\RequirePackage{forloop}
% Colors
\RequirePackage{xcolor}
% ifelsethen
\RequirePackage{xifthen}
% Needed to deal hyperlink
\RequirePackage[hidelinks]{hyperref}

%% Page Layout
\geometry{left=1.0cm, top=1.0cm, right=1.0cm, bottom=1.0cm}
% 1.5 spacing
\onehalfspacing
% No indents
\setlength{\parindent}{0pt}
% No page numbers
\pagenumbering{gobble}
% Page color
\definecolor{backgroundcolor}{HTML}{FDF6E3}
\pagecolor{backgroundcolor}

%% Styles
% For elements of skill
\newcommand*{\skilltypestyle}[1]{{\small\bfseries #1}}
\newcommand*{\skillsetstyle}[1]{{\small#1}}

% Personal info
\newcommand*{\name}[1]{\def\@name{#1}}
\newcommand*{\position}[1]{\def\@position{#1}}
\newcommand*{\mobile}[1]{\def\@mobile{#1}}
\newcommand*{\email}[1]{\def\@email{#1}}
\newcommand*{\github}[1]{\def\@github{#1}}
\newcommand*{\linkedin}[1]{\def\@linkedin{#1}}

\newcommand{\providecounter}[1]{
    \@ifundefined{c@#1}{\newcounter{#1}}{}
}

% \cvsection[<section-end>]{<section-title>}
\newcommand{\cvsection}[2][]{
    {\large\MakeUppercase{#2}}
    \hspace{1mm}
    \hrulefill
    \ifthenelse{\isempty{#1}}
        {}
        {
            \hspace{1mm}
            {\large#1}
        }
    
}

% \cvexperience{company}{position}{place}{dates}{resume_description}{cv_description}
\newcommand{\cvexperience}[6]{
    \begin{flushleft}
    \begin{tabularx}{\textwidth}{X r}
        {\large#2} & {\large#3} \\
        {\large#1} & #4 \\
        \ifthenelse{\equal{\isresume}{true}}{
            #5 & \\
        }{
            #6 & \\
        }    
    \end{tabularx}
    \end{flushleft}
}


\newenvironment{cvskills}{
    \providecounter{cvskillcounter}
    \setcounter{cvskillcounter}{0}    
}{
    \begin{center}
    \setlength\tabcolsep{1ex}
    \setlength{\extrarowheight}{0pt}
    \providecounter{idx}
    \begin{tabularx}{\textwidth}{r X}
        \forloop{idx}{0}{\value{idx}<\value{cvskillcounter}}{
            \bfseries{\@nameuse{cvskillname\theidx}} & \large\@nameuse{cvskilllist\theidx} \\
        }
    \end{tabularx}
    \end{center}
}

% \cvskill{type}{skillset}
\newcommand*{\cvskill}[2]{
    \@namedef{cvskillname\arabic{cvskillcounter}}{#1}
    \@namedef{cvskilllist\arabic{cvskillcounter}}{#2}
    \stepcounter{cvskillcounter}
}

% CV header with contact info
\newcommand{\makecvheader}{
  
    {\fontsize{40}{48}\selectfont \@name}
    \hfill
    As of \today
    
    \vspace{3mm}
    \ifthenelse{\isundefined{\@position}}{}{
        {\huge\@position}
    }

    \rule{\textwidth}{0.1pt}
    
    \begin{flushleft}
    \begin{tabularx}{\textwidth}{X X}
        Phone: \@mobile 
            & \hfill\url{https://github.com/\@github} \\
        \href{mailto:\@email}{\@email}
            & \hfill\url{https://www.linkedin.com/in/\@linkedin}
    \end{tabularx}
    \end{flushleft}
}
