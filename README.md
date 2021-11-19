# CV [![Example](https://img.shields.io/badge/example-pdf-green.svg)](https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/resume.pdf)

This is my CV and an extremelly small LaTeX class for my CV requirements.  
Please, don't hesitate to use it for your needs.
<object data="https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/resume.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/resume.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://raw.githubusercontent.com/sikrinick/cv/master/output/pdf/resume.pdf">Download PDF</a>.</p>
    </embed>
</object>

## Requirements:
- [Latexmk](https://mg.readthedocs.io/latexmk.html)  
You probably have it already installed on your computer, because it is part of MacTeX and MikTeX and is bundled with many Linux Distributions.
For macOS with brew I suggest 
```
brew install --cask mactex
```

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
- [LaTeX](http://www.latex-project.org)
- [Awesome CV](https://github.com/posquit0/Awesome-CV)
- [cvmaker](https://cvmkr.com/) and especially its [Elegant](https://cvmkr.com/pl/Pages/samples?type=elegant) sample
