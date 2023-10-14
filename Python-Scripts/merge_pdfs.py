import os
import PyPDF2

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfFileWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def collect_pdfs(dir_path):
    pdfs = []
    for foldername, subfolders, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.endswith('.pdf'):
                pdfs.append(os.path.join(foldername, filename))
    return pdfs

def main():
    dir_path = '/path/to/your/folder'  # replace with your directory path
    output = 'merged.pdf'  # final output 

    all_pdfs = collect_pdfs(dir_path)

    merge_pdfs(all_pdfs, output)

if __name__ == '__main__':
    main()
