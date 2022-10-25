#!/usr/bin/env python3

from os.path import dirname, realpath, join
from os import chdir
from subprocess import run
from pathlib import Path

script_dir = dirname(realpath(__file__))
chdir(script_dir)

class Target:
    
    def __init__(self, input_file_name: str, output_dir: str) -> 'Target':
        self.input_file_name = input_file_name
        self.output_dir = output_dir
        self.target_name = Path(self.input_file_name).with_suffix("")


    def build(self):
        pdf = self.__build_pdf()
        self.__build_svg(pdf)        

    def __build_pdf(self) -> Path:
        output_pdf_dir = self.output_dir / "pdf" / self.target_name
        output_pdf_dir.mkdir(parents=True, exist_ok=True)

        output_pdf_file = output_pdf_dir / self.target_name.with_suffix(".pdf")

        run([
            "latexmk",
            "-xelatex",
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            f"-outdir={output_pdf_dir}",
            f'"{self.input_file_name}"'
        ])
        print("\n")
        print(f"PDF file is in {output_pdf_file}")
        
        return output_pdf_file

    def __build_svg(self, pdf_file: Path):
        output_svg_dir = self.output_dir / "svg"
        output_svg_dir.mkdir(parents=True, exist_ok=True)

        print("Converting PDF to SVG")

        output_svg_file = output_svg_dir / self.target_name.with_suffix(".%d.svg")
        run([
            "pdf2svg",
            pdf_file,
            output_svg_file,
            "all"
        ])

output_dir = Path("output")
resume_target = Target(
    input_file_name="resume.tex",
    output_dir=output_dir
)
cv_target = Target(
    input_file_name="cv.tex",
    output_dir=output_dir
)
resume_target.build()
cv_target.build()
