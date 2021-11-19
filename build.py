#!/usr/bin/env python3

from os.path import dirname, realpath, join
from os import chdir
from subprocess import run

script_dir = dirname(realpath(__file__))
chdir(script_dir)

input_file = "resume.tex"
output_pdf_file_name = "resume.pdf"
output_svg_file_name = "resume.svg"
output_root = "output"
output_pdf_dir = join(output_root, "pdf")
output_svg_dir = join(output_root, "svg")
output_pdf_file = join(output_pdf_dir, output_pdf_file_name)
output_svg_file = join(output_svg_dir, output_svg_file_name)

# build pdf
run([
    "latexmk",
    "-xelatex",
    "-synctex=1",
    "-interaction=nonstopmode",
    "-file-line-error",
    f"-outdir={output_pdf_dir}",
    f'"{input_file}"'
])
print("\n")
print(f"PDF file is in {output_pdf_file}")

print("Converting PDF to SVG")
run([
    "dvisvgm",
    "--pdf",
    f"--output={output_svg_file}",
    output_pdf_file
])
print(f"SVG file is in {output_svg_file}")