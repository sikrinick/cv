# CV [![Example](https://img.shields.io/badge/example-pdf-green.svg)](https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/resume.pdf)

This is my CV and an extremelly small LaTeX class for my CV requirements.  
Please, don't hesitate to use it for your needs.

## Resume
[![Resume](https://raw.githubusercontent.com/sikrinick/cv/master/output/svg/resume.svg)](https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/resume/resume.pdf)

## More precise Curriculim Vitae
<table>
<tr>
<td valign="top">

<a href="https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/cv/cv.pdf">

<img
src="https://raw.githubusercontent.com/sikrinick/cv/master/output/svg/cv.svg" title="cv" 
/>
</a>
</td>

<td valign="top">
<a href="https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/cv/cv.pdf">
<img
 src="https://raw.githubusercontent.com/sikrinick/cv/master/output/svg/cv.2.svg" title="cv_2"
 />
</a>
</td>
</table>

## Quick Start
- [**Check CV on OverLeaf.com**](https://www.overleaf.com/read/sthfkhvrccpx)

## Requirements:
- [Latexmk](https://mg.readthedocs.io/latexmk.html)  
If you use LaTeX you probably have it already installed on your computer, because it is part of MacTeX and MikTeX and is bundled with many Linux Distributions.  
For macOS with brew I suggest 
```
brew install --cask mactex
```
- [Python 3](https://www.python.org/downloads/)  
Required to run `build.py` script

## Compilation
```zsh
./build.py
```
or
```zsh
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error "cv.tex"
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error "resume.tex"
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
- [LaTeX](http://www.latex-project.org)
- [Awesome CV](https://github.com/posquit0/Awesome-CV)
- [cvmaker](https://cvmkr.com/) and especially its [Elegant](https://cvmkr.com/pl/Pages/samples?type=elegant) sample
