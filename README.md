# CV [![Example](https://img.shields.io/badge/example-pdf-green.svg)](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume.pdf)

<!--
## Quick Start

1. [**OverLeaf.com**](https://www.overleaf.com/latex/templates/awesome-cv/tvmzpvdjfqxp)(formerly **WriteLaTeX.com**)

**_Note:_ Above services do not guarantee up-to-date source code of Awesome CV**
-->

## Requirements:
- [Latexmk](https://mg.readthedocs.io/latexmk.html)  
You probably have it already installed on your computer, because it is part of MacTeX and MikTeX and is bundled with many Linux Distributions.
For macOS with brew I suggest 
```
brew install --cask mactex
```
- [Python 3](https://www.python.org/downloads/)  
Required to run build.py script

## Compilation
```zsh
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -outdir=output/pdf "resume.tex"
```

## Editor
As an editor I strongly suggest Visual Studio Code.  
List of required extensions are in `.vscode/extensions.json`.


## Spell checker
I used `aspell` for spell checks in terminal.
```zsh
# install aspell
brew install aspell 

# run spellcheck script
./spellcheck.py
```

## Credit
### LaTeX
LaTeX is a fantastic typesetting program that a lot of people use these days, especially the math and computer science people in academia.

You can find out more about it here: [LaTeX Project](http://www.latex-project.org)


### Awesome CV
[**Awesome CV**](https://github.com/posquit0/Awesome-CV) is LaTeX template for a **CV(Curriculum Vitae)** or **resume** or **cover letter** inspired by [Fancy CV](https://www.sharelatex.com/templates/cv-or-resume/fancy-cv). It is easy to customize your own template, especially since it is really written by a clean, semantic markup.

![alt tag](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume-0.png)
![alt tag](https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume-1.png)


### LaTeX-FontAwesome
[LaTeX FontAwesome](https://github.com/furl/latex-fontawesome) is bindings for FontAwesome icons to be used in XeLaTeX.

### Roboto
[Roboto](https://github.com/google/roboto) is the default font on Android and ChromeOS, and the recommended font for Google’s visual language, Material Design.

### Source Sans Pro
[Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro) is a set of OpenType fonts that have been designed to work well in user interface (UI) environments.


## Contact
You are free to take my `.tex` file and modify it to create your own resume. Please don't use my resume for anything else without my permission, though!

Good luck!
