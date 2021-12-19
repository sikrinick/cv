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
        target_name = Path(self.input_file_name).with_suffix("")

        self.output_pdf_dir = output_dir / "pdf" / target_name
        self.output_pdf_name = target_name.with_suffix(".pdf")
        self.output_pdf_file = self.output_pdf_dir / self.output_pdf_name

        self.output_svg_dir = output_dir / "svg"
        self.output_svg_name = target_name.with_suffix(".svg")
        self.output_svg_file = self.output_svg_dir / self.output_svg_name

        self.output_pdf_dir.mkdir(parents=True, exist_ok=True)
        self.output_svg_dir.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.__build_pdf()
        self.__build_svg()
        

    def __build_pdf(self):
        run([
            "latexmk",
            "-xelatex",
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            f"-outdir={self.output_pdf_dir}",
            f'"{self.input_file_name}"'
        ])
        print("\n")
        print(f"PDF file is in {self.output_pdf_file}")

    def __build_svg(self):
        print("Converting PDF to SVG")
        run([
            "dvisvgm",
            "--pdf",
            f"--output={self.output_svg_file}",
            self.output_pdf_file
        ])
        print(f"SVG file is in {self.output_svg_file}")


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
