# CV [![Example](https://img.shields.io/badge/example-pdf-green.svg)](https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/cv.pdf)

CV template and a LaTeX class.

<a href="https://github.com/sikrinick/cv/blob/master/output/pdf/cv_android/cv_android.pdf">
<img src="https://github.com/sikrinick/cv/blob/master/output/svg/cv_android.1.svg"/>
</a>

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
- [pdf2svg](https://cityinthesky.co.uk/opensource/pdf2svg/)  
Required to run `build.py` script
```
brew install pdf2svg
```
## Compilation
```zsh
./build.py
```
or
```zsh
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error "cv_android.tex"
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
- [American Psycho — Business Card scene](https://www.youtube.com/watch?v=aZVkW9p-cCU&ab_channel=SCOTLUSHdotCOM) for the background color inspiration
