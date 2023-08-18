import os
from pdf2docx import Converter


pdf_directory = "./pdf"
output_directory = "./doc"

os.makedirs(output_directory, exist_ok=True)

pdf_files = [f for f in os.listdir(pdf_directory) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("No PDF files found in the directory.")
else:
    for pdf_file in pdf_files:
        input_pdf_path = os.path.join(pdf_directory, pdf_file)
        output_docx_path = os.path.join(output_directory, pdf_file.replace(".pdf", ".docx"))

        cv = Converter(input_pdf_path)
        cv.convert(output_docx_path, start=0, end=None)
        cv.close()

        print(f"PDF '{pdf_file}' converted to DOCX '{output_docx_path}'.")

print("Conversion process complete.")

